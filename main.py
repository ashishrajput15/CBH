import math
import numpy as np
import matplotlib.pyplot as plt

def growth(prev_capital, prev_no_driver, prev_no_rider):
    CAC_driver=500
    rider_per_month = 100
    new_rider = 0
    new_driver = 0
    
    
    capital = prev_capital
    new_capital=1
    while (new_capital>0):
        
        if (new_capital<=0):
            pass
        else:
            new_rider = new_rider+100
            no_rider = new_rider + prev_no_rider
            new_driver = max(math.ceil(no_rider/100 -prev_no_driver),0)
            if (prev_no_rider==0):
                rate_of_growth=0.5
            else:
                rate_of_growth=new_rider/prev_no_rider
            CAC_rider=10+rate_of_growth*20
            new_capital = prev_capital - new_rider*CAC_rider - new_driver*CAC_driver
            capital = new_capital
        
    no_driver = new_driver+prev_no_driver
    no_rider = new_rider + prev_no_rider
    return(capital, no_driver, no_rider)

def revenue(margin):
    
    matching_rate=min(150-25*margin,100)
    probability_failed = 100-matching_rate
    Churn_rider = (2+probability_failed*33/100)/100
    
    capital = 50000000
    no_driver = 0
    no_rider =0
    
    Churn_driver = .05
    monthly_revenue = 0
    
    arr_month=[None]*12    
       
    for month in range (0,12):
        no_driver = no_driver*(1-Churn_driver)
        no_rider = no_rider*(1-Churn_rider)
        capital, no_driver, no_rider = growth(capital, no_driver, no_rider )
        
        monthly_revenue=no_rider*margin
        capital = capital + monthly_revenue
        arr_month[month]=round(capital)
    return (arr_month)


last_month_rev=[]
arr_margin=[]
i=-1
for margin in np.arange(1, 8, .02):
    i+=1
    arr_month=revenue(margin)
    print(i,round(margin,2),arr_month[11])
    last_month_rev.append(arr_month[11])
    arr_margin.append(margin)

top_3_values = sorted(last_month_rev)[-3:]
top_3_indices = [last_month_rev.index(value) for value in top_3_values]
print(f'Top 3 values: {top_3_values}')
print(f'Indices of top 3 values: {top_3_indices}')


plt.plot(arr_margin, last_month_rev)

plt.xlabel('Margins')
plt.ylabel('MRR at the end of 12th month')

plt.show()
