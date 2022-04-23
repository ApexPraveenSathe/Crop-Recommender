from flask import Flask, render_template, request, Markup
from flask import request
import numpy as np
import pandas as pd
import pickle
import sklearn



# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)
model = pickle.load(open('RFClassifier.pkl','rb'))

# render home page


@ app.route('/')
def home():
    title = 'CROP-RECOMMENDER-HOME'
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop.html', title=title)

# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page


@ app.route('/crop-predict',methods = ['POST'])
def crop_prediction():
    temp_array = list()
    title = 'Crop Recommendation'
    if request.method == 'POST':

        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        temp = float(request.form['temperature'])
        hum = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall  = float(request.form['rainfall'])


        temp_array = temp_array + [N, P, K, temp,hum, ph, rainfall] 
        data = np.array([temp_array])
        my_prediction = model.predict(data)
        final_prediction = my_prediction[0]
    
	    #prediction=final_prediction 

        return render_template('crop-result.html',prediction = final_prediction, title=title)
        

    
    
# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
