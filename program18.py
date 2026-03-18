#WAP to Count Lines and Words

with open("test.txt") as f:
 data=f.read()
print("Lines:",data.count("\n")+1)
print("Words:",len(data.split()))