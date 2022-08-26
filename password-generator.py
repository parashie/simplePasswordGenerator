import random

#asks user for name
print('Hello user')
n = input('What is your name user?')

#characters to use in generator
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

#simple input questions, will change floats to ints
number = input('How many passwords do you want me to create for you?')
number = int(number)
length = input('Password Length')
length = int(length)

#function to create password
def createPassword():
    print('Here are your passwords:')
    # for loop for the password generation
    for password in range(number):
        pswd = ''
        for c in range(length):
            pswd += random.choice(charset)
        print(pswd)

createPassword()


print('Goodbye, ' + n + '!')

input('Press ENTER to exit')



