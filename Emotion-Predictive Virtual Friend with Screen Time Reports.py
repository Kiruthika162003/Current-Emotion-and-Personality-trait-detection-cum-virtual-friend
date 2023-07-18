# Function for emotion prediction (replace with actual emotion prediction model)
def predict_emotion(user_input):
    # Simulate emotion prediction
    emotions = ['happy', 'sad', 'angry', 'excited', 'calm']
    detected_emotion = np.random.choice(emotions)
    return detected_emotion

# Function for responding to user based on detected emotion
def respond_to_emotion(detected_emotion):
    if detected_emotion == 'happy':
        return "I'm glad to hear that! How can I make your day even better?"
    elif detected_emotion == 'sad':
        return "I'm sorry to hear that. Remember, it's okay to feel down. Is there anything I can do to help?"
    elif detected_emotion == 'angry':
        return "I understand. Take a deep breath and let's work through it together."
    elif detected_emotion == 'excited':
        return "That sounds amazing! Let's share your excitement together!"
    else:
        return "I'm here for you. How can I support you?"

# Function for generating screen time report (replace with actual screen time data)
def generate_screen_time_report():
    # Simulate screen time data for the past week
    screen_time_data = {
        'Monday': 4.5,
        'Tuesday': 5.2,
        'Wednesday': 3.8,
        'Thursday': 4.1,
        'Friday': 6.2,
        'Saturday': 7.5,
        'Sunday': 5.0
    }
    return screen_time_data

def main():
    # Simulate user input (you can replace this with actual user interactions)
    user_input = "Hey, virtual friend, I had a rough day at work today..."

    # Predict user's emotion
    detected_emotion = predict_emotion(user_input)

    # Respond to user based on the detected emotion
    response = respond_to_emotion(detected_emotion)

    # Generate and display the screen time report
    screen_time_data = generate_screen_time_report()
    print("Screen Time Report:")
    for day, time in screen_time_data.items():
        print(f"{day}: {time} hours")

    print("\nVirtual Friend: ", response)

if __name__ == "__main__":
    main()
