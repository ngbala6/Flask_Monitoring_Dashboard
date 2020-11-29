from flask import Flask
import flask_monitoringdashboard as dashboard


app = Flask(__name__)

dashboard.config.init_from(file='config.cfg')

dashboard.bind(app)


@app.route('/bala',methods = ['GET','POST'])
def bala():
    return "Hello Maintenance"

@app.route('/sri', methods = ['GET','POST'])
def sri():
    return "Hello Maintenance 2"


if __name__ == '__main__':
    app.run(host = '127.0.0.1',threaded = True, port = 5000)