from yourapplication import app
from yourapplication import module as ml

@app.route('/')  # page that help to go on a registration page
def api():
    return ml.render_template('api.html')  