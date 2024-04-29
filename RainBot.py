import cloudscraper as cs
from time import sleep

scraper = cs.create_scraper()

print("cool started")

while True:
    rain_active = False
    print("sending")
    if not rain_active:
        response = scraper.get("https://api.bloxflip.com/chat/history")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if data['rain']['active']:
                prize = data['rain']['prize']
                message = f"@everyone\nActive Rain ${prize} [join rain](https://bloxflip.com)"
                webhook_url = "https://discord.com/api/webhooks/1230986498657226812/E8xdf9eRVEMIFmlgKVYfyrv0ExL0A5alS0PxC65funxZdx7PC76Uu5xikUOg2ygjojiv"
                payload = {"content": message}
                response = scraper.post(webhook_url, json=payload)
                
                # Check if the POST request was successful
                if response.status_code == 200:
                    rain_active = True
                else:
                    print("Failed to send message to Discord webhook.")
            else:
                print("Rain not active.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    sleep(3)  # Sleep for 1 minute before checking again