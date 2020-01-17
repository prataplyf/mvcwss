from yourapplication import module as ml
from yourapplication import app



myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.WSS
user = mydb["Users"]
course = mydb["Course"]
profile = mydb["Profile"]
User_delete = mydb["Delete"]
timeslotBooking = mydb["sessionBooking"]

@app.route('/booking', methods=['POST', 'GET'])
@ml.cross_origin()
def booking():
    if ml.request.method == 'POST':
        uname = ml.request.form.get('name')
        email = ml.request.form.get('email')
        contact = ml.request.form.get('contact')
        skypeID = ml.request.form.get('skypeID')
        date = ml.request.form.get('date')
        #timeslot = request.form.get('timeslot')
        country = ml.request.form.get('country')
        state = ml.request.form.get('state')
        office_mailid = 'info@wharfstreetstrategies.com'
        li = [office_mailid, email]
        t_id = [16, 15]
        result = timeslotBooking.find({}).count() + 1
        uid = "B-WSS" + "%07d"%result
        name = uname.split()[0]
        configuration = ml.sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = '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'
        api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
        for i in range(0,2,1):
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                to=[{"email": li[i] }], 
                                template_id= t_id[i], 
                                params={"name": name, "date":date, "country":country, "skypeID":skypeID, "state":state, "email":email, "contact":contact}, 
                                headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                ml.pprint(api_response)
                if li[i] == email:
                    timeslotBooking.insert_one({"_id":uid,"Name":name, "Email":email, "Contact":contact, "SkypeID":skypeID,"Date":date, "Country":country, "State":state})
                  
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        
        return ml.jsonify({"name":name, "email":email, "contact":contact, "skypeid":skypeID,"date":date, "country":country, "state":state})
    

    return ml.render_template('booking.html')
