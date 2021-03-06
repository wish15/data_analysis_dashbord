import os
from flask import Flask, flash, request, redirect, url_for, session,render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
from keras.models import load_model
from Text.Text import Text
from Audio.Audio import Diariazation
from Video.test import Video_Analysis
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
directory = os.getcwd()



'''
UPLOAD_FOLDER = './Video'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','.mp4'])
model=load_model('./Video/saved_model.h5')
'''
app = Flask(__name__)
CORS(app)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/',methods=['GET'])
def check():
    # text_class=Text()
    # a,b,c=list(text_class.topic_modelling(file_path='C:\\Users\\vishu\\OneDrive\\Desktop\\Vishal\\final year project\\Text-analysis~\\Final_project_Server-main\\xyz.pdf'))
    return "Listening on 5000"
    #print(summary)
    #a=[str(i) for i in a]
    #a=" ".join(a)
    #return a

@app.route('/<filename>',methods=['GET'])
@cross_origin()
def lol(filename):
    print(filename)
    return render_template(str(filename))




@app.route('/uploadText', methods=['POST','GET'])
@cross_origin()
def fileUpload():
    UPLOAD_FOLDER="./Text"
    target=os.path.join(UPLOAD_FOLDER,'TextD')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file_path = None
    url=None
    text=None
    if(request.files):
        file = request.files['file']
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        print(destination,filename)
        file.save(destination)
        file_path=destination
    elif(request.form["url"]):
        url=request.form["url"]
        print("lol",url)
    else:
        text=request.form["text"]

    text_class=Text()
    text_class.file_path_ext(file_path, url,text)
    a,b,c,d=list(text_class.topic_modelling())
    summary=text_class.extractive_summary()
    readability=text_class.readability_analysis()
    
    response={'summary':summary,'readability':readability,'topic_modelling':[a,b,c,d]}

    # session['uploadFilePath']=destination
    # response={"test":"heyy","response":res,"reconstruction":reconstruction_array}
    
    #response={'summary':'summary','readability':'readability','topic_modelling':[['a','b','c'],['a','b','c'],['a','b','c']]}
    print(response)
    return response

@app.route('/uploadVideo', methods=['POST','GET'])
@cross_origin()
def fileVideoUpload():

    UPLOAD_FOLDER = directory+"\\Video"
    target=os.path.join(UPLOAD_FOLDER,'videosD')
    demo= os.getcwd()
    print(demo)
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    print(destination,filename)
    file.save(destination)
    for i in range(8000000):
        pass
    model=load_model(directory+"\\Video\\saved_model.h5")
    res,reconstruction_array=Video_Analysis(filename,model,destination)


    print("response",res)
    print("on server")
    session['uploadFilePath']=destination
    response={"test":"heyy","response":res,"reconstruction":reconstruction_array}
    
    
    return response



@app.route('/uploadAudio', methods=['POST','GET'])
@cross_origin()
def AudioFileUpload():
    UPLOAD_FOLDER="./Audio"
    target=os.path.join(UPLOAD_FOLDER,'AudioD')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file_path = None
    url=None
    text=None
    if(request.files):
        file = request.files['file']
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        print(destination,filename)
        file.save(destination)
        file_path=destination
        ans=Diariazation(file_path,filename)
        return ans
    else :
        return {"msg":"NO file uploadede"}



if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,use_reloader=False)

# CORS(app, expose_headers='Authorization')
