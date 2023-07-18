# Sample set of questions
questions = [
    "How often do you feel overwhelmed with your responsibilities? (Never/Sometimes/Often)",
    "How well do you sleep at night? (Very well/Okay/Poorly)",
    "How frequently do you experience physical symptoms of stress? (Rarely/Sometimes/Often)",
    # Add more questions as needed
]

# Function to calculate stress level based on user responses
def calculate_stress_level(responses):
    stress_score = 0
    for response in responses:
        # Assign scores based on user responses (higher scores indicate higher stress)
        if response == "Often" or response == "Poorly" or response == "Often":
            stress_score += 1
        # Add more scoring rules as needed

    # Calculate the stress level based on the total score (you can customize the stress level ranges)
    if stress_score >= 3:
        stress_level = "high"
    elif stress_score >= 2:
        stress_level = "moderate"
    else:
        stress_level = "low"

    return stress_level

def main():
    print("Stress Level Finder")
    print("Please answer the following questions:")

    user_responses = []
    for question in questions:
        response = input(question + " ")
        user_responses.append(response)

    stress_level = calculate_stress_level(user_responses)

    print("\nBased on your responses, your stress level is:", stress_level.upper())

if __name__ == "__main__":
    main()
