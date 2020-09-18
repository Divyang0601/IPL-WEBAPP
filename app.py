from flask import Flask,render_template,request
import numpy as np
import pickle
import os

#############################################################

filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

##############################################################

app = Flask(__name__)


@app.route('/')
def predictor_view():
    return render_template('Predictor.html')

@app.route('/form')
def form_view():
    return render_template('form.html')

@app.route('/feedback')
def feedback_view():
    return render_template('feedback.html')

@app.route('/thankyou')
def thank_you():
    return render_template('thank_you.html')


@app.route('/result_page',methods=['POST'])
def result_page():
    temp_value = list()
    if request.method == 'POST':

        batting_team = request.form['batting team']
        if batting_team == 'Chennai Super Kings':
            temp_value = temp_value + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_value = temp_value + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_value = temp_value + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_value = temp_value + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_value = temp_value + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_value = temp_value + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_value = temp_value + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_value = temp_value + [0,0,0,0,0,0,0,1]


        bowling_team = request.form['bowling team']
        if bowling_team == 'Chennai Super Kings':
            temp_value = temp_value + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_value = temp_value + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_value = temp_value + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_value = temp_value + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_value = temp_value + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_value = temp_value + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_value = temp_value + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_value = temp_value + [0,0,0,0,0,0,0,1]

        match_venue = request.form['Venue']
        if match_venue == 'venue_Eden Gardens':
            temp_value = temp_value + [1,0,0,0,0,0,0,0]
        elif match_venue == 'venue_Feroz Shah Kotla':
            temp_value = temp_value + [0,1,0,0,0,0,0,0]
        elif match_venue == 'venue_M Chinnaswamy Stadium':
            temp_value = temp_value + [0,0,1,0,0,0,0,0]
        elif match_venue == 'venue_MA Chidambaram Stadium, Chepauk':
            temp_value = temp_value + [0,0,0,1,0,0,0,0]
        elif match_venue == 'venue_Punjab Cricket Association Stadium, Mohali':
            temp_value = temp_value + [0,0,0,0,1,0,0,0]
        elif match_venue == 'venue_Rajiv Gandhi International Stadium, Uppal':
            temp_value = temp_value + [0,0,0,0,0,1,0,0]
        elif match_venue == 'venue_Sawai Mansingh Stadium':
            temp_value = temp_value + [0,0,0,0,0,0,1,0]
        elif match_venue == 'venue_Wankhede Stadium">Wankhade Stadium, Mumbai':
            temp_value = temp_value + [0,0,0,0,0,0,0,1]


        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['prev runs'])
        wickets_in_prev_5 = int(request.form['prev wickets'])

        temp_value = temp_value + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

        data = np.array([temp_value])
        my_prediction = int(regressor.predict(data))


    return render_template('results.html', lower_limit = my_prediction-7, upper_limit = my_prediction+8)

##########################################################

@app.errorhandler(404)
def wrong_port(e):
    return render_template('wrong_port.html'), 404

##########################################################

if __name__ == "__main__":
    app.run()

############################################################
