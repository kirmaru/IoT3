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
    def __init__(self, name, lum = 0):
        super().__init__(name)
        self.lum = lum
    def setLighting(self):
        return "setLighting<br />"
    def autoLighting(self):
        return "autoLighting<br />"
    def connect(self, source):
        super().connect()
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' +str(self.lum))

    def emulate(self):
        self.lum = random.randint(15, 25)
        return json.dumps({"lights_state": self.lum})
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
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' +str(self.temp)+', ' +str(self.humid))
    def emulate(self):
        self.temp = random.randint(15, 25)
        self.humid = random.randint(15, 25)
        return json.dumps({'temp': self.temp, 'humid': self.humid})
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
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' + str(self.status))
    def emulate(self):
        self.status = random.randint(15, 25)
        return json.dumps({"Doors_state": self.status})


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
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' + str(self.status))
    def emulate(self):
        self.status = random.randint(15, 25)
        return json.dumps({"Alarm_state": self.status})

class Fire_Sensor(Thing):
    def __init__(self, name, status = 0):
        self.status = status
        super().__init__(name)

    def disable(self):
        return f"{self.status} disable<br />"

    def connect(self, source):
        super().connect()
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' + str(self.status))
    def emulate(self):
        self.status = random.randint(15, 25)
        return json.dumps({"Alarm_state": self.status})

class Intruder_Sensor(Thing):
    def __init__(self, name, status = 0):
        self.status = status
        super().__init__(name)

    def disable(self):
        return f"{self.status} disable<br />"

    def connect(self, source):
        super().connect()
        self.emulate()
        print('Connection with '+self.name+' success, new value is ' + str(self.status))
    def emulate(self):
        self.status = random.randint(15, 25)
        return json.dumps({"Alarm_state": self.status})
