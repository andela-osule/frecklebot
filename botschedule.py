import schedule, time, re
from threading import Thread

class Schedule(object):
    """"Schedule for bot to run"""

    def __init__(self, slack_obj):
        self.slack = slack_obj


    def get_users():
        users = []
        with open('users.lst', 'r') as store:
            store = store.read().split()
            for user in store:
                users.append(user[:re.search(':', user).start()])
        print users
        return users
    
    def notify(self, message, users=get_users()):
        rtm = self.slack.rtm.start()
        for user in users:
            im = self.slack.im.open(user)
            self.slack.chat.post_message(im.body['channel']['id'], message, 'frecklebot', True)
            im.close()
    
    def run_at_start(self):
        message = "Hi! Remember to log your activities today on Freckle"    
        self.notify(message)

    def run_at_end(self):
        message = "Great work today! Remember to log your activities today on Freckle"
        self.notify(message) 

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    

    def run(self):
        schedule.every().day.at("09:00").do(self.run_at_start)
        #schedule.every().second.do(self.run_at_end)
        schedule.every().day.at("05:00").do(self.run_at_end)
        t = Thread(target=self.run_schedule)
        t.start()        