# ETA_To_Work
This a python script that sends you a text message every morning with your estimated commute time and approximate time of arrival from your home to your work. Of course, it does not have to be just your home and work, it can be any two addresses that you would like to get a text message. 
#**Google API Key**
This script relies on Google Maps API, you have to create your own key and use within this script in order for it to run.
Replace "YOUR_API_KEY" with your OWN key but make sure to keep the quotes. 
#**Twilio Client**
Since we are going to receive SMS messages we will be using Twilio as our client to send those messages. You will need to create a Twilio account to get your twilio phone number, account SID, and authorization token.

Replace 'YOUR_TWILIO_SID' with your own SID
Replace 'YOUR_TWILIO_AUTH_TOKEN' with your own Authorization Token
Replace 'YOUR_TWILIO_NUMBER' with your own Twilio phone number

Make sure you leave the single quotes. 
#**Installations**
Make sure you have pip installed 
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py 

Install twilio client
pip3 install twilio

Install python googlemaps client
pip3 install googlemaps
