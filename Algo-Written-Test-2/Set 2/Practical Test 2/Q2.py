# Correct Answer
def CalcBill(unit):
    if unit <= 100:  
        payment = 0
    elif 101 <= unit <= 200:
        payment = (unit - 100)* 0.8
    elif unit >= 201:
        payment = (100*0.8)+ ((unit-200)*1.5)

    return payment 

unit= int(input("ENter electric units"))
print("RM", CalcBill(unit))






