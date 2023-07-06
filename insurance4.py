# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
akira_insurance_cost = estimate_insurance_cost("akira", 19, 1, 27.1, 0, 0)


names = ["Maria", "Rohan", "Valentina", "Akira"]
insurance_cost = [ 4150.0, 5320.0, 35210.0, 2930.0 ]
insurance_data = list(zip(names, insurance_cost))
print("Here is the actual insurance cost data:")
print(insurance_data)

estimate_insurance_data = []
estimate_insurance_data.append(("Maria", maria_insurance_cost))
estimate_insurance_data.append(("Rohan", rohan_insurance_cost))
estimate_insurance_data.append(("Valentina", valentina_insurance_cost))
estimate_insurance_data.append(("Akira", akira_insurance_cost))
estimate_insurance_data2 = [4222.0, 5442.0, 36368.0]
print("Here is the estimated insurance cost:")
print(estimate_insurance_data)

insurance_cost_difference = 0

def difference_cost(num1, num2):
  difference_cost = num1 - num2
  return difference_cost

difference_cost_maria = [difference_cost(maria_insurance_cost, 4150.0)]
difference_cost_rohan = [difference_cost(rohan_insurance_cost, 5320.0 )]
difference_cost_valentina = [difference_cost(valentina_insurance_cost, 35210)]
difference_cost_akira = [difference_cost(akira_insurance_cost, 2930.0)]

difference_cost_list = []
difference_cost_list.append(("Maria", difference_cost_maria))
difference_cost_list.append(("Rohan", difference_cost_rohan))
difference_cost_list.append(("Valentina", difference_cost_valentina))
difference_cost_list.append(("Akira", difference_cost_akira))
print(difference_cost_list)

