from retreiver import get_all_upcoming_events
import json
import os

organzation_page_url = "https://www.eventbrite.com/o/leaderboard-games-32824819501"

evnts = get_all_upcoming_events(organzation_page_url)
print(f"Retrieved {len(evnts)} upcoming events.")

# Check if "output" directory exists. If not, create it.
if not os.path.isdir("output"):
  os.mkdir("output")

# Write the data of all the upcoming events to a json file.
with open("output/upcoming_events.json", "w") as file:
  json.dump(evnts, file, indent=2)