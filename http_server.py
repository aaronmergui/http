from flask import Flask,request,render_template_string
app=Flask(__name__)



@app.route('/sum')
def addition():
    try:
        a=float(request.args.get('a'))
        b=float(request.args.get('b'))
        c = a + b
        message = f"The result of {a}+{b} is: {c}"
        return '''<h2>{}</h2>'''.format(message)
    except:
        return '''<h2>At least one of the parameters is not a number </h2>'''

@app.route('/average')
def average():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = a + b
        message = f"The average is: {c/2}"
        return '''<h2>{}</h2>'''.format(message)
    except:
        return '''<h2>At least one of the parameters is not a number </h2>'''


if __name__ == '__main__':
    app.run(debug=True)