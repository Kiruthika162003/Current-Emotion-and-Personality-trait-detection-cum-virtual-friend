""" The Emotion-Based Content Recommendation System is a Python program that offers personalized content recommendations to users based on their detected emotions.
By simulating emotion recognition, the system categorizes users into specific emotional states such as happy, sad, excited, or calm. 
It then leverages an extensive content database, including various genres of movies, TV series, music, and nature soundscapes, each tagged with relevant emotion categories.
Users can access the system through a user-friendly interface, log in with their unique ID, and receive content suggestions tailored to their current emotional state. 
The system also considers users' past search history and screen time, creating personalized profiles to refine recommendations further."""

import random

# Emotion categories for content tagging
EMOTION_CATEGORIES = {
    'happy': ['comedy', 'romance', 'uplifting music'],
    'sad': ['drama', 'melancholic music'],
    'excited': ['action', 'thriller', 'energetic music'],
    'calm': ['relaxing music', 'nature sounds'],
    # Add more emotion categories and corresponding content types as needed
}

# Sample content database
content_database = {
    'comedy': ['Sitcom A', 'Stand-up Comedy B'],
    'romance': ['Romantic Movie X', 'Romantic Comedy Y'],
    'uplifting music': ['Song 1', 'Song 2'],
    'drama': ['Drama Movie Z', 'TV Series C'],
    'melancholic music': ['Song 3', 'Song 4'],
    'action': ['Action Movie D', 'Action Series E'],
    'thriller': ['Thriller Movie F', 'Thriller Series G'],
    'energetic music': ['Song 5', 'Song 6'],
    'relaxing music': ['Song 7', 'Song 8'],
    'nature sounds': ['Nature Soundscapes H', 'Nature Soundscapes I'],
    # Add more content entries as needed
}

# Sample user profiles database (you can replace this with an actual database)
user_profiles = [
    {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'emotion': 'happy',
        'search_history': ['travel', 'cooking', 'music'],
        'screen_time_history': {'date': '2023-07-18', 'duration': '2 hours'},
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'age': 25,
        'emotion': 'sad',
        'search_history': ['books', 'poetry', 'movies'],
        'screen_time_history': {'date': '2023-07-18', 'duration': '3 hours'},
    },
    # Add more user profiles as needed
]

def get_user_emotion():
    # Simulate emotion recognition or user input
    emotions = list(EMOTION_CATEGORIES.keys())
    return random.choice(emotions)

def get_user_preferences(user_id):
    # Simulate user preferences (search history and screen time)
    for user_profile in user_profiles:
        if user_profile['id'] == user_id:
            return user_profile
    return None

def get_emotion_based_recommendation(emotion, user_preferences):
    # Get content categories associated with the detected emotion
    content_categories = EMOTION_CATEGORIES.get(emotion, ['general'])

    # Create a list of recommended content based on user's preferred categories
    recommended_content = []
    for category in content_categories:
        if category in content_database:
            content_list = content_database[category]
            recommended_content.extend(content_list)

    # Shuffle the list of recommendations to provide a diverse selection
    random.shuffle(recommended_content)

    return recommended_content

def display_recommendations(username, user_emotion, recommendations):
    print(f"\nHi {username}!")
    print(f"Based on your emotion ({user_emotion}), we recommend:")
    for idx, content in enumerate(recommendations, start=1):
        print(f"{idx}. {content}")

def main():
    # Emotion recognition (you can replace this with actual emotion detection)
    user_emotion = get_user_emotion()

    # Simulate user login (you can replace this with actual user authentication)
    user_id = 1  # Replace with the user ID of the logged-in user

    # Get user preferences (you can replace this with actual user data retrieval)
    user_preferences = get_user_preferences(user_id)
    if not user_preferences:
        print("User not found!")
        return

    # Get emotion-based recommendations for the user
    recommendations = get_emotion_based_recommendation(user_emotion, user_preferences)

    # Display the recommendations to the user
    display_recommendations(user_preferences['name'], user_emotion, recommendations)

if __name__ == "__main__":
    main()
