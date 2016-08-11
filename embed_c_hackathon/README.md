
== Instructions

=== Get the code

git clone https://github.com/davidstacy/aws-iot-examples

=== Explore the codee

Check out the Makefile and README.md


=== Configure Credentials

find your assigned username and keys

configure your credentials
```
aws configure --profile iothackathon
```

use region: us-east-1

=== create a thing

cd scripts
python creatething.py

=== compile C code

adjust headers

make
