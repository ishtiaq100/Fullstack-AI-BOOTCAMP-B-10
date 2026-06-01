# =========================================================
# Assignment No 1 - Week 1
# Use print, input, arithmetic operations, logical conditions
# =========================================================

# 1. Celsius to Fahrenheit
c = float(input("Q1 - Celsius: "))
print("Fahrenheit:", (c * 9/5) + 32)

# 2. Area of Rectangle
l = float(input("\nQ2 - Length: "))
w = float(input("Q2 - Width: "))
print("Area:", l * w)

# 3. Compound Interest
P = float(input("\nQ3 - Principal: "))
R = float(input("Q3 - Rate: "))
T = float(input("Q3 - Time: "))
CI = P * (1 + R/100)**T - P
print("Compound Interest:", CI)

# 4. Perimeter of Rectangle
l = float(input("\nQ4 - Length: "))
w = float(input("Q4 - Width: "))
print("Perimeter:", 2 * (l + w))

# 5. Average of Three Numbers
a = float(input("\nQ5 - Num1: "))
b = float(input("Q5 - Num2: "))
c = float(input("Q5 - Num3: "))
print("Average:", (a + b + c) / 3)

# 6. Square and Cube
n = float(input("\nQ6 - Number: "))
print("Square:", n**2)
print("Cube:", n**3)

# 7. Candies Distribution
candies = int(input("\nQ7 - Candies: "))
students = int(input("Q7 - Students: "))
print("Each gets:", candies // students)
print("Left:", candies % students)

# 8. Profit or Loss
cp = float(input("\nQ8 - Cost Price: "))
sp = float(input("Q8 - Selling Price: "))
if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No Profit No Loss")

# 9. Marks, Total, Percentage
marks = []
for i in range(5):
    marks.append(float(input(f"\nQ9 - Subject {i+1}: ")))
total = sum(marks)
print("Total:", total)
print("Percentage:", (total / 500) * 100)
print("Average:", total / 5)

# 10. Salary Calculator
basic = float(input("\nQ10 - Basic Salary: "))
hra = basic * 0.20
da = basic * 0.15
print("Total Salary:", basic + hra + da)

# 11. Age in Months & Days
years = int(input("\nQ11 - Age in years: "))
print("Months:", years * 12)
print("Days:", years * 365)

# 12. USD to PKR
usd = float(input("\nQ12 - USD: "))
print("PKR:", usd * 280)

# 13. Sum of N Natural Numbers
n = int(input("\nQ13 - N: "))
print("Sum:", n * (n + 1) / 2)

# 14. Percentage Score
total_q = int(input("\nQ14 - Total Questions: "))
correct = int(input("Q14 - Correct Answers: "))
print("Percentage:", (correct / total_q) * 100)

# 15. Speed
d = float(input("\nQ15 - Distance: "))
t = float(input("Q15 - Time: "))
print("Speed:", d / t)

# 16. BMI
weight = float(input("\nQ16 - Weight (kg): "))
height = float(input("Q16 - Height (m): "))
print("BMI:", weight / (height ** 2))

# 17. Minutes to Hours
minutes = int(input("\nQ17 - Minutes: "))
print("Hours:", minutes // 60, "Minutes:", minutes % 60)