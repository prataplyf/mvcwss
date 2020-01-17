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
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]



@app.route('/reactivate', methods=['POST','GET'])  # Re-activate Deleted Account From Delete Table
@ml.cross_origin()
def reactivate():
    if ml.request.method == 'POST':
        mail = ml.request.form.get('email')
        if mail in [temp['Email'] for temp in User_delete.find({}, {"Email":1} )]:
            for x in User_delete.find({"Email":mail},{"Name":1, "Email":1, "Password":1, "_id":1}):
                uid = x['_id']
                name = x['Name']
                email = x['Email']
                
                
                # Code for Password send on User Email
                def check():
                    characters = ml.string.ascii_letters  + ml.string.digits
                    password =  "".join(ml.choice(characters) for x in range(ml.randint(8,8)))
                    if ml.re.search("[0-9][a-z][A-Z]", password):
                        global pd
                        pd = password
                        configuration = ml.sib_api_v3_sdk.Configuration()
                        configuration.api_key['api-key'] = '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'
                        api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
                        send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                            to=[{"email": email ,"name": name}], 
                                            template_id=14, 
                                            params={"name": name, "email": email, "pwd": password}, 
                                            headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
                        try:
                            # Send a transactional email
                            api_response = api_instance.send_transac_email(send_smtp_email)
                            user.insert_one({"_id": uid, "Name": name, "Email":email, "Password":pd })
                            User_delete.remove({"Email":email},{"Name":1, "Email":1, "Password":1, "_id":1})  
                            ml.pprint(api_response)
                        except ml.ApiException as e:
                            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
                        # 
                    else:
                        return check()
                check()
                return ml.jsonify({"status":"Success","message":"Re-activate Account Successfully", 
                                "data":{
                                        "_id": uid, 
                                        "name": name, 
                                        "email":email, 
                                        "password": pd 
                                        }})
        else:
            return ml.jsonify({"status":"Error","message":"Enter Correct Email ID!"})
    
    msg = "Enter your Email ID for Register Yourself !"
    return ml.render_template('reactivate.html', message=msg)
