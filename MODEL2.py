import pandas as pd

def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (in kg) and height (in meters).
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def bmi_tracker():
    """
    Main function to input data, calculate BMI, and classify it.
    """
    print("Welcome to the BMI Tracker!")

    # Input weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))

    # Input height in meters
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)

    # Display results
    print(f"Your BMI is {bmi:.2f}, which is classified as {classification}.")

    # Optionally, save results to a DataFrame and CSV
    data = {
        'Weight (kg)': [weight],
        'Height (m)': [height],
        'BMI': [bmi],
        'Classification': [classification]
    }
    df = pd.DataFrame(data)
    df.to_csv('bmi_results.csv', index=False)
    print("Results have been saved to 'bmi_results.csv'.")

# Run the BMI Tracker
bmi_tracker()
