import sys
import myspace
from datetime import datetime


def main():
    input_file = sys.argv[1]
    file_name = open(input_file, 'r', encoding='utf-8')
    booking = myspace.AvailableRoom()
    for line in file_name:
        command = list(line.split())
        if len(command) > 4:
            print("INCORRECT_INPUT")
        else:
            start_time = datetime.strptime(command[1], '%H:%M').time()
            end_time = datetime.strptime(command[2], '%H:%M').time()
            if (start_time.minute % 15 != 0) or (end_time.minute % 15 != 0):
                print("INCORRECT_INPUT")
            elif (command[0].lower() == "vacancy") and (end_time > start_time):
                result = booking.vacancy(start_time, end_time)
                print(*result)
            elif (command[0].lower() == "book") and (end_time > start_time):
                booking.book(start_time, end_time, int(command[3]))
            else:
                print("INCORRECT_INPUT")


if __name__ == "__main__":
    main()
