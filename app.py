from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    consent = request.cookies.get('consent')
    return render_template("home.html", consent=consent)

@app.route('/privacy_policy')
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route('/cookies')
def cookies():
    return render_template("cookies.html")

@app.route('/accept_cookies')
def accept_cookies():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('consent', 'accepted', max_age=3600, httponly=True, secure=True)
    return response

@app.route('/reject_cookies')
def reject_cookies():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('consent')
    return response

@app.route('/get_cookie')
def get_cookie():
    user = request.cookies.get('user')
    if user:
        return f"Hello, {user}"
    return "The cookie is not available"

if __name__ == "__main__":
    app.run(debug=True)

