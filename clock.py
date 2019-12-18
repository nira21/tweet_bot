from apscheduler.schedulers.blocking import BlockingScheduler
import words

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
def timed_job():
    words.puttweet()

if __name__ == "__main__":
    twische.start()
