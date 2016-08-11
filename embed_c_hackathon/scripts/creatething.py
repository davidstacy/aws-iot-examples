import boto3

#capture inputs
thingname = raw_input("Please enter your thing name: ")

#load credentials for demo into the profile with 'aws configure --profile iothackathon
session = boto3.Session(profile_name='iothackathon',region_name='us-east-1')
iot = session.client('iot')

#create a thing
print "creating thing"
thing_resp = iot.create_thing(thingName=thingname)

#create a certificate and capture arn this will be the principal
print "creating keys and certs"
create_key_resp = iot.create_keys_and_certificate(
    setAsActive=True
)
print "writing certificate to certs/cert.pem"
with open("../certs/cert.pem", "w") as pemfile:
    pemfile.write(create_key_resp['certificatePem'])

print "writing privatekey to certs/privkey.pem"
with open("../certs/privkey.pem", "w") as pvkeyfile:
    pvkeyfile.write(create_key_resp['keyPair']['PrivateKey'])

#policy document
policy_doc = '''{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": ["iot:*"],
        "Resource": ["*"]
        }
}
'''

#create a policy 
print "creating full access policy"
policy_name="FullAccessPolicy-%s" % thingname

create_policy_resp = iot.create_policy(
    policyName=policy_name,
    policyDocument=policy_doc
)


#attach policy to the principal
print "attaching policy"
attach_policy_resp = iot.attach_principal_policy(
    policyName=policy_name,
    principal=create_key_resp['certificateArn']
)

#attach thing to the principal
print "attaching thing"
attach_thing_resp = iot.attach_thing_principal(
    thingName=thingname,
    principal=create_key_resp['certificateArn']
)






    
        
