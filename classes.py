from flask import request
import abc
import json
import random

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

    def setLighting(self):
        return "setLighting<br />"

    def autoLighting(self):
        return "autoLighting<br />"

    def update_power(self):
        if self.lum < 300:
            self.power = "On"
        else:
            self.power = "Off"

    def connect(self, source):
        super().connect()
        try:
            float(request.args.get('value', ''))
            self.lum = float(request.args.get('value', ''))
            self.update_power()
            print('Connection with ' + self.name + ' success, new value is ' + str(self.lum))
            return {"power": self.power, "lum": self.lum}  # Return power and lum as dictionary
        except ValueError:
            print('Error: float type requested')
            return {"error": "float type requested"}  # Return error if conversion fails
class Climate_Control(Thing):
    def __init__(self, name, humid = 0, temp = 0):
        super().__init__(name)
        self.humid = humid
        self.temp = temp

    def setTemp(self):
        return "setTemp<br />"

    def setHumid(self):
        return "setHumid<br />"

    def autoClimate(self):
        return "autoClimate<br />"

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
