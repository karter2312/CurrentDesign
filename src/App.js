import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css'; // Make sure you style your app properly with CSS

function App() {
  const [bostonStats, setBostonStats] = useState([]);
  const [nbaStats, setNbaStats] = useState([]);
  const [teams, setTeams] = useState([]); // State to store unique teams
  const [selectedTeam1, setSelectedTeam1] = useState("");
  const [selectedTeam2, setSelectedTeam2] = useState("");
  const [matchupResult, setMatchupResult] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    // Fetch initial data for stats and teams
    axios.get('http://127.0.0.1:8000/show_data')
      .then(response => {
        console.log("Show Data Response:", response.data);
        const nbaData = convertNestedObjectToArray(response.data.nba_stats);
        setNbaStats(nbaData);

        // Extract unique teams
        const uniqueTeams = Array.from(new Set(nbaData.map(player => player.Team)));
        setTeams(uniqueTeams);
      })
      .catch(error => {
        setError("Error fetching data");
        console.error("Error fetching data:", error);
      });

  }, []);

  // Function to convert nested response data into an array of player objects
  const convertNestedObjectToArray = (nestedData) => {
    const keys = Object.keys(nestedData);
    const length = Object.keys(nestedData[keys[0]]).length; // Assume all columns have the same length

    let dataArray = [];
    for (let i = 0; i < length; i++) {
      let player = {};
      keys.forEach(key => {
        player[key] = nestedData[key][i];
      });
      dataArray.push(player);
    }

    return dataArray;
  };

  // Handle prediction of specific matchups
  const handleMatchupPrediction = () => {
    if (selectedTeam1 && selectedTeam2) {
      // Implement logic to get the prediction for the selected matchup
      axios.get(`http://127.0.0.1:8000/predict?team1=${selectedTeam1}&team2=${selectedTeam2}`)
        .then(response => {
          const prediction = response.data.predictions;
          if (prediction) {
            setMatchupResult(prediction.Prediction ? `${selectedTeam1} wins` : `${selectedTeam2} wins`);
          } else {
            setMatchupResult("No prediction available for this matchup");
          }
        })
        .catch(error => {
          console.error("Error fetching predictions:", error);
          setMatchupResult("Error fetching predictions");
        });
    }
  };

  return (
    <div className="App">
      {/* Hero Banner Section */}
      <div className="hero-banner">
        <h1>Stream the Chase for the NBA Championship</h1>
        <p>More games. Higher stakes. Stay tuned to every game and enjoy the NBA experience.</p>
      </div>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Matchup Predictions Section */}
      <div className="matchup-predictions">
        <h2>Matchup Predictions</h2>
        <label>Select Team 1: </label>
        <select value={selectedTeam1} onChange={(e) => setSelectedTeam1(e.target.value)}>
          <option value="">Select a Team</option>
          {teams.map((team, index) => (
            <option key={index} value={team}>{team}</option>
          ))}
        </select>

        <label>Select Team 2: </label>
        <select value={selectedTeam2} onChange={(e) => setSelectedTeam2(e.target.value)}>
          <option value="">Select a Team</option>
          {teams.map((team, index) => (
            <option key={index} value={team}>{team}</option>
          ))}
        </select>

        <button onClick={handleMatchupPrediction}>Predict Matchup</button>

        {matchupResult && <p>Prediction Result: {matchupResult}</p>}
      </div>

      {/* Team Stats Section */}
      <div className="teams-stats">
        <h2>NBA Team Stats</h2>
        {teams.map((team, index) => (
          <div key={index} className="team-stats">
            <h3>{team}</h3>
            <table border="1">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Player Name</th>
                  <th>Position</th>
                  <th>Age</th>
                  <th>Games Played</th>
                  <th>Points Per Game</th>
                </tr>
              </thead>
              <tbody>
                {nbaStats.filter(player => player.Team === team).map((player, index) => (
                  <tr key={index}>
                    <td>{index + 1}</td>
                    <td>{player.Player_Name}</td>
                    <td>{player.Position}</td>
                    <td>{player.Age}</td>
                    <td>{player.Games_Played}</td>
                    <td>{player.Points_Per_Game}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
