largeInteger = int(input("Enter large integer representing seconds\n"))
print(type(largeInteger))

secondType = largeInteger

print(secondType)


hourType = int(secondType / 3600)

forMin = secondType - (hourType * 3600)

minType = int(forMin / 60)


print(str(secondType) + " second is " + str(hourType) + " hours, " + str(minType) + " minutes, and " + str(0) + " seconds")




