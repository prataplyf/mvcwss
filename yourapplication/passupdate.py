from yourapplication import module as ml
from yourapplication import app

myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

# user password update
@app.route('/userpassupdate', methods=['POST', 'GET'])
@ml.cross_origin()
def passupdate():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            userNewPass = data['newPass']
            userConfirmPass = data['confPass']
            userID = data['userID']
        else:
            userNewPass = ml.request.values['newPass']
            userConfirmPass = ml.request.values['confPass']
            userID = ml.request.values['userID']
        
        if userNewPass == userConfirmPass:
            user.update_one({'_id':userID},{'$set':{'Password':userNewPass}})
            return ml.jsonify({'message':'password updated successfully', 'status':'success','data':{'userNewPass':userConfirmPass, 'userID':userID}})
        else:
            return ml.jsonify({'message':"Password didn't match", 'status':'failed', 'data':{'userNewPass':userConfirmPass, 'userID':userID}})
        
    return ml.render_template('passupdate.html')
