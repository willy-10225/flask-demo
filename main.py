from flask import Flask,render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/sum')
def  get_sum2():
    return render_template('./index.html')

@app.route('/sum/x=<x>&y=<y>')
def  get_sum(x,y):
    try:
        total=str(eval(x)+eval(y))
    except Exception as e:
        print(e)
        total="輸入錯誤"

    result={
        'x':x,
        'y':y,
        'total':total
    }

    return render_template('./index.html',result=result)

@app.route('/stock')
def stock():
    stocks=[
            {'分類': '日經指數', '指數': '22,920.30'},
            {'分類': '韓國綜合', '指數': '2,304.59'},
            {'分類': '香港恆生', '指數': '25,083.71'},
            {'分類': '上海綜合', '指數': '3,380.68'}
        ]
    return render_template('./stock.html',stocks=stocks)



@app.route('/today')
@app.route('/today/<name>')
def getTime(name='GUEST'):
    today= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'<h1>Hello {name},Welcome!</h1><br>{today}'



if __name__ =='__main__':
    getTime('willy')
    app.run(debug=True)
