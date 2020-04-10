from Membership import member
member1 = member("BB", 53, "Jeju", 161, 60, True)
member2 = member("Seran", 23, "SLC", 170, 58, False)
member3 = member("Danny", 50, "Jeju", 100, 20, True)
member4 = member("Scarlet", 37, "LA", 167, 58, False)

print(member2.weight)
print(member1.name)
if member1.weight >= 60:
    print(member1.name,member1.weight,"Overwight")

print(member1.high_risk_group())




    

