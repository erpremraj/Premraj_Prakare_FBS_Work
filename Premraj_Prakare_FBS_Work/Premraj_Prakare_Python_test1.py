# firstbit.pragati@gmail.com - ma'ams gmail

# Ques1
# user integer input
# rectangle
length = int(input("Enter length : "))
breadth = int(input("Enter breadth : "))
# circle
radius =  int(input("Enter radius of circle : "))
pi = 3.142
diameter = 2 * radius
print("Your rectangle values of length and breadth are ", length ,"and", breadth)
print("Your circle values of pi, radius and diameter are ", pi ,",", radius,"," , diameter)
areaOfCircle = (0.5) * pi * radius ** radius
periOfCircle = (pi * diameter) / 2
periOfRectangle = 2 * ( length + breadth )
areaOfRectangle = length * breadth
print("Perimeter of Rectangle : " , areaOfRectangle)
print("Perimeter of Rectangle : " , periOfRectangle)
print("Area of Circle : " , areaOfCircle)
print("Perimeter of Circle : " , periOfCircle)

# Ques 2
principle = float(input("Enter principle amount : "))
rate = float(input("Enter rate of interest ( % per year) : "))
time = float(input("Enter time in years : "))
print("Your values of principle, rate,time are : ",principle,",",rate,",",time)
si = (principle * rate * time) / 100
print("Simple Interest is : ",si)

# Ques3
kilometers = float(input("Enter distance in kilometers : "))
# conversion
meters = kilometers * 1000
centimeters = kilometers * 100000
print("You entered distance in kilometers : " , kilometers)
print("Distance in meters : " , meters)
print("Distance in centimeters : " , centimeters)


# Ques 4
# Take user for units
interiorArea = float(input("Enter Total area of interior walls : "))
exteriorArea = float(input("Enter Total area of exterior walls : "))
interiorCost = float(input("Enter cost for interior painting : "))
exteriorCost = float(input("Enter cost for exterior painting : "))

# Calculate total painting cost
totalInteriorCost = interiorArea * interiorCost
totalExteriorCost = exteriorArea * exteriorCost
totalCost = totalInteriorCost + totalExteriorCost

# Display results
print("Cost of painting interior walls : " , totalInteriorCost)
print("Cost of painting exterior walls : " , totalExteriorCost)
print("Total painting cost : " , totalCost)
