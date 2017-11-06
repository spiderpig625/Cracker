import md5

counter = 1

pass_in = raw_input("Please enter the MD5 Hash: ")
pwfile = raw_input("Please enter the password file name: ")
try:
        pwdfile = open(pwfile, "r")
except:
        print ("\nFile not found.")
        quit()
for password in pwfile:
        filemd5 = md5.new(password.strip()).hexdigest()
        print ("Trying password number %d: %s ") % (counter, password.strip())

        counter += 1

        if pass_in == filemd5:
                print ("\nMatch Found. \nPassword is: %s") % password
                break

else: print ("\nPassword Not Found.")
