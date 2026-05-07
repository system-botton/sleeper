import argparse
import subprocess
import time

def main():
    parser = argparse.ArgumentParser(description="Уснуть с маком")
    parser.add_argument('minutes', type=int, help='Через сколько минут засыпать')
    args = parser.parse_args()

    seconds = args.minutes * 60
    print(f'Мак уснет через {args.minutes} минут')

    time.sleep(seconds)

    subprocess.run(['pmset', 'sleepnow'])

if __name__ == "__main__":
    main()