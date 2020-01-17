from yourapplication import module as ml
from yourapplication import app

global password
password = ''
global pd
pd = ''

myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
User_delete = mydb["Delete"]

# @app.route('/register',methods = ['POST', 'GET'])
@app.route("/register", methods=['POST','GET'])
@ml.cross_origin()
def register():
    if ml.request.method == 'POST':
        uemail = ml.request.form.get('email')
        uname = ml.request.form.get('name')
        count = 0
        if uemail in [temp['Email'] for temp in user.find({}, {"Email":1} )]:
            return ml.jsonify({"status":"Already used","message":"This Email ID Already Registered Us!"})
        elif uemail in [temp['Email'] for temp in User_delete.find({}, {"Email":1} )]:
            count += 1
            msg1 = "You are already registered with us and you Deleted your account Previously!"
            msg2 = "Want to Re-activate your account"
            return ml.jsonify({"status":"Already used",'message':"Already Exist, Reactivate Account!"})
            # return jsonify({"Message": })
        else:
            user_count = user.find({}).count()
            delete_count = User_delete.find({}).count()
            result = user_count + delete_count + 1
            fid = "R-WSS"  # auto generated user id with R-WSS (i.e: R-WSS0000001)
            uid = fid + "%07d"%result
            def check():
                global pd, password
                characters = ml.string.ascii_letters  + ml.string.digits
                password =  "".join(ml.choice(characters) for x in range(ml.randint(8,8)))
                if ml.re.search("[0-9][a-z][A-Z]", password):
                    pd = password
                    configuration = ml.sib_api_v3_sdk.Configuration()
                    configuration.api_key['api-key'] = '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'
                    api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
                    send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                        to=[{"email": uemail ,"name": uname}], 
                                        template_id=13, 
                                        params={"name": uname, "email": uemail, "pwd": pd}, 
                                        headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
                    try:
                        # Send a transactional email
                        api_response = api_instance.send_transac_email(send_smtp_email)
                        user.insert_one({"_id": uid, "Name": uname, "Email":uemail, "Password":pd })   
                        ml.pprint(api_response)
                    except ml.ApiException as e:
                        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
                    # 
                else:
                    return check()
            check()
            return ml.jsonify({"status":"Success","message":"Register Successfully", "data":{"_id": uid, "name": uname, "email":uemail, "password": password }})
                
    
    return ml.render_template('register.html')
