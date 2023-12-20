# using the time module for calcuating the time 
# typing speed counts as per WPM method that is words per minute but in this program, the speed is calculated by words per second
# random module is used for giving the different context after every execution
# in this program, i just collected some text from internet regarding AI, ML and Python


from time import *                                          #importing time module for calculating the time
import random                                               #generating random choice from the context variable


def mistake (paragraph_test, user_test):                    #created a function for calculating the mistakes
    error = 0
    for i in range(len(paragraph_test)):                    #loop for checking one by one character from the context variable
        try:                                                #try or except used for error handling and if a user doesn't type full sentence, instead of throwing error it will execute the program
            if paragraph_test[i] != user_test[i]:           #conditional statement applied because the actual_text charcters are not equal to user-text so that it will increase the error by 1
                error = error + 1
            if paragraph_test[i] == user_test[i]:           #if there is exact same match then, it will remain the error free
                error = error
        except:
            error = error + 1                               #if a user type more letters than actual_text then, it will again increase the error by 1
    return error


def speed_time(time_start,time_end,user_input):             #function created for calculating the speed in seconds
    time_delay = (time_end - time_start)                    #time ends subtract the started time
    exact_time = round(time_delay)                          #rounding off the time 
    speed = len(user_input)/exact_time                      #calculaing the time
    return round(speed,2)                                   #again round off the speed 
    

print("\n\n\t\t\t\t ***** Typing Speed *****\n")

while True:                                                        #created a while loop if a user is interested to type again so, he/she can able to input yes other wise no.
    check = input("Ready for the test: 'yes/no:'  ")
    check = check.lower()
    if check == "yes":
    
    # created a context variable which is a 'list' data type and i just enetered 3 long substrings in it.

        context = [
        '''AI stands for artificial intelligence, which is the ability of machines or software to perform tasks that normally require human intelligence, such as reasoning, learning, or problem-solving. AI is a broad field of study that includes many subfields and applications, such as machine learning, natural language processing, computer vision, speech recognition, and robotics. AI can be used for various purposes, such as entertainment, education, health care, business, and security.''',
        '''Machine learning is a subfield of artificial intelligence that uses algorithms trained on data sets to create models that enable machines to perform tasks that would otherwise only be possible for humans, such as categorizing images, analyzing data, or predicting price fluctuations. Machine learning can be divided into three main types: supervised learning, unsupervised learning, and reinforcement learning.''',
        '''Python is a popular programming language that is easy to learn and widely used for various purposes. It is an interpreted, object-oriented, high-level language with dynamic semantics and a powerful standard library. It supports multiple programming paradigms, such as procedural, object-oriented, and functional programming.'''
                 ]

        test = random.choice(context)                       #it will generate the random text from the context variable
        print(test)
        time1 = time()                                      #noted the time before inputing
        testinput = input("Enter: ")                        #user inputting the string
        time2 = time()                                      #noted the time ends

        print("Speed: ", speed_time(time1,time2,testinput),"average words per second")              #calling the speed function
        print("Error: ",mistake(test,testinput))                                                    #calling the mistake function
    
    elif check == "no":
        print("Thank You! for giving the test -> @abhinav_gera")
        break
    
    else:                                                    #while loop, if a user enetered something else instead of yes or no. so it would be an invalid input from the user.
        print("Invalid Input")
