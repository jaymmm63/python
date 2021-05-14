#1 US Gallon = 3.7854118 litres
#1 mile = 1609.344 meter

# To convert from miles per gallon to liters per 100 kilometers

def convert_mileage(mil):
    dist_km = mil * 1609.344/1000
    fuel_lt = 3.7854118
    dist_100km = dist_km / 100
    milege = fuel_lt/dist_100km
    return milege

m=float(input('Enter milege in miles per gallon: '))
new_m = convert_mileage(m)
print('milege = ',new_m,'liters per 100 kilometer')

