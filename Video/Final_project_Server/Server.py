import os
from flask import Flask, flash, request, redirect, url_for, session,render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
from keras.models import load_model
from Video.test import Video_Analysis



logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')



UPLOAD_FOLDER = './Video'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','.mkv','.mp4'])
model=load_model('Video/saved_model.h5')

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/',methods=['GET'])
def check():
    return "Listening on 5000"




@app.route('/uploader', methods=['POST','GET'])
@cross_origin()
def fileUpload():
    
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
    model=load_model("Video\saved_model.h5")
    res,reconstruction_array=Video_Analysis(filename,model,destination)


    print("response",res)
    print("on server")
    session['uploadFilePath']=destination
    response={"test":"heyy","response":res,"reconstruction":reconstruction_array}
    
    
    return response






 




if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,use_reloader=False)

# CORS(app, expose_headers='Authorization')