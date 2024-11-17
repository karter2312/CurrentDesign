import re

def clean_mysql_script_for_sqlite(script_path, cleaned_script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()

    # Remove MySQL-specific commands like SET, LOCK TABLES, and UNLOCK TABLES
    sql_script_cleaned = re.sub(r"/\*![0-9]+.*?\*/;", "", sql_script, flags=re.DOTALL)
    sql_script_cleaned = re.sub(r"SET .*?;", "", sql_script_cleaned)
    sql_script_cleaned = re.sub(r"LOCK TABLES .*?;", "", sql_script_cleaned)
    sql_script_cleaned = re.sub(r"UNLOCK TABLES;", "", sql_script_cleaned)
    sql_script_cleaned = re.sub(r"ENGINE=.*?;", ";", sql_script_cleaned)  # Remove engine specifications
    sql_script_cleaned = re.sub(r"--.*?\n", "\n", sql_script_cleaned)  # Remove comments

    # Write the cleaned script to a new file
    with open(cleaned_script_path, 'w') as cleaned_file:
        cleaned_file.write(sql_script_cleaned)

# Paths to the cleaned SQL files
clean_mysql_script_for_sqlite('basketballdb_boston_celtics_per_game_stats_renamed.sql', 'cleaned_boston.sql')
clean_mysql_script_for_sqlite('basketballdb_nba_player_stats_2023_2024.sql', 'cleaned_nba.sql')
