	
#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
import io
from werkzeug.utils import secure_filename
import cv2
import pandas as pd
import tensorflow
import numpy as np
import json
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from matplotlib import pyplot as plt
from PIL import Image
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
model = keras.models.load_model('scr/83_per_dignat.h5')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def modelfun(filename):
    #filename = 'Rugby.png'
    path = url_for('static', filename='uploads/' + filename)
    path = path[1:]
    print(type(path))
    img = image.load_img(path, target_size=(224,224))
    img = image.img_to_array(img, dtype=np.uint8)
    img=np.array(img)/255.0
    desc_data = pd.read_excel(r'D:\IBM_WEBSITE\scr\IBM_classes (2).xlsx')
    model_class_names = ['BLACK SWAN',
                             'Cats',
                             'PEACOCK',
                             'PINK ROBIN',
                             'Red Mullet',
                             'Shrimp',
                             'Trout',
                             'daisy',
                             'horse',
                             'rose',
                             'squirrel',
                             'sunflower']
    out_ind = model.predict(img[np.newaxis, ...])
    out_ind = np.argmax(out_ind[0], axis=-1)
    print(out_ind)
    pred_name = model_class_names[out_ind]
    print(pred_name)
    if pred_name in model_class_names:
        outp = desc_data[desc_data['COMMON NAME']==pred_name]
        out_dict = {'Name':outp['COMMON NAME'].values[0].casefold().capitalize(), 'Scientific_Name':outp['SCIENTIFIC NAME'].values[0].casefold().capitalize(), 'Class':outp['CLASS'].values[0].casefold().capitalize(),'Descriprion':outp['DESCRIPTION'].values[0]}
        return out_dict
    else:
        return "Not found"
   
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_img')
def up_img():
    return render_template('upload_img.html')



@app.route('/', methods=['POST','GET'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
   
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        
        model_out = modelfun(filename)
        
        model_out['filename'] = filename
        #model_out = json.dumps(model_out)
        
        return render_template('out.html',model_out=model_out)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run()

    ##file_bytes = numpy.fromstring(file, numpy.uint8)
    #img = Image.open(request.files['file'])
    ##img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    #img = np.array(img)
    #img = Image.fromarray(img, 'RGB')
    #
    #img.show()