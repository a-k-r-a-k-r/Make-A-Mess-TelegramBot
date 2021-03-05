import requests
import time
count=1
user_time = int(input("Enter the time interval: "))
bot_token = input("Enter the token key of your bot: ")
group_chat_id = input("Enter the chat id: ")
message_to_print = input("Enter the message to send: ")
while True:
    base_url = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + group_chat_id + "&text=" + message_to_print
    requests.get(base_url)
    count+=1
    time.sleep(user_time)
