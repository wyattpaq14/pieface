from flask import render_template, request, url_for, redirect, jsonify
from app import app
from sqlalchemy import create_engine
from app.forms import ImageSetForm
from app import hdmi_controller
from app import database_handler
import subprocess
from database_handler import db_functions, MediaSets, sessionmaker

hdmi_controller = hdmi_controller.hdmi_controller()
app.secret_key = 's3cr3t'
db = db_functions()


@app.route('/hdmi_control')
def potato():
    return render_template('hdmi_control.html',
                           title='PieFace',
                           version=2.0,
                           style="/static/css/bootstrap.css")


@app.route('/medset/<medid>/<action>')
def shit(medid, action):
    
    if (action == "edit"):
        return render_template('edit.html',
                           title='PieFace',
                           version=2.0,
                           selectedMediaSet=db.get_media_set_by_id(medid),
                           style="/static/css/bootstrap.css")
    elif (action == "delete"):
        return render_template('delete.html',
                           title='PieFace',
                           version=2.0,
                           mediasetId=medid,
                           style="/static/css/bootstrap.css")
        



    
    

@app.route('/', methods=['POST', 'GET'])
def index():
    activeSet = "Not Here"
    version = '0.1'
    current_image = "NONE"
    selectedSet = "No Set Selected Yet"
    imageset_form = ImageSetForm()

    # imgchange_status = hdmi_controller.display_output_status

    # Coll
    if request.method == 'POST':

        test = db.get_media_set_by_id(selectedSet)
        imageset_form = ImageSetForm(obj=test)
    
        imageset_form.populate_obj(test)


        



        if 'imageSet' in request.form:
            print("i clicked on form 1 submit!")
        elif 'output7' in request.form:
            print("i clicked on form2 submit!")

        else:
            print("alex is a peice of shit")

        if imageset_form.validate():
            print("activate button was pressed : {value}".format(value=imageset_form.activate.data))
            print("select button was pressed : {value}".format(value=imageset_form.select.data))

        if imageset_form.activate.data == True:
            activeSet = request.form['imageSet']

        elif imageset_form.select.data == True:
            selectedSet = request.form['imageSet']

    return render_template('index.html',
                           imageset_form=imageset_form,
                           title='PieFace',
                           active=activeSet.upper(),
                           version=2.0,
                           selected=selectedSet,
                           db= db,
                           hdmichange_status="hdmi_controller.get_hdmi_status",
                           imgchange_status="hdmi_controller.display_output_status()",
                           style="/static/css/bootstrap.css")


def get_output_input():
    if request.form['output1']:
        response = "out1" + '-' + request.form['output1']

    elif request.form['output2']:
        response = "out2" + '-' + request.form['output2']

    elif request.form['output3']:
        response = "out3" + '-' + request.form['output3']

    elif request.form['output4']:
        response = "out4" + '-' + request.form['output4']

    elif request.form['output5']:
        response = "out5" + '-' + request.form['output5']

    elif request.form['output6']:
        response = "out6" + '-' + request.form['output6']

    elif request.form['output7']:
        response = "out7" + '-' + request.form['output7']

    elif request.form['output8']:
        response = "out8" + '-' + request.form['output8']
    else:
        response = "Nothing here good sir"

    return response
