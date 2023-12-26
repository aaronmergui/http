from flask import Flask,request,render_template_string
app=Flask(__name__)



@app.route('/sum')
def addition():
    try:
        numbers=list(map(float,request.args.values()))
        s=lambda num:sum(num)
        message = f"The result of sum is: {s(numbers)}"
        return '''<h2>{}</h2>'''.format(message)
    except:
        return '''<h2>http error code bad request </h2>'''

@app.route('/average')
def average():
    try:
        numbers = list(map(float, request.args.values()))
        av=lambda num:sum(num)/len(num) if len(num)!=0 else 0
        return '''<h2>The average is: {} </h2>'''.format(av(numbers))


    except:
        return '''<h2>http error code bad request </h2>'''
@app.errorhandler(404)
def page_not_found(error):
    return "this page doesn't exist",404



if __name__ == '__main__':
    app.run(debug=True)