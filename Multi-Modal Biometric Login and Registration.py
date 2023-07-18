# Sample User Database (replace with an actual database)
users = {}

# Function for user registration
def register_user(username, password, face_template, voice_template):
    if username in users:
        print("Username already exists. Please choose another.")
    else:
        users[username] = {
            'password': password,
            'face_template': face_template,
            'voice_template': voice_template
        }
        print("Registration successful!")

# Function for face recognition (replace with real face recognition model/API)
def recognize_face(face_template, registered_face_template):
    # Simulate face recognition by comparing face templates
    return face_template == registered_face_template

# Function for voice recognition (replace with real voice recognition model/API)
def recognize_voice(voice_template, registered_voice_template):
    # Simulate voice recognition by comparing voice templates
    return voice_template == registered_voice_template

# Function for user login
def login(username, password, face_template=None, voice_template=None):
    if username not in users or users[username]['password'] != password:
        print("Invalid username or password.")
    else:
        if face_template and not recognize_face(face_template, users[username]['face_template']):
            print("Face recognition failed.")
        elif voice_template and not recognize_voice(voice_template, users[username]['voice_template']):
            print("Voice recognition failed.")
        else:
            print("Login successful!")

def main():
    # User Registration
    register_user("john_doe", "password123", "john_face_template", "john_voice_template")

    # User Login
    login("john_doe", "password123", "john_face_template", "john_voice_template")

if __name__ == "__main__":
    main()
