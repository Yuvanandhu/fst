#if nested if 
age=18
nationality="INDIAN"
if(age>=18):
    if nationality=="INDIAN":
        print("you are eligble for vote to an INDIA")
    else:
        print("only allowed INDIAN to vote")
else:
    print("your age is less than 18")