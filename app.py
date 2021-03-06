import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '500005505:AAGn3xAUZGyg2l5x-_ORRiArYbs7JCkX1XY'
WEBHOOK_URL = 'https://50afaa2f.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'jokelist',
        'jokeinorder',
        'joke1',
        'joke2',
        'joke3',
        'joke4',
        'joke5'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'jokelist',
            'conditions': 'is_going_to_jokelist'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'jokeinorder',
            'conditions': 'is_going_to_jokeinorder'
        },
         {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'user',
            'conditions': 'jokelist_to_home'
        },
        {
            'trigger': 'advance',
            'source': 'jokeinorder',
            'dest': 'user',
            'conditions': 'jokeinorder_to_home'
        },
        {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'joke1',
            'conditions': 'list_to_joke1'
        },
        {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'joke2',
            'conditions': 'list_to_joke2'
        },
        {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'joke3',
            'conditions': 'list_to_joke3'
        },
        {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'joke4',
            'conditions': 'list_to_joke4'
        },
        {
            'trigger': 'advance',
            'source': 'jokelist',
            'dest': 'joke5',
            'conditions': 'list_to_joke5'
        },
        {
            'trigger': 'go_back',
            'source': [
                'joke1',
                'joke2',
                'joke3',
                'joke4',
                'joke5'
            ],
            'dest': 'jokelist'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
