def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name +" is "+ str(estimated_cost) + " dollars")
  return estimated_cost

def difference_insurance_cost(first_insurance_cost, second_insurance_cost):
  difference_insurance_cost = first_insurance_cost - second_insurance_cost
  print("The difference in insurance cost is "+ str(difference_insurance_cost) + " dollars")
  return difference_insurance_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

#Extra
nicola_insurance_cost = calculate_insurance_cost("Nicola", 28, 1, 38, 0, 1)

#Extra2
difference_insurance_cost(omar_insurance_cost, maria_insurance_cost)