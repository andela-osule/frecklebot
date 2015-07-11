from os import environ
from flask import Flask, json, jsonify, request, session, redirect, url_for 
from slacker import Slacker


app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent=True)
slack = Slacker(app.config['BOT_API_TOKEN'])
#m = slack.rtm.start()
#m.successful
#im = slack.im.open()
#slack.chat.post_message(im.body['channel']['id'], 'hi there', 'frecklebot', True)
store = open('users.lst', 'w+')
store.close()

@app.route('/')
def index():
    return jsonify(message="Hello World")

@app.route('/incoming', methods=['POST'])
def subscribe():
    """Subscribe to incoming post requests from Slack service"""
    if request.method == 'POST':
        if request.form.get('token') == app.config['BOT_APP_OUTGOING_PAYLOAD_TOKEN']:
            store_user(request.form.get('user_id'), request.form.get('user_name'))
            return jsonify(Status='OK')
        # return jsonify(request.form)
    return jsonify(Status='Unauthorized access')


def store_user(user_id, user_name):
    """Store <user_id>:<user_name> into flat file """
    with open('users.lst', 'a+') as store:
        store_str = store.read()
        if user_id not in store_str:
            store.write(user_id+':'+user_name+'\n')


if __name__=='__main__':
    app.run(debug=True) 