#asking the user to enter time in seconds
sec = int(input("Enter time in seconds: "))
#checking if the input time is a non-negative number
if sec >= 0:
    hour = sec // 3600    #converting seconds into hours
    sec %= 3600         #updating sec to the remainder after extracting hours
    min = sec // 60      #converting seconds into minutes
    sec %= 60           #updating sec to the remainder after extracting minutes
    #Printing the time in hours, minutes and seconds format
    print(f"{hour} hour(s) {min} minute(s) {sec} second(s)")
else:
    print("Time must be positive")
