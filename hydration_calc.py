flour = int(input("How much flour are you using? (grams)"))
water = int(input("How much water are you using? (grams)"))


hydration = water/(flour/100)

print("Your dough, {}g flour and {}g water, has {}% hydration.".format(flour, water, hydration))