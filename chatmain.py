import re
import time
from logger import Logger as lg

lg.start()

bot_template = "BOT : {0}"
user_template = "USER : "

URL_template="www.websitename.com/search=" #template for generating searc URL
idStock={"STCK-0001":["phone","20"],"STCK-0002":["jacket","5"],"STCK-0003":["cup","0"],"STCK-0004":["hat","100"]}
#idStock for looking stock id's and names and gives how much left in the storage
faqs={"when will I get the product":"7 to 14 days",
        "Can I pay online?":"absolutely",
        "how much cargo fee do I need to pay?":"10$ for every shipment",
        "how much tax I need to pay?":"you can calculate it by (total cost of your shopping cart * 0.18)",
        "can I change my address after I bought something? ":"you need to change within first 3 days after purchasing",
        "can I refund the item before 30 days":"yes, in 30 days you can refund it",
        "can I cancel the purchase":"yes, if you cancel it within a day",
        "can I refund the item after 30 days":"no" }
#basic FAQ(Frequently Asked Questions) and answers


while 1: #loop for continuation of the program

    time.sleep(1) #to look like more human 
    print(bot_template.format("any question? ( you can exit by typing 'exit')"))# asking every time after the operations end
    
    inp=input() # taking input from customer
    if inp=="exit": #if customer type exit the program will end and algo logging will end
        break
        lg.stop()
     
    

    def urlSend(message): # this function takes user message, find the keywords after 'find' keyword and generate an URL
        msg=re.search(r"((?<=find).*$)",message) # extracting the sentence after 'find' keyword
        msg1=msg.group(0)   #selecting all the words
        msg2=re.findall(r"(\W)",msg1) #extracting spaces between words
        split_msg=re.findall(r"\w+",msg1) # extracting words on message
        urlstr=""
        for it in range(len(msg2)): # loop for generating search URL
            urlstr=urlstr+split_msg[it]+"+"
        urlstr=urlstr[:-1] # erasing the last '+' sign
        time.sleep(0.5)
        print("you can find them with this link: "+URL_template+urlstr) #printing the generated URL
        time.sleep(0.5)
        

    def stock(message): # a function for learning how much stock remaining for a certain product
        count=0
        for key,value in idStock.items(): # loop iterates over idStock
            if re.search(key,message) or re.search(value[0],message): #looking for either stock id or product name
                time.sleep(0.5)
                print(bot_template.format("Products stock count: "+value[1])) # printing the value
                time.sleep(0.5)
                count+=1
        if count==0:
            print("Oh no! Couln't understand what you are searching.")

    def stocklearn(message):    # a function for learning stockid for named product
        count=0
        for key,value in idStock.items(): # loop iterates over idStock
            if re.search(value[0],message): # looking for product name
                print("Stock ID for "+value[0]+" is "+key) # printing the id
                count+=1
        if count==0:
            print("Oh no! Couln't understand what you are searching.")

    def faq(message): # a function for looking the message and gives corresponding answer if message is a FAQ
        count=0
        previousc=0
        msg=re.findall(r"(\w+)",message) # extracting word
        for key, value in faqs.items(): #loop for iterates over faq
            for k in range(len(msg)): # loop for iterates over length of message
                if msg[k] in key: # if a message's word matches a word in directories increase count by 1
                    count+=1
            if count > previousc: # checking for most similar question
                selectedvalue= value
                previousc=count #saving the current count value for later uses
            count=0
        if previousc==0:
            print("Oh no! Couln't understand what you are searching.")
        time.sleep(0.5)
        print(bot_template.format(selectedvalue))  
        print(bot_template.format("you can also look for the FAQ's in our website: www.websitename.com/faqs"))  
        time.sleep(0.5)



    def manage(message):   # this function manages the user input and select where the message will go so it can be evaluated 
            if re.search(r"(how|where)", message) and re.search(r"(find)", message): # deciding whether the question is searching for something or not
                urlSend(message)
            elif re.search(r"(how many|how much|stock)",message) and re.search(r"(STCK-|have|buy)",message): # deciding whether the question is for learning the stock number
                stock(message)
            elif re.search(r"tax|fee|online|when|address|cancel|refund",message): # deciding whether the question is for general FAQs
                faq(message)
            elif re.search(r"learn|know|tell|get|inform",message) and re.search(r"stock id|Stock id|stock ID|id|Id|",message): # deciding for whether the question is to learn stock id or not
                stocklearn(message)
            else: # if nothing else then it will generate an error
                time.sleep(0.5)
                print(bot_template.format("Oh no! Couln't understand what you are searching."))
                time.sleep(0.5)
            
    manage(inp)
        


