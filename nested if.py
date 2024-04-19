uei="humaira@gmail.com"
upw=1234
uotp=8907
emailid=str(input('enter the email id:'))
password=int(input('enter the password:'))
if(emailid==uei):
    if(password==upw):
        print('login success')
        otp=int(input('enter otp:'))
        if(uotp!=otp):
            print('transaction failed due to invalid otp')
        else:
                print('transaction successful')
    else:
        print('login failed due to incorrect password')
else:
    print('login failed due to incorrect email')
    