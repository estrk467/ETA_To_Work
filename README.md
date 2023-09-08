# ETA_To_Work
This a python script that sends you a text message every morning with your estimated commute time and approximate time of arrival from your home to your work. Of course, it does not have to be just your home and work, it can be any two addresses that you would like to get a text message with the estimated time of arrival.

# **Installations**
Make sure you have pip installed to help you install twilio and googlemaps client

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python3 get-pip.py
```

Install twilio client
```
pip3 install twilio
```

Install python googlemaps client
```
pip3 install googlemaps
```

# **Google API Key**
This script relies on Google Maps API, you have to create your own key and use within this script in order for it to run.

Replace `"YOUR_API_KEY"` with your OWN key but make sure to keep the quotes. 


# **Twilio Client**
Since we are going to receive SMS messages we will be using Twilio as our client to send those messages. You will need to create a Twilio account to get your twilio phone number, account SID, and authorization token.

Replace `'YOUR_TWILIO_SID'` with your own SID

Replace `'YOUR_TWILIO_AUTH_TOKEN'` with your own Authorization Token

Replace `'YOUR_TWILIO_NUMBER'` with your own Twilio phone number

Make sure you leave the single quotes. 

# **Text Message**
You should get a similar text message as the following 

![IMG_5182](https://github.com/estrk467/ETA_To_Work/assets/73969422/54a9c244-05fd-4e24-ae30-3bda0fe2cb0a)

# **Conclusion**
I had a lot of fun doing this script as it was my first time working with Twilio. I didn't know what to expect when starting this project but working with Twilio was not as hard as I thought it was going to be. The only thing that does suck is that I can't really automate this message as I don't want to be charged every day for getting a text message. Twilio only gives you limited credits for the free trial. The other downside is that I also don't want to have a cron job running on my computer all day just for me to get a text message. I did do some research and a solution could potentially be using a rasberry pi. :)


