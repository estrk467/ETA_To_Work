
#!/usr/bin/python3



import googlemaps
import datetime
from datetime import timedelta
from twilio.rest import Client



def get_commute_duration():
	#Define your home and work locations
	home_address = "YOUR_HOME_ADDRESS"
	work_address = "YOUR_WORK_ADDRESS"

	#set up Google Maps API Client
	google_maps_api_key = "YOUR_API_KEY"
	gmaps = googlemaps.Client(key=google_maps_api_key)

	#Get directions
	directions = gmaps.directions(home_address, work_address, departure_time = 'now')

	#get the duration of the first leg
	duration = directions[0]['legs'][0]['duration']
	return duration
     

def send_text_message(message):
	#Set up Twilio client
	twilio_account_sid= 'YOUR_TWILIO_SID'
	twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
	twilio_phone_number = 'YOUR_TWILIO_NUMBER'
	your_phone_number = 'YOUR_NUMBER'
	client = Client(twilio_account_sid, twilio_auth_token)

        #Set up message
	client.messages.create(
		from_=twilio_phone_number,
		to=your_phone_number,
		body=message
		)

def main():
        #Get duration: text and value
	duration = get_commute_duration()
	
	#calculate the estimated arrival time
	now = datetime.datetime.now()
	arrival_time= (now + timedelta(seconds = duration['value'])).strftime('%I:%M %p')

	#send estimated commute time
	message = (
		f"Good Morning!\n\n"
		f"Estimated commute time from home to work at 9am: {duration['text']}.\n\n"
		f"Leave now for work at 9am to arrive at approximately {arrival_time}.\n"
		)

	send_text_message(message)

if __name__ == "__main__":
	main()
