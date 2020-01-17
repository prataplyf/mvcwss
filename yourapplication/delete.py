from yourapplication import module as ml
from yourapplication import app


myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

@app.route('/delete', methods=['POST', 'GET'])  # Delete an Account of Existing Users
@ml.cross_origin()
def delete():
    if ml.request.method == 'POST':
        did = ml.request.form.get('cid')  # did -> (delete id)
        for x in user.find({"_id":did},{"Name":1, "Email":1, "Password":1, "_id":1}):
            uid = x['_id']
            name = x['Name']
            email = x['Email']
            password = x['Password']
            User_delete.insert_one({"_id": uid, "Name": name, "Email":email, "Password":password })
            user.remove({"_id":did},{"Name":1, "Email":1, "Password":1, "_id":1})
            return ml.jsonify({"id":uid, "message": "Data Delete!", "status":"Success"})

            # else:
            #     return jsonify({'Message': "IDs Not Found!"})
        # elif did in User_delete.find({"_id":did}, {"_id":1}):
        #     return jsonify({"Message":"User Already Deleted"})
        else:
            return ml.jsonify({"message":"This ID doesn't exist!","status":"Error"})
    
    return ml.render_template('delete.html')
