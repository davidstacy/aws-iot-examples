import boto3

#load credentials for demo into the profile with 'aws configure --profile iothackathon

session = boto3.Session(profile_name='iothackathon')
iam = session.client('iam')

#deletes all access keys for these users

for i in range(20):
    username = "user%s" % i
    try:
        user = iam.get_user(UserName=username)
        print "%s found" % username
    except:
        print "no user, creating %s" % username
        user = iam.create_user(UserName=username)
    
    keyresp = iam.list_access_keys(
        UserName=username
    )
    for keymetadata in keyresp['AccessKeyMetadata']:
        print iam.delete_access_key(
            UserName=username,
            AccessKeyId=keymetadata['AccessKeyId']
        )
    
        
