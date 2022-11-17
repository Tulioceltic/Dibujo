from flask import Flask, render_template, redirect, request, url_for




app = Flask(__name__)

ordenb = [
    ['A1','A2','B3'],
    ['B1','B2','B3'],
    ['C1','C2','C3'],
    ['D1','D2','D3'],    
]

heib = len(ordenb)

habilitadob = [
    [True,False,True],
    ['B1','B2','B3'],
    ['C1','C2','C3'],
    ['D1','D2','D3'],    
]


@app.route('/', methods = ['POST','GET'])
def inicio():
    return render_template('inicio.html')

@app.route('/cu', methods = ['POST','GET'])
def ver_cuadrado():
    return render_template('cu.html',ordenf=ordenb, habilitadof=habilitadob, heif=heib)


@app.route('/trapecio', methods = ['POST','GET'])
def ver_circulo():
    return render_template('trapecio.html',ordenf=ordenb)

if __name__ == '__main__':
    app.run(debug=True)