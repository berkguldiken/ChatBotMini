import re
import time
from logger import Logger as lg

lg.start()

bot_template = "BOT : {0}"
user_template = "USER : "
print(bot_template.format("you can exit this chatbot by typing exit"))

URL_template="www.websitename.com/search="
idStock={"STCK-0001":["phone","20"],"STCK-0002":["jacket","5"],"STCK-0003":["cup","0"],"STCK-0004":["hat","100"]}
faqs={"when will I get the product":"7 to 14 days",
        "Can I pay online?":"absolutely",
        "how much cargo fee do I need to pay?":"10$ for every shipment",
        "how much tax I need to pay?":"you can calculate it by (total cost of your shopping cart * 0.18)",
        "can I change my address after I bought something? ":"you need to change within first 3 days after purchasing",
        "can I refund the item before 30 days":"yes, in 30 days you can refund it",
        "can I cancel the purchase":"yes, if you cancel it within a day",
        "can I refund the item after 30 days":"no" }

while 1:
    time.sleep(1)
    print(bot_template.format("any question?"))
    
    inp=input()
    if inp=="exit":
        break
        lg.stop()
     
    

    def urlSend(message):
        msg=re.search(r"((?<=find).*$)",message)
        msg1=msg.group(0)
        msg2=re.findall(r"(\W)",msg1)
        split_msg=re.findall(r"\w+",msg1)
        urlstr=""
        for it in range(len(msg2)):
            urlstr=urlstr+split_msg[it]+"+"
        urlstr=urlstr[:-1]
        time.sleep(0.5)
        print("you can find them with this link: "+URL_template+urlstr)
        time.sleep(0.5)
        

    def stock(message):
        for key,value in idStock.items():
            if re.search(key,message) or re.search(value[0],message):
                time.sleep(0.5)
                print(bot_template.format("Products stock count: "+value[1]))
                time.sleep(0.5)

    def stocklearn(message):
        for key,value in idStock.items():
            if re.search(value[0],message):
                print("Stock ID for "+value[0]+" is "+key)

    def faq(message):
        count=0
        previousc=0
        msg=re.findall(r"(\w+)",message)
        for key, value in faqs.items():
            for k in range(len(msg)):
                if msg[k] in key:
                    count+=1
            if count > previousc:
                selectedvalue= value
                previousc=count
            count=0
        time.sleep(0.5)
        print(bot_template.format(selectedvalue))  
        print(bot_template.format("you can also look for the FAQ's in our website: www.websitename.com/faqs"))  
        time.sleep(0.5)



    def manage(message):   
            if re.search(r"(how|where)", message) and re.search(r"(find)", message):
                urlSend(message)
  

            elif re.search(r"(how many|how much|stock)",message) and re.search(r"(STCK-|have|buy)",message):
                stock(message)
            elif re.search(r"tax|fee|online|when|address|cancel|refund",message):
                faq(message)
            elif re.search(r"learn|know|tell|get|inform",message) and re.search(r"stock id|Stock id|stock ID|id|Id|",message):
                stocklearn(message)
            else:
                time.sleep(0.5)
                print(bot_template.format("Oh no! Couln't understand what you are searching."))
                time.sleep(0.5)
            
    manage(inp)
        


