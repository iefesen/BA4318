reserve = 0
while reserve < 100:
    print("Current Reserve is: ", reserve)
    incoming=int(input("Please make a deposit on the reserve: "))
    reserve=reserve+incoming
else :
    print("Exiting the loop with: ", reserve)
if reserve >500:
    print("We Deposited Really Fast")
elif reserve >200:
    print("We normally deposited")
else:
    print("We deposited slowly")

wallet = [1,1, 5, 5, 5, 10, 10, 10, 100, 100]
sum = 0
for note in wallet:
    sum=sum+note
print("Sum is: ", sum)


coordinates = [ (0,0), (1,2), (4,5)]
area = 0
for a,b in coordinates:
    area= area+ a*b
print("Area of the coordinates is: ", area)



xs = (0,1,4)
ys = (0, 2, 5)
zipped = zip(xs, ys)
zippedlist = list(zipped)
print(zippedlist)

emails = {}
emails["METU"] = "efe.senyuva@metu.edu.tr"
emails["Bilkent"] = "efe.senyuva@bilkent.edu.tr"
emails["Gmail"] = "efe.senyuva@gmail.com"
for k in emails:
    print("Key: ", k)
    
for k,v in emails.items():
    print("Key: ", k , "Value: ", v)