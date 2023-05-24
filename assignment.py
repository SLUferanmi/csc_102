phone_num = input ("please provide your phone number: ")
while True :
    password = input ("please create a suitable password for your account: ")
    tomakesure = input(" please re-enter your password: ")
    if password == tomakesure :
        print ("you have successfully made your account")
        break
    if password != tomakesure :
        print ("passwords don't match. Please try again") 
        continue
print ("welcome to login page")
while True:
    login_num = input ("provide your phone number: ") 
    if login_num == phone_num :
        break
    if login_num != phone_num :
        print ("sorry, your phone number is not in our records.")
        print ("please check the number and try again")
        continue
while True : 
    login_pw = input ("please enter your password: ")
    if login_pw == password :
        break
    if login_pw != password :
        print (" you entered a wrong password")
        print(" please try again")
        continue
print (" Welcome to your Dashboard!") 
