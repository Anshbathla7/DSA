Days=int(input("enter the no of day's average temperature"))
total=0
temp=[]
for i in range(Days):
    days_temp=int(input(f"enter the {i+1}'s Days temperature"))
    temp.append(days_temp)
    total+=temp[i]
avg=round(total/Days,2)
print(f"average temperature is {avg}")

above=0
for i in temp:
    if i >avg:
        above+=1
print(f"{above} are the days which is above avg temperature")



