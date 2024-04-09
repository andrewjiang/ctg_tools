
# tg_script.py
This script is used to get a count of activity within a TG group chat. It will display the TG display name and a count of their messages.

1. Go to Export Chat History and make sure the format is JSON
2. Put the JSON file (e.g. "chatfile.json") in the same directory as the script 
3. Run `python tg_script.py chatfile.json` in your terminal
4. You'll get a output json chatfile_summary.json with a list of display names and their message count