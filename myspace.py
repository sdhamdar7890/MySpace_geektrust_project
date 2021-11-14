class MeetingRoom:
    def __init__(self):
        self.start_time = []
        self.end_time = []

    def is_vacant(self, start, end):
        for i in range(len(self.start_time)):
            if self.start_time[i] <= start < self.end_time[i]:
                return False
            elif self.start_time[i] <= end < self.end_time[i]:
                return False
        return True

    def booking(self, start, end):
        if start.minute % 15 == 0 and end.minute % 15 == 0:
            self.start_time.append(start)
            self.end_time.append(end)
        else:
            print("INCORRECT VALUE")


class AvailableRoom:
    def __init__(self):
        self.room = {"C-Cave": MeetingRoom(), "D-Tower": MeetingRoom(), "G-Mansion": MeetingRoom()}

    def vacancy(self, start, end):
        answer = []
        for key in self.room.keys():
            if self.room[key].is_vacant(start, end):
                answer.append(key)
        if len(answer):
            return answer
        else:
            return ['NO_VACANT_ROOM']

    def book(self, start, end, people):
        vacant_room = self.vacancy(start, end)
        if people <= 3 and len(vacant_room) > 0:
            self.room[vacant_room[0]].booking(start, end)
            print(vacant_room[0])
        elif people <= 7 and len(vacant_room) > 0:
            if vacant_room[0] == "C-Cave" and len(vacant_room) > 1:
                self.room[vacant_room[1]].booking(start, end)
                print(vacant_room[1])
            elif vacant_room[0] != "C-Cave":
                self.room[vacant_room[0]].booking(start, end)
                print(vacant_room[0])
            else:
                print("NO_VACANT_ROOM")
        elif people <= 20 and len(vacant_room) > 0:
            if vacant_room[-1] == "G-Mansion":
                self.room[vacant_room[-1]].booking(start, end)
                print(vacant_room[-1])
            else:
                print("NO_VACANT_ROOM")
        else:
            print("NO_VACANT_ROOM")
