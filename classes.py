from flask import request
import abc
import json
import random
import pymongo
import datetime
import numpy


# class Logger:
#     def __init__(self, db_name):
#         self.client = pymongo.MongoClient('mongodb://localhost:27017/')
#         self.db = self.client[db_name]
#
#     def log_lighting(self, data):
#         self.db['LightingLogs'].insert_one({
#             'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'data': data
#         })
#
#     def log_error(self, error_message):
#         self.db['ErrorLogs'].insert_one({
#             'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'error': error_message
#         })
#     def avg_lum(self):
#         cursor = self.db['lum'].find()
#         lum_data = []
#         for elem in cursor:
#             lum_data.append(elem['lum'])
#         return round(numpy.mean(lum_data), 1)
#
#     def max_lum(self):
#         cursor = self.db['lum'].find()
#         lum_data = []
#         for elem in cursor:
#             lum_data.append(elem['lum'])
#         return max(numpy.mean(lum_data))

class Thing(abc.ABC):
    def __init__(self, name):
        self.name = name
        print("THE THING")

    @abc.abstractmethod
    def connect(self, *args):
        print("CONNECTION")

class lighting(Thing):
    def __init__(self, name, lum=0):
        super().__init__(name)
        self.lum = lum
        self.power = "Off"
        self.avg = 1
        self.max = 1
        # Initialize MongoDB connection
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['IOT_logger_db']

    def lum_chart(self):
        cursor = self.db['LightingLogs2'].find()
        lum_data = []
        time_data = []
        for elem in cursor:
            lum_data.append(elem['lum'])
            time_data.append(elem['timestamp'])
        return {'lum_data': lum_data, 'time_data': time_data}
    def update_power(self):
        if self.lum < 300:
            self.power = "On"
        else:
            self.power = "Off"

    def log_lighting(self, lum):
        self.db['LightingLogs2'].insert_one({
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'lum': lum  # Сохраняем только значение lum
        })

    def log_error(self, error_message):
        self.db['ErrorLogs'].insert_one({
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'error': error_message
        })

    def avg_lum(self):
        cursor = self.db['LightingLogs2'].find()
        lum_data = [elem['lum'] for elem in cursor]
        print("lum_data:", lum_data)  # Добавляем отладочное сообщение
        if lum_data:
            return round(numpy.mean(lum_data), 1)
        else:
            return 0

    def max_lum(self):
        cursor = self.db['LightingLogs2'].find()
        lum_data = [elem['lum'] for elem in cursor]
        print("lum_data:", lum_data)  # Добавляем отладочное сообщение
        if lum_data:
            return max(lum_data)
        else:
            return 0

    def connect(self, source):
        super().connect()
        try:
            value = int(request.args.get('value', ''))
            self.lum = value
            self.update_power()
            self.log_lighting(self.lum)
            self.max = self.max_lum()
            self.avg = self.avg_lum()

            response = {"power": self.power, "lum": self.lum, "avg_lum": self.avg, "max_lum": self.max}


            print('Connection with ' + self.name + ' success, new value is ' + str(self.lum))
            return response
        except ValueError:
            error_message = 'Error: int type requested'
            self.log_error(error_message)
            print(error_message)
            return {"error": error_message}
class Climate_Control(Thing):
    def __init__(self, name, humid = 0, temp = 0):
        super().__init__(name)
        self.humid = humid
        self.temp = temp

    def connect(self, source):
        super().connect()
        try:
            float(request.args.get('temp', ''))
            float(request.args.get('humid', ''))
            self.temp = request.args.get('temp', '')
            self.humid = request.args.get('humid', '')
            print('Connection with '+self.name+' success, new value is ' +str(self.temp)+', ' +str(self.humid))
        except ValueError:
            print('Error: float type requested')
    # def emulate(self):
    #     self.temp = random.randint(15, 25)
    #     self.humid = random.randint(15, 25)
    #     return json.dumps({'temp': self.temp, 'humid': self.humid})
class Garage_Doors(Thing):
    def __init__(self, name, status = 0):
        super().__init__(name)
        self.status = status

    def openDoor(self):
        return "openDoor<br />"

    def closeDoor(self):
        return "closeDoor<br />"
    def connect(self, source):
        super().connect()
        try:
            int(request.args.get('value', ''))
            self.value = request.args.get('value', '')
            print('Connection with '+self.name+' success, new value is ' + str(self.value))
        except ValueError:
            print('Error: integer is requested')
    # def emulate(self):
    #     self.status = random.randint(15, 25)
    #     return json.dumps({"Doors_state": self.status})


class Smart_Garage:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def menu(self):
        return "menu"

    def change_settings(self):
        return f"{self.user}"

    def default_settings(self):
        return f"{self.password}"

    def addUser(self):
        return "addUser<br />"

    def deleteUser(self):
        return "User deleted"
class Alarm_system(Thing):
    def __init__(self, name, status = 0):
        super().__init__(name)
        self.status = status

    def disableAlarm(self):
        return f"{self.status} disable alarm"

    def setAlarm(self):
        return f"{self.status} set alarm"

    def enableAlarm(self):
        return f"{self.status} enable alarm"

    def connect(self, source):
        super().connect()
        self.value = request.args.get('value', '')
        print('Connection with '+self.name+' success, new value is ' + str(self.value))
    # def emulate(self):
    #     self.status = random.randint(15, 25)
    #     return json.dumps({"Alarm_state": self.status})

class Fire_Sensor(Thing):
    def __init__(self, name, status = 0):
        self.status = status
        super().__init__(name)

    def disable(self):
        return f"{self.status} disable<br />"

    def connect(self, source):
        super().connect()
        self.value = request.args.get('value', '')
        print('Connection with '+self.name+' success, new value is ' + str(self.value))
    # def emulate(self):
    #     self.status = random.randint(15, 25)
    #     return json.dumps({"Alarm_state": self.status})

class Intruder_Sensor(Thing):
    def __init__(self, name, status = 0):
        self.status = status
        super().__init__(name)

    def disable(self):
        return f"{self.status} disable<br />"

    def connect(self, source):
        super().connect()
        self.value = request.args.get('value', '')
        print('Connection with '+self.name+' success, new value is ' + str(self.value))
    # def emulate(self):
    #     self.status = random.randint(15, 25)
    #     return json.dumps({"Alarm_state": self.status})
