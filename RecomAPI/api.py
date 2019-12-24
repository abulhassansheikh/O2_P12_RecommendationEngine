import flask
from flask import request, jsonify
from tabulate import tabulate
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True

MasterRecomDoc=(pd.read_csv("//192.168.2.32/Group/Data Team/Recommender_System_Location/1_Reference_Files/MasterRecomDoc.csv", encoding='utf-8'))

@app.route('/all', methods=['GET'])
def home():
    
    resultshtml = tabulate(MasterRecomDoc, tablefmt='html')
    return resultshtml

@app.route('/Y3M', methods=['GET'])
def api_Y3M():
    
    
    if 'year' in request.args:
        year = request.args['year']
    else:
        year =  "All"  
        
    if 'make' in request.args:
        make = request.args['make']
    else:
        make =  "All"  
    
    if 'model' in request.args:
        model = request.args['model']
    else:
        model =  "All"  
        
    if 'month' in request.args:
        month = request.args['month']
    else:
        month =  "All" 

    # Create an empty list for our results
    results = (MasterRecomDoc[(MasterRecomDoc["Year"] == year) & 
                              (MasterRecomDoc["Make"] == make) & 
                              (MasterRecomDoc["Model"] == model) & 
                              (MasterRecomDoc["OD_MonthNum"] == month) 
                             ])[["Sku_0", "Sku_1"]]
    
    results = (results["Sku_0"].dropna().unique().tolist() + 
                results["Sku_1"].dropna().unique().tolist())


    resultshtml = tabulate(results, tablefmt='html')
    return resultshtml

app.run()