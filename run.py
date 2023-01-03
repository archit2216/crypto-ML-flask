from flask import Flask,render_template,request,jsonify
import pickle

modelBTC=pickle.load(open('lr_modelBTC.pkl','rb'))
modelXRP=pickle.load(open('lr_modelXRP.pkl','rb'))
modelETH=pickle.load(open('lr_modelETH.pkl','rb'))
modelDOGE=pickle.load(open('lr_modelDOGE.pkl','rb'))
modelSOL=pickle.load(open('lr_modelSOL.pkl','rb'))
modelXLM=pickle.load(open('lr_modelXLM.pkl','rb'))
modelDOT=pickle.load(open('lr_modelDOT.pkl','rb'))
modelADA=pickle.load(open('lr_modelADA.pkl','rb'))
modelLINK=pickle.load(open('lr_modelLINK.pkl','rb'))
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    pred=[0]
    if request.method=='POST':
        user_input=request.form
        Coin=str(user_input.get('Coin'))
        openVal=int(user_input.get('Open'))
        high=int(user_input.get('High'))
        low=int(user_input.get('Low'))
        vol=int(user_input.get('Volume'))
        if Coin=='BTC': 
            pred=modelBTC.predict([[openVal,high,low,vol]])
        elif Coin=='XRP':
            pred=modelXRP.predict([[openVal,high,low,vol]])
        elif Coin=='ETH':
            pred=modelETH.predict([[openVal,high,low,vol]])
        elif Coin=='DOGE':
            pred=modelDOGE.predict([[openVal,high,low,vol]])
        elif Coin=='SOL':
            pred=modelSOL.predict([[openVal,high,low,vol]])
        elif Coin=='XLM':
            pred=modelXLM.predict([[openVal,high,low,vol]])
        elif Coin=='DOT':
            pred=modelDOT.predict([[openVal,high,low,vol]])
        elif Coin=='ADA':
            pred=modelADA.predict([[openVal,high,low,vol]])
        elif Coin=='LINK':
            pred=modelLINK.predict([[openVal,high,low,vol]])
        else:
            pred=modelBTC.predict([[openVal,high,low,vol]])
        return jsonify(pred[0])
    # return render_template('index.html',prediction=pred[0])


if __name__=='__main__':
    app.run(port=5000,debug=True)
