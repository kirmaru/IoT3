from flask import Flask, render_template
import classes
import json

app = Flask(__name__)
lights = classes.lighting("lights")
climate = classes.Climate_Control("climate")
doors = classes.Garage_Doors("doors")
alarm = classes.Alarm_system("alarm")
fire = classes.Fire_Sensor("fire")
intruder = classes.Intruder_Sensor("intruder")

@app.route('/light')
def connect_light():
    return json.dump({lights.connect("lights")})


@app.route('/climate')
def ChangeTemp():
    return json.dumps({climate.connect("climate")})

@app.route('/doors')
def connect_Doors():
    return json.dumps({doors.connect("doors")})
@app.route('/alarm')
def connect_Alarm():
    return json.dumps({alarm.connect("alarm")})

@app.route('/fire')
def connect_Fire():
    return json.dumps({fire.connect("fire")})
@app.route('/intruder')
def connect_Intruder():
    return json.dump({intruder.connect("intruder")})


@app.route('/')
def main():

    return render_template('emulators.html')

    #return monitoring_system.menu() + "\n" + monitoring_system.change_settings() + "\n" +monitoring_system.default_settings()+ "\n" + monitoring_system.control() + "\n" + monitoring_system.add_thing() + "\n" + monitoring_system.delete_thing() + "\n" +monitoring_system.delete_user() + "\n" + monitoring_system.add_user() + "\n" + monitoring_system.get_status_info() + "\n" + life_qual.get_humidity(3232) + "\n" + life_qual.get_temperature(7000) + "\n" + life_qual.get_brightness(00) + "\n" + pers_health.get_current_activity(32) + "\n" + pers_health.get_current_pulse(17) + "\n" + pers_health.get_sleep_info(2) + "\n" + pers_health.connect("port 5000 ") + "\n" + fridge.get_current_fridge_count(900) + "\n" + fridge.connect("port 5000 ") + "\n" + coffeemachine.get_current_beans_count(900) + "\n" + coffeemachine.connect("port 5000 ")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
