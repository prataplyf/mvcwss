from yourapplication import module as ml
from yourapplication import app




global password
password = ''
global pd
pd = ''

myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
Profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

# get user Profile            
@app.route('/userprofile', methods=['POST','GET'])
@ml.cross_origin()
def getuserprofile():
    if ml.request.method == 'POST':
        if ml.request.is_json:
            data = ml.request.get_json()
            userid = data['userID']
        else:
            userid = ml.request.values['userID']
        
        for x in Profile.find({'_id':userid},{'_id':1,'Email':1, 'Name':1, 'Contact_Number':1,'Address':1, 
                                              'City':1, 'State':1,'Country':1, 'ZIP_Code':1}):
            
            return ml.jsonify({'message':'User Data Get Successfully', 
                            'status':'success', 
                            'userProfile':{
                            'userID':x['_id'],'email':x['Email'], 'name':x['Name'], 
                                        'contactNumber':x['Contact_Number'],
                            'address':x['Address'], 'city':x['City'], 'state':x['State'],
                            'country':x['Country'], 'postal_code':x['ZIP_Code']
                            }})
        else:
            return ml.jsonify({'message':'No such UserID found in Profile Data, Check it Again!', 'status':'success'})
            
    return ml.render_template('getuserprofile.html')
        
