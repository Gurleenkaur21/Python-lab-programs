#WAP to Log File Writer

with open("log.txt","a") as f:
 msg=input("Enter log: ")
 f.write(msg+"\n")