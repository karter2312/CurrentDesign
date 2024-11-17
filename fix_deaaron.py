import re

def fix_all_apostrophes(script_path, fixed_script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()

    # Replace all instances of `\'` with `''`
    # This targets names like De'Aaron Fox, De'Andre Hunter, etc.
    sql_script_fixed = re.sub(r"\\'", "''", sql_script)

    # Write the corrected script to a new file
    with open(fixed_script_path, 'w') as fixed_file:
        fixed_file.write(sql_script_fixed)

# Paths to the cleaned and fixed SQL file
fix_all_apostrophes('cleaned_nba.sql', 'fixed_nba_final_all.sql')
