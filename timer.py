import time
timer_in_seconds = input("enter the time in seconds for the timer: ")
def countDown_timer(timer_in_seconds):
    minutes = int(timer_in_seconds/60)
    seconds = int(timer_in_seconds%60)
    timer = f'{minutes}:{seconds}'
    print(timer)

countDown_timer(int(timer_in_seconds))