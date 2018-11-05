import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


#Woked with Steve, Andrew, Lucas, Annastasia

#data = AnalysisData()
#data.parseFile("candy-data.csv")

class AnalysisData:


    def __init__(self):
        self.dataset = []
        self.variables = []
    def parseFile (self, filename):
        self.dataset = pd.read_csv(filename)
        for column in self.dataset.columns.values:
            if column != "competitorname": 
                self.variables.append(column)  
                
class LinearAnalysis:
    def __init__ (self, _targetY):
        self.targetY = _targetY
        self.bestX = ""
        
    def runSimpleAnalysis(self, data):
        best_r2 = -1
        best_var = ""
        for column in data.variables:
            if column != self.targetY:
                inde_variable = data.dataset[column].values
                inde_variable = inde_variable.reshape(len(inde_variable),1)
                regression = LinearRegression()
                regression.fit(inde_variable, data.dataset[self.targetY])
                predict = regression.predict(inde_variable)
                r_score = r2_score(data.dataset[self.targetY],predict)
            if r_score > best_r2:
                best_r2 = r_score
                best_variable = column
        self.bestX = best_var
        print(best_variable, best_r2)

data = AnalysisData()
data.parseFile("candy-data.csv")

final_analysis = LinearAnalysis('sugarpercent')
final_analysis = LinearAnalysis('pricepercent')
final_analysis = LinearAnalysis('winpercent')
final_analysis.runSimpleAnalysis(data)
final_analysis.runSimpleAnalysis(data)
final_analysis.runSimpleAnalysis(data)


        

    