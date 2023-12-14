import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


from datetime import datetime, timedelta

# Define the start date and end date
start_date = datetime.strptime('12-21-2023', '%m-%d-%Y')
end_date = datetime.strptime('07-31-2024', '%m-%d-%Y')

# Find the last Friday of July 2024
while end_date.weekday() != 4:  # 0 is Monday, 1 is Tuesday, ..., 4 is Friday
    end_date -= timedelta(days=1)

# Generate dates
current_date = start_date
while current_date <= end_date:
    
    





    #replace gabecolli with the owner of the repo and daily-activity with the repo name
    url = "https://api.github.com/repos/gabecolli/daily-activity/milestones"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('githtoken')}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    sprint_end = current_date + timedelta(days=14)
    data = {
        "title": f"Sprint {current_date.strftime('%m-%d-%Y')} --> {sprint_end.strftime('%m-%d-%Y')}",
        "state": "open",
        "description": "Sprint",
        "due_on": f"{sprint_end.strftime('%Y-%m-%dT%H:%M:%SZ')}",
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    current_date += timedelta(days=14)

    print(response.json())