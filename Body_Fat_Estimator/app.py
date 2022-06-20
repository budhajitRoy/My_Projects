from flask import Flask, request, render_template
import pickle

file = open('body_fat_estimator.pkl', 'rb')
clf = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def predict():

    if request.method == 'POST':
        my_dict = request.form

        # print(my_dict)

        # get values from the form
        density = float(my_dict['density'])
        abdomen = float(my_dict['abdomen'])
        chest = float(my_dict['chest'])
        weight = float(my_dict['weight'])
        hip = float(my_dict['hip'])

        # prepare input values
        inputs = [[density, weight, chest, abdomen, hip]]

        # get prediction
        # since predict returns a list
        prediction_results = clf.predict(inputs)[0].round(2)

        string = 'Percentage of Body Fat Estimated is : ' + str(prediction_results)+'%'
        return render_template('show.html', string=string)

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True) 
