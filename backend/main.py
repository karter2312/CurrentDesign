# backend/main.py
from fastapi import FastAPI
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import logging
from fastapi.middleware.cors import CORSMiddleware

# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connections
engine_boston = create_engine('mysql+pymysql://root:blessing23@127.0.0.1:3306/basketballdb')
engine_nba = create_engine('mysql+pymysql://root:blessing23@127.0.0.1:3306/basketballdb')
metadata = MetaData()

@app.get("/")
def read_root():
    return {"message": "Welcome to the NBA Web App"}

@app.get("/show_data")
def show_data():
    try:
        # Load data from the databases
        logging.info("Loading data from databases...")
        boston_stats = pd.read_sql_table('boston_celtics_per_game_stats_renamed', con=engine_boston)
        nba_stats = pd.read_sql_table('nba_player_stats_2023_2024', con=engine_nba)
        
        # Log data preview
        logging.info("Boston Stats Preview:\n%s", boston_stats.head())
        logging.info("NBA Stats Preview:\n%s", nba_stats.head())
        
        return {
            "boston_stats": boston_stats.to_dict(),  # Return all rows, not just head
            "nba_stats": nba_stats.to_dict()
        }
    except Exception as e:
        logging.error("Error occurred while loading data: %s", str(e))
        return {"error": str(e)}

@app.get("/teams")
def get_teams():
    try:
        # Load NBA stats data from the database
        logging.info("Loading NBA stats data for teams...")
        nba_stats = pd.read_sql_table('nba_player_stats_2023_2024', con=engine_nba)

        # Extract unique teams
        unique_teams = nba_stats['Team'].unique().tolist()
        logging.info("Teams available: %s", unique_teams)

        return {"teams": unique_teams}
    except Exception as e:
        logging.error("Error occurred while loading team data: %s", str(e))
        return {"error": str(e)}

@app.get("/predict")
def predict():
    try:
        # Load data from the databases
        logging.info("Loading data from databases...")
        boston_stats = pd.read_sql_table('boston_celtics_per_game_stats_renamed', con=engine_boston)
        nba_stats = pd.read_sql_table('nba_player_stats_2023_2024', con=engine_nba)
        
        # Log data preview
        logging.info("Boston Stats Preview:\n%s", boston_stats.head())
        logging.info("NBA Stats Preview:\n%s", nba_stats.head())
        
        # Preprocess the data
        player_stats_df = preprocess_data(nba_stats)
        logging.info("Player Stats DataFrame after preprocessing:\n%s", player_stats_df.head())
        
        # Train the model
        model, model_features, accuracy, report = train_model(player_stats_df)
        logging.info("Model trained. Accuracy: %s", accuracy)
        
        # Identify key players
        key_players = identify_key_players(player_stats_df)
        logging.info("Key Players Identified:\n%s", key_players)
        
        # Generate matchups and simulate scenarios
        selected_teams = key_players['Team'].unique().tolist()
        matchups = generate_matchups(selected_teams)
        results_df = simulate_matchup_scenarios(matchups, key_players, player_stats_df, model, model_features)
        logging.info("Simulation Results:\n%s", results_df)
        
        return {
            "predictions": results_df.to_dict(),
            "accuracy": accuracy,
            "report": report
        }
    except Exception as e:
        logging.error("Error occurred during prediction: %s", str(e))
        return {"error": str(e)}

# Function to preprocess data
def preprocess_data(nba_stats):
    # Select relevant columns from the database data
    nba_stats = nba_stats[['Player_Name', 'Position', 'Age', 'Team', 'Games_Played', 'Minutes_Played', 'Field_Goal_Percentage', 'Three_Point_Percentage', 'Assists', 'Points_Per_Game']]
    return nba_stats

# Function to train the model
def train_model(player_stats_df):
    player_stats_df = player_stats_df.copy()
    player_stats_df['High_Scorer'] = player_stats_df['Points_Per_Game'] > 15
    X = player_stats_df[['Points_Per_Game', 'Minutes_Played', 'Field_Goal_Percentage', 'Three_Point_Percentage', 'Assists', 'Age']]
    y = player_stats_df['High_Scorer']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    model_features = X.columns.tolist()
    return model, model_features, accuracy, report

# Function to identify key players
def identify_key_players(player_stats_df):
    key_players = player_stats_df.loc[player_stats_df.groupby('Team')['Points_Per_Game'].idxmax()].reset_index(drop=True)
    return key_players

# Function to generate matchups
def generate_matchups(teams):
    matchups = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            matchups.append((teams[i], teams[j]))
            matchups.append((teams[j], teams[i]))
    return matchups

# Function to simulate matchup scenarios
def simulate_matchup_scenarios(matchups, key_players, player_stats_df, model, model_features):
    results = []
    for team1, team2 in matchups:
        if team1 not in key_players['Team'].values or team2 not in key_players['Team'].values:
            continue

        team1_key_player = key_players[key_players['Team'] == team1].iloc[0]
        team2_key_player = key_players[key_players['Team'] == team2].iloc[0]

        features = ['Points_Per_Game', 'Minutes_Played', 'Field_Goal_Percentage', 'Three_Point_Percentage', 'Assists', 'Age']

        combined_stats_df = pd.DataFrame([{f: (team1_key_player[f] + team2_key_player[f]) / 2 for f in features}])
        combined_stats_df = combined_stats_df.values

        prediction = model.predict(combined_stats_df)

        results.append({
            'Team1': team1,
            'Team2': team2,
            'Prediction': prediction[0]
        })

    return pd.DataFrame(results)

# Run with: uvicorn main:app --reload
