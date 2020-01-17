from flask import Flask
app = Flask(__name__)


import yourapplication.api
import yourapplication.booking
import yourapplication.delete
import yourapplication.getbooking
import yourapplication.login
import yourapplication.passupdate
import yourapplication.prof
import yourapplication.reactivate
import yourapplication.register


if __name__ == "__main__":
    app.run(debug=True)



