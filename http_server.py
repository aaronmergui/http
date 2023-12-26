from flask import Flask,request,render_template_string
app=Flask(__name__)



@app.route('/sum')
def addition():
    a=request.args
    a=request.args.get('a', default=0,type=float)
    b=request.args.get('b', default=0,type=float)
    c=a+b
    message = f"The result of {a}+{b} is: {c}"
    return '''<h2>{}</h2>'''.format(message)


if __name__ == '__main__':
    app.run(debug=True)