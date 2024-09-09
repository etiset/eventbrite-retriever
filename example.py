from retriever import get_all_upcoming_events
import json
import os

# The organization page url.
organzation_page_url = "https://www.eventbrite.com/o/leaderboard-games-32824819501"

# Retrieve all upcoming events based on the organization page url.
evnts = get_all_upcoming_events(organzation_page_url)
print(f"Retrieved {len(evnts)} upcoming events.")

# Check if "output" directory exists. If not, create it.
if not os.path.isdir("output"):
  os.mkdir("output")

# Write the data of all the upcoming events to a json file.
with open("output/upcoming_events.json", "w") as json_file:
  json.dump(evnts, json_file, indent=2)