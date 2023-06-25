income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
lowtaxland_amt = income*lowtaxland_rate
ripoffland_amt = income*ripoffland_rate


print('Your income is {} and you would pay {} income tax in Lowtaxland or {} income tax in Ripoffland. You would save {} by paying taxes in Lowtaxland!'.format (income, lowtaxland_amt, ripoffland_amt, ripoffland_amt - lowtaxland_amt))