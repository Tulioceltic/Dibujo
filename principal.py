from flask import Flask, render_template, redirect, request, url_for




app = Flask(__name__)

ordenb = [
    {'A1':True,'A2':False,'A3':True},
    {'B1':False,'B2':True,'B3':True},
    {'C1':True,'C2':True,'C3':True},
    {'D1':True,'D2':True,'D3':False},    
]

heib = len(ordenb)


@app.route('/', methods = ['POST','GET'])
def inicio():
    return render_template('inicio.html')

@app.route('/cu', methods = ['POST','GET'])
def ver_cuadrado():
    return render_template('cu.html',ordenf=ordenb, heif=heib)


@app.route('/trapecio', methods = ['POST','GET'])
def ver_trap():
    return render_template('trapecio.html',ordenf=ordenb,heif=heib)

if __name__ == '__main__':
    app.run(debug=True)