from requests import request
from random import randint
from time import sleep
from discordwebhook import Discord

urls = []
webhooks = []

for i in webhooks:
    BUMP_WEBHOOK = Discord(url=f'{i}')
    BUMP_WEBHOOK.post(content='AUTOBUMP HAS STARTED', username='DISBOARD')

while True:
    for i in webhooks:
        BUMP_WEBHOOK = Discord(url=f'{i}')
        BUMP_WEBHOOK.post(content='SERVER HAS BEEN AUTOBUMPED!', username='DISBOARD')

    TIME_TO_WAIT = randint(7200, 9000)
    TIME_TO_WAIT_MINUTES = TIME_TO_WAIT / 60
    TIME_TO_WAIT_MINUTES_ROUNDED = int(TIME_TO_WAIT_MINUTES) / 1

    for i in urls:
        DISBOARD_REQUEST = request(url=f'{i}', method='get')
        print(DISBOARD_REQUEST.status_code)
    sleep(TIME_TO_WAIT_MINUTES_ROUNDED)
