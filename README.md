# ✨ Personal Scripts
These a python and shell scripts I use on my computer to automate daily tasks like:
- Creating markdown files for task management (to-do lists, eisenhower matrix)
- Cleaning up misc files on my desktop
- *(TODO)* Summarize and auto-prioritize tasks and dump to a MD file for a daily to-do list
- *(TODO)* Auto backup desktop media & archived repos to FTP
- *(TODO)* Aggregate Solana wallet balances via a custom CLI tool
& more to be added!

## Run locally
Use the following command in your terminal to add a cron job
```
crontab -e
```
Then add the following to the config file using vi
```
<cron syntax> /usr/bin/python3 <path to script>
```
Save and exit vi, and verify that the job was added
```
crontab -l
```
and you're all set!
