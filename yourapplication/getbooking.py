from yourapplication import module as ml
from yourapplication import app

myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

@app.route('/getbooking', methods=['GET'])
@ml.cross_origin()
def getbooking():
    if ml.request.method == 'GET':
        result = []
        for i in range(0,timeslotBooking.find({}).count()):
            for x in timeslotBooking.find({},{"_id":0,"Name":1, "Date":1, "Country":1, "State":1}):
                result.append({"name":x['Name'], "date":x['Date'], "country":x['Country'], "state":x['State']})            
            return ml.jsonify({"message":"Booking Information", "status":"success", "Result":result})
    else:
        return ml.jsonify({"message":"No Booking Available"})
