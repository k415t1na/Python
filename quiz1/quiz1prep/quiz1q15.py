status=1
income=20

if status == 0:     
# Compute tax for single filers
    if income>0 and income<8350:
        print("the taxes are: ", income*0.1)

    elif income>8351 and income<33950:
        print("the taxes are: ", income*0.15)

    elif income>33951 and income<82250:
        print("the taxes are: ", income*0.25)

    elif income>82251 and income<137050:
        print("the taxes are: ", income*0.28)

    elif income>137051 and income<372950:
        print("the taxes are: ", income*0.33)
    
    elif income>372951:
        print("the taxes are: ", income*0.35)

    else:
        print("the  ")

    

elif status == 1:     
    # Compute tax for married filing jointly

elif status == 2:     
    # Compute tax for married filing separately

elif status == 3:    
     # Compute tax for head of household

else:   
     #   # Display wrong status