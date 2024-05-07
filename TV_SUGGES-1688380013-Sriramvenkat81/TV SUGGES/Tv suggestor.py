import pandas as pd
print("Television recommendation mini project")
print()
print("This portal helps you to find the best Tv available in the market..")
print()
print("Prices mentioned are INR")
print()
print("Type 1 for 32 inches, Type 2 for 43 inches, Type 3 for 55 inches ")
print()
model=int(input("Enter your Type of tv: "))
print()
tv_parts = pd.read_csv('tv.csv')
for index, row in tv_parts.iterrows():
    if(row['Type :']==model):
        print(row)
        print()
print("Choose according to your preference")
print()
print("THANK YOU")
