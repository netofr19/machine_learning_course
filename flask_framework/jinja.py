from flask import Flask, render_template, request, redirect, url_for

# Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} condition, for loops
{#...#} this is for comments
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html', results=res)

# Variable rule
@app.route('/successres/<int:score>')
def successres(score):
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"

    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)

# if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html', results=score)

# Variable rule
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html', results=score)

@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['data_science'])

        total_score = (science + maths + c + data_science)/4

    return redirect(url_for('successres', score=total_score))



if __name__ == "__main__":
    app.run(debug=True)