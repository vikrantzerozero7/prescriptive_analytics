from flask import Flask, render_template
from github import Github
from github import InputGitTreeElement
app = Flask(__name__)

import pycaret
from pycaret.classification import *
#import pickle
import numpy as np
import pandas as pd
#import pickle

@app.route('/')
def home():	
    saved_final_rf = load_model('model')
    g = Github("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")

    user = g.get_user()

    repository = user.get_repo('pres')

    file_content = repository.get_contents('jun23.csv')

    bytes_data=file_content.decoded_content

    s=str(bytes_data,'utf-8')

    file = open("data.txt","w")

    file.write(s)

    df = pd.read_csv('data.txt')
    df.rename(columns = {'Customer Name':"Party_Name","Plant":"Warehouse","Target Quantity":"Net Weight"},inplace = True)
    name = [x for x in df.Party_Name]
    return render_template('index2.html', name=name)
    

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
    
'''Total_rejected_WD=1&Nr_days_without_activity=2

from flask import Flask, render_template, json
app = Flask(__name__)

@app.route('/')
def index():    
    name = ['Red', 'Blue', 'Orange', 'Yellow', 'Green']
    return render_template('index2.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
'''
