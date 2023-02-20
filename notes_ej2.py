print ("HEM DIRAS LA NOTA I TE DIRE QUE TENS ")
nota=float(input("Dis-me la teua nota"))

if nota >10 or nota<0:
    print ("Això no es possible")   
elif nota<5:
    print("Insuficient")
elif nota<6:
    print("Suficient")
elif nota<7:
    print("be")
elif  nota<=9:
    print("Notable")
elif nota>= 9 or nota<=10:
    print("Excel·lent")

