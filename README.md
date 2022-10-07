# crontab
HHA 507, SBU


1. Create a new GitHub repo called crontab


2. Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters:
    • One should pull down data from an API once a day (don’t care about what time) 
    • One should pull down data every Sunday night at 10:00pm 
    • One should pull down data


Report the appropriate cron job command (like in page 12 of this presentation) within the GitHub repo within the markdown file.


So repo should contain two files: 
    - markdown file (.md) with instructions for how the python files were automated using crontab 
    - a python file (.py) that contains the python code for pulling down the data 
    


/// the retrieved data should then be saved locally on that machine where the cron job is running 
    - e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10- 10.csv)

#How to install and perform cronjob

#Step 2:Install and log into VM/terminal

#Step 2: Update OS
sudo apt-get update
sudo apt upgrade

#Step 3: use git clone to copy and paste your github repo
git clone [insert url-remove brackets]

#Step 4: check if crontab and python 3 is installed
crontab -h
python3

#Step 5: Change directory to the github repo to find directory information and file presence 

#Step 6: From that directory, run:
crontab -e
Scroll to the bottom of the page and insert

For once a day
0 0 * * * usr/bin/python3 /crontab/cron_app.py > log.txt 2>&1 &
At 10pm every sunday
0 22 * * SUN usr/bin/python3 /crontab/cron_app.py > log.txt 2>&1 &
At very quarter
0 0 1 */3 * usr/bin/python3 /crontab/cron_app.py > log.txt 2>&1 &

#Step 7: Save and exit the file

#Step 8: Check to see the status of cron running
systemctl status cron
