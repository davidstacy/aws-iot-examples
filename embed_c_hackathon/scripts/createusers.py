import boto3
import random
import string

#load credentials for demo into the profile with 'aws configure --profile iothackathon

session = boto3.Session(profile_name='iothackathon')
iam = session.client('iam')

password_file = open('keys.csv', 'w+')

for i in range(20):
    username = "user%s" % i
    try:
        user = iam.get_user(UserName=username)
        print "%s found" % username
    except:
        print "no user, creating %s" % username
        user = iam.create_user(UserName=username)

    print iam.attach_user_policy(
        UserName=username,
        PolicyArn='arn:aws:iam::aws:policy/AWSIoTFullAccess'
    )
    
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    response = iam.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=False
    )

    keyresp = iam.create_access_key(
        UserName=username
    )
    userkey = "%s,%s,%s,%s\n" %(
        username,
        keyresp['AccessKey']['AccessKeyId'],
        keyresp['AccessKey']['AccessKeyId'],
        password
    )
    
    password_file.write(userkey)

password_file.close()   

    
        
