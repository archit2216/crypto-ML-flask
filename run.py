from flask import Flask,render_template,request,jsonify
from datetime import date,timedelta
import pickle

with open('ARIMA_modelBTC1.pkl', 'rb') as file:
    modelBTC=pickle.load(file)
with open('ARIMA_modelETH.pkl','rb') as file:
    modelETH=pickle.load(file)
with open('ARIMA_modelDOGE.pkl','rb') as file:
    modelDOGE=pickle.load(file)
with open('ARIMA_modelXRP.pkl','rb') as file:
    modelXRP=pickle.load(file)
with open('ARIMA_modelSOL.pkl','rb') as file:
    modelSOL=pickle.load(file)
with open('ARIMA_modelADA.pkl','rb') as file:
    modelADA=pickle.load(file)
with open('ARIMA_modelXLM.pkl','rb') as file:
    modelXLM=pickle.load(file)
with open('ARIMA_modelDOT.pkl','rb') as file:
    modelDOT=pickle.load(file)
with open('ARIMA_modelLINK.pkl','rb') as file:
    modelLINK=pickle.load(file)

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    pred=[0]
    if request.method=='POST':
        user_input=request.form
        Coin=str(user_input.get('Coin'))
        start_date=date.today()-timedelta(1)
        end_date=date.today()
        if Coin=='BTC': 
            pred=modelBTC.predict(start=start_date,end=end_date)
        elif Coin=='XRP':
            pred=modelXRP.predict(start=start_date,end=end_date)
        elif Coin=='ETH':
            pred=modelETH.predict(start=start_date,end=end_date)
        elif Coin=='DOGE':
            pred=modelDOGE.predict(start=start_date,end=end_date)
        elif Coin=='SOL':
            pred=modelSOL.predict(start=start_date,end=end_date)
        elif Coin=='XLM':
            pred=modelXLM.predict(start=start_date,end=end_date)
        elif Coin=='DOT':
            pred=modelDOT.predict(start=start_date,end=end_date)
        elif Coin=='ADA':
            pred=modelADA.predict(start=start_date,end=end_date)
        elif Coin=='LINK':
            pred=modelLINK.predict(start=start_date,end=end_date)
        else:
            pred=modelETH.predict(start=start_date,end=end_date)
        return jsonify(pred[0])
    # return render_template('index.html',prediction=pred[0])


if __name__=='__main__':
    app.run(port=5000,debug=True)
