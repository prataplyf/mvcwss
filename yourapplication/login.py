from yourapplication import module as ml
from yourapplication import app

myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

app.config['SECRET_KEY'] = "wharfstreetstrategies"

@app.route('/login', methods=['POST','GET'])
@ml.cross_origin()
def login():
    if ml.request.method == 'POST':
        auth = ml.request.authorization
        mail = ml.request.form.get('lmail')
        enter_pass = ml.request.form.get('lpassword')
        
        # print(mail)
        for x in user.find({"Email":mail},{"Name":1, "Email":1, "Password":1, "_id":1}):
            pwd = x['Password']
            uid = x['_id']
            uname = x['Name']
            umail = x['Email']
            if pwd == enter_pass:
                token = ml.jwt.encode({'user':uname, 'exp':ml.datetime.datetime.utcnow() + ml.datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                # return jsonify({'Token':token.decode('UTF-8'), 'Message':"Login Success", "User ID":uid, "Name": uname, "Email":umail})
                msg = "Login Successful!"
                return ml.jsonify({ "data":{"name": uname, 
                                 "userid": uid, 
                                 "email": umail, 
                                 "token":token.decode('UTF-8')}, 
                                 "message": msg,
                                 "status":"Success"
                                })
                #return "Login Success"
            else:
                return ml.make_response('Wrong email ID or Password!', 
                                        401, {'WWW-Authenticate' : 'Basic realme="Login Required"'})

        

    return ml.render_template('login.html')
