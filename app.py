from flask import Flask, request, render_template

app=Flask(__name__)

import pickle
import numpy as np
model = pickle.load(open('agri.pkl', 'rb'))

@app.route('/input', methods=['GET','POST'])
def input():
    msg=""
    if request.method=="POST":
        details=request.form
        count = float(details['count'])
        crop = int(details['crop'])
        soil = int(details['soil'])
        doses = int(details['doses'])
        quit = int(details['quit'])
        season = int(details['season'])
    
        predict=model.predict([[count, crop, soil, doses, quit, season]])
        if predict[0]==0:
            msg="Alive"

        elif predict[0]==1:
            msg="Damaged due to other causes"
        else:
            msg="Damaged due to pesticide"
    return render_template('output.html',msg=msg)





    



@app.route('/')
def main():
    return render_template('Front.html')

if __name__ == '__main__':
    app.run(debug=True)