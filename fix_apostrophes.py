import re

def correct_quotes_in_sql(script_path, fixed_script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()

    # Correct quotes in INSERT statements by properly escaping them
    corrected_script = re.sub(
        r"INSERT INTO .*? VALUES \((.*?)\);",
        lambda match: re.sub(r"(?<=,|\()'([^']*?)'(?=,|\))", lambda m: f"'{m.group(1).replace(\"'\", \"''\")}'", match.group(0)),
        sql_script
    )

    # Write the corrected script to a new file
    with open(fixed_script_path, 'w') as fixed_file:
        fixed_file.write(corrected_script)

# Paths to the corrected SQL files
correct_quotes_in_sql('cleaned_boston.sql', 'corrected_boston.sql')
correct_quotes_in_sql('cleaned_nba.sql', 'corrected_nba.sql')
