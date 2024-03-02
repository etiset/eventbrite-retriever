# eventbrite-retriever
Retrieve all upcoming events for an organization on Eventbrite.

The *retreiver* module is used to obtain a list containing all of an organization's upcoming events.
An example can be found in the *example.py* file.


## Event Data Format
Each JSON-formatted event has the following structure:
* id (string): The event's id.
* url (string): The event's url.
* is_free (boolean): Denotes if the event is free.
* online_event (boolean): Denotes if the event is being held online.
* organizer (object): Information about the organization responsible for the event.
  * id (string): The organizer's id.
  * name (string): The organizer's name.
  * url (string): The organizer's url.
  * website (string): The organizer's website url.
  * start (object): Information about the event's start time.
    * utc (string): The event's start time in UTC format.
    * timezone (string): The event's timezone.
  * end (object): Information about the event's end time.
    * utc (string): The event's end time in UTC format.
    * timezone (string): The event's timezone.
  * venue (object): Information about the event's venue.
    * name (string): The venue's name.
    * address_1 (string): The venue's address line 1.
    * address_2 (string): The venue's address line 2.
    * city (string): The venue's city.
    * region (string): The venue's region.
    * country (string): The venue's country.
    * postal_code (string): The venue's postal code.
    * latitude (string): The venue's latitude.
    * longitude (string): The venue's longitude.
  * name (string): The event's name.
