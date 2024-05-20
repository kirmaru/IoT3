from flask import Flask, render_template, request
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
    response = lights.connect(request)
    return json.dumps(response)


@app.route('/climate')
def ChangeTemp():
    return json.dumps(climate.connect("climate"))

@app.route('/doors')
def connect_Doors():
    doors.connect(request)
    return json.dumps(doors.connect("doors"))
@app.route('/alarm')
def connect_Alarm():
    return json.dumps(alarm.connect("alarm"))

@app.route('/fire')
def connect_Fire():
    return json.dumps(fire.connect("fire"))
@app.route('/intruder')
def connect_Intruder():
    return json.dump({intruder.connect("intruder")})

@app.route('/get_chart', methods=['GET'])
def get_chart():
    data = lights.lum_chart()
    return json.dumps(data)

@app.route('/')
def main():

    return render_template('emulators.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
