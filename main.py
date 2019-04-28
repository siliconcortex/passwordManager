import getpass
import sys
import random
import pickle
import re
import file_leslie
import caesarcipher_leslie


def save():
    file_leslie.save('database.pickle',database)

def encryptAll():
    for account, password in database.items():
        password = caesarcipher_leslie.caesarEncrypt(password,OFFSET)
        database[account] = password

def decryptAll():
    for account, password in database.items():
        password = caesarcipher_leslie.caesarEncrypt(password,REVERSEOFFSET)
        database[account] = password
        
OFFSET = 5
REVERSEOFFSET = -5
file_leslie.initialize('database.pickle')
database = file_leslie.load('database.pickle')
decryptAll()


print('LESLIE PASSWORD MANAGER lesliecaminade@gmail.com')
print('================================================')
print('Type the master password:')

#ask for a passsword
try: 
    masterpassword = getpass.getpass() 
except Exception as error:
    
    print('ERROR', error) 


#check if the password is correct
if masterpassword == 'yourkungfuisweak':
    print('Logged in.')
    print('search - type in any set of characters')
    print('save %accountinfo% %password%')
    print('save %accountinfo% generate')
    print('showall')
    print('del %accountinfo_exact%')
    
else:
    print('Wrong password. Exiting.')
    sys.exit()

end = False
while (end == False):

    
    
    command = input()

    #separate the command by splitting the string input
    #command, arg1, arg2, arg3
    commandSplit = command.split(' ')
    

    #check against saved passwords
    for account, password in database.items():
       
        if re.search(commandSplit[0],account):
            print (account + ': ' + password)


    #generate a new password
    if commandSplit[0] == 'generate':
        # generate a password with length "passlen" with no duplicate characters in the password
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        passlen = 20
        p =  "".join(random.sample(s,passlen ))
        print (p)

    #create a new password entry
    if commandSplit[0] == 'save':
        #check if there are proper inputs
        if len(commandSplit) == 3:  
            #ask for the key
            #print('input account: ')
            #accountInput = input()
            #print('input password / type generate: ')
            accountInput = commandSplit[1]

            #check if generate
            passwordInput = commandSplit[2]
            if passwordInput == 'generate':
                            # generate a password with length "passlen" with no duplicate characters in the password
                            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                            passlen = 20
                            p =  "".join(random.sample(s,passlen ))
                            print (p)
                            database[accountInput] = p
            else:
                    #place the password into memory
                    #passwordEncrypted = caesarcipher_leslie.caesarEncrypt(passwordInput,OFFSET)
                    database[accountInput] = passwordInput
                    

                        
        #send an invalid input error
        else:
            print('invalid input')

        


    #deleting a password
    if commandSplit[0] == 'del' or commandSplit[0] =='delete':
        accountInput = commandSplit[1]
        del database[accountInput]
        print(accountInput + ' is deleted')

    #show all data
    if commandSplit[0] == 'showall':
        print('ACCOUNT: PASSWORD')
        print('======================================')
        for account, password in database.items():
            print(account + ': ' + password)
        print('===============end of file================')
            
    #exit the program
    if commandSplit[0] == 'exit':
        encryptAll()
        save()
        #terminate the program
        end = True

    #force encrypt
    if commandSplit[0] == 'encrypt':
        encryptAll()

    #force decrypt
    if commandSplit[0] == 'decrypt':
        decryptAll()




        










    
    
    
