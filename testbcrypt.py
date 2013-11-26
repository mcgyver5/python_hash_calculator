import bcrypt

def testing_the_b():
    text = "password"
    hashed = bcrypt.hashpw(text, bcrypt.gensalt())
    print hashed
    hashed2 = bcrypt.hashpw(text,bcrypt.gensalt())
    print hashed2
    hashed3 = bcrypt.hashpw(text,bcrypt.gensalt())
    print hashed3

    if bcrypt.checkpw(text,hashed):
        print("it worked")
    else:
        print("it did not work!")
    hashed44 = bcrypt.hashpw(text,bcrypt.gensalt(6))

    if bcrypt.checkpw(text,hashed3):
        print("it worked")
    else:
        print("it did not work!")
print("hello")
testing_the_b()