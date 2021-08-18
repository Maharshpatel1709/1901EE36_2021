def meraki_helper(n):
    
    while True:
        
        if(n // 10 == 0):
            return True
        
        dig1 = n % 10
        
        n = n // 10
        
        dig2 = n % 10
        
        if(abs(dig1 - dig2) != 1):
            return False
            

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

meraki = 0
non_meraki = 0

for i in input:
    
    if meraki_helper(i):
        meraki += 1
        print("Yes -", i, "is a Meraki number")
    else:
        non_meraki += 1
        print("No -", i, "is not a Meraki number")

print("the input list contains", meraki, "meraki and", non_meraki, "non meraki numbers.")