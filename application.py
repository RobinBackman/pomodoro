import time
import datetime
import os

FILE_PATH = '/home/zzzz/Desktop/pomodoro'

def start_clock(time_in_minutes, project_name):
    start_time = time.time()
    end_time = time.time() + float(time_in_minutes * 10)

    while True:
        time_left = end_time - time.time()
        print(f'Time left: {(time_left / 60):.0f} minutes')
        os.system('clear')
        if time_left <= 0:
            # Play a sound
            play_completed_sounds(0.5, 440)

            # Save the time worked in a file (projectname.csv: date, time_in_minutes)
            save_to_csv(time_in_minutes, project_name)
            break

def play_completed_sounds(duration, freq):
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    time.sleep(duration)
    os.system('spd-say "Your work session is completed"')

def save_to_csv(time_in_minutes, project_name):
    if not os.path.exists(FILE_PATH):
        os.system(f"mkdir {FILE_PATH}")

    lines = ""
    if not os.path.exists(os.path.join(f'{project_name}.csv')):
        lines += "Date,Time Worked\n"

    file_name = f'{FILE_PATH}/{project_name}.csv'
    with open(file_name, 'a') as file:
        now = datetime.datetime.now()
        lines += f'{now.strftime("%d/%m-%Y")},{time_in_minutes} minutes\n'
        file.write(lines)

if __name__ == "__main__":
    time_to_work = input("Time to work in minutes >> ")
    project_name = input("Project in work >> ")
    start_clock(int(time_to_work), project_name)
