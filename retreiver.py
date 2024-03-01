import requests

def get_organization_id(organization_page_url):
  # Extract the organization id from the its page url.
  return organization_page_url.split("-")[-1]

def process_event_data(event_data):
  # Process the event data. Return a dictionary with the desired key-value pairs.

  # The keys and subkeys to track in the event data. These keys and subkeys can be easily extracted
  # from event_data using dictionary comprehensions.
  keys_to_track = ["id", "url", "is_free", "online_event"]
  subkeys_to_track = {
    "organizer": ["id", "name", "url", "website"],
    "start": ["utc", "timezone"],
    "end": ["utc", "timezone"],
  }

  result = {key: event_data[key] for key in keys_to_track}
  for key in subkeys_to_track:
    result[key] = {subkey: event_data[key][subkey] for subkey in subkeys_to_track[key]}

  # Add venue data to the result.
  venue_address_subkeys_to_track = ["address_1", "address_2", "city", "region", "country",
                                    "postal_code", "latitude", "longitude"]

  result["venue"] = {"name": event_data["venue"]["name"]}
  for subkey in venue_address_subkeys_to_track:
    result["venue"][subkey] = event_data["venue"]["address"][subkey]  

  # Add event date to the result.
  result["name"] = event_data["name"]["text"]

  return result

def process_response_data(data):
  # Process the response data. Return a list of processed events and a boolean indicating whether
  # there are more pages of events to retrieve.
  evnts = [process_event_data(evnt) for evnt in data["events"]]

  return evnts, data["has_next_page"]

if __name__ == "__main__":
  organzation_page_url = "https://www.eventbrite.com/o/leaderboard-games-32824819501"
  organization_id = get_organization_id(organzation_page_url)

  second_page_url = f"https://www.eventbrite.com/org/{organization_id}/showmore/?page_size=12&type=future&page=2"

  try:
    response = requests.get(second_page_url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    response_json = response.json()

    if response_json["success"]:
      evnts, has_next_page = process_response_data(response_json["data"])
      print(f"Event Count: {len(evnts)}, Has Next Page: {has_next_page}")

  except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
