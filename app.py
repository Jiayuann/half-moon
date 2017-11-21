from flask import Flask, redirect, url_for, request, render_template, make_response, flash

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['user_name'] == 'admin' and request.form['user_password'] == 'admin':
            flash('You are successfully logged in')
            return redirect(url_for('login_message'))
        else:
            error = 'Invalid username or password'
    return render_template('index.html', error=error)


@app.route('/loginMessage')
def login_message():
    return render_template('loginMessage.html')

@app.route('/scoreMessage/<name>/<int:score>')
def score_message(name, score):
    scores = {'Phy':60, 'Math':70, 'CHN': 110}
    return render_template('scoreMessage.html',
                           name=name,
                           mark=score,
                           marks=scores)


@app.route('/getInfo',methods=['POST','GET'])
def get_info():
    if request.method == 'POST':
        user = request.form['user_name']
        score = request.form['user_score']
        return redirect(url_for('score_message', name=user, score=score))
    else:
        user = request.args.get('user_name') + 'GET'
        score = request.args.get('user_score')
        response = make_response(redirect(url_for('get_cookie')))
        response.set_cookie('user_name', user)
        response.set_cookie('user_score', score)
        return response


@app.route('/getCookie')
def get_cookie():
    name=request.cookies.get('user_name')
    return 'welcome' + name


if __name__ == '__main__':
    app.debug = True
    app.run()
