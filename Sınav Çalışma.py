weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("Zero-day:", weekdays[0])
print("Number of days:", len(weekdays))
print("Is there a Sunday in weekdays?", ("Sunday" in weekdays))
weekend=("Saturday","Sunday")
wholeweek=weekend+weekdays
print("Whole Week: " , wholeweek)
boxdimensions = [ 24, 25, 30]
identity = ["Ilgın Efe", "Şenyuva", "İşsiz", "Business Administration", 2076990]
print("The size of the tuples are:", len(boxdimensions), len(identity), "respectively")
print(boxdimensions[-1])
namedata=identity[0:2]
print(namedata)
print("Name:",namedata[0], "Surname:", namedata[1])
restof=identity[2:]
print(restof)
boxinfo = [ boxdimensions, None, namedata]
print(boxinfo)
boxvolume = boxdimensions[-1] * boxdimensions[-2] * boxdimensions[-3]
boxinfo[1]=boxvolume
print(boxinfo)
address = "METU"
boxinfo.append(address)
print ("Dimensions:", boxinfo[0], " Volume: ", boxinfo[1], " to be delivered to:", boxinfo[2])
print("The address to deliver to: ", boxinfo[3])
x1 = [1,2,3]
x2 = [9,8,7]
x1.extend(x2)
print ("Extended list:", x1)
phone="05342161204"
identity.insert(4,phone)
print(identity)
print(x1)
del x1[2:4]
print(x1)
print("Inserted", identity[4], "just before", identity[5])
x1.sort()
print(x1)
copyx1=sorted(x1)
print(copyx1)
reversecopyx1=sorted(x1, reverse=True)
print(reversecopyx1)
print("Minimum value of x1:", min(x1), "Maximum value of x1:", max(x1))
fivezeroes = [0] * 5
print(fivezeroes)
original=[ [0,1,2], 1]
shallow = original[:]
print(shallow)
import copy
deep=copy.deepcopy(original)
print(deep)
shallow[0][0]=5
print(shallow)
print("Original's version: ", original[0])
print("Deep's version: ", deep[0])
print("Shallow version: ", shallow[0])
weekdaylist=list(weekdays)
print(weekdays)
Hello="Hello"
hellochars=list(Hello)
print(Hello)