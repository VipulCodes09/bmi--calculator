import matplotlib.pyplot as plt

def calculate_bmi(weight,height_cm):
    height_m = height_cm/100
    bmi = weight/(height_m**2)
    return round(bmi,2)

def categorize_bmi(bmi):
    if bmi < 16:
        return "Severely Underweight", "Consult a nutritionist for a healthy diet plan."
    elif bmi < 18.5:
        return "Underweight", "Consider a balanced diet and light exercises."
    elif bmi < 25:
        return "Healthy", "Great! Maintain this with regular exercise."
    elif bmi < 30:
        return "Overweight", "Try to include more physical activity in your routine."
    else:
        return "Severely Overweight", "Consult a doctor or dietitian for a health checkup."


def get_user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))

        if weight <= 0 or height_cm <= 0:
          print("please enter values grater than 0")
          return None,None
        return weight,height_cm

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None,None

def show_graph(bmi,category):
  plt.figure(figsize=(7,5))
  bar = plt.bar([category], [bmi], color = 'skyblue')
  plt.title('BMI Category')
  plt.text(0, bmi, f"{bmi}", ha='center', va='bottom', fontsize=14)
  plt.ylim(0,max(40,bmi + 5))
  plt.grid(True, axis='y', linestyle='--', alpha=0.7)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

def main():
    print("\n")
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight and height to calculate your BMI.")
    while True: 
        weight,height_cm = get_user_input()

        if weight is not None and height_cm is not None :
          bmi = calculate_bmi(weight,height_cm)
          if bmi is not None:
            category,advice = categorize_bmi(bmi)
            print(f"\nYour BMI is: {bmi}")
            print(f"\nCategory: {category}")
            print(f"Advice: {advice}\n")

            show_graph(bmi,category)

        choice = input("Do you want to calculate BMI for another person? (yes/no): ").strip().lower()

        if choice != 'yes':
            print("Thank you for using the BMI calculator!")
            break

if __name__ == "__main__":
    main()