# Function to display the guide mode interface
def display_guide_mode():
    print("Welcome to Guide Mode!")
    print("In this mode, we provide step-by-step instructions to help you navigate the platform easily.")
    print("Please select an action:")
    print("1. Check notifications")
    print("2. View messages")
    print("3. Browse content")
    print("4. Settings")

def guide_mode_instructions(action):
    if action == 1:
        print("To check notifications, click on the 'Bell' icon located in the top right corner of the screen.")
    elif action == 2:
        print("To view messages, click on the 'Messages' tab in the navigation menu.")
    elif action == 3:
        print("To browse content, use the search bar to find your desired topic and click on the search results.")
    elif action == 4:
        print("To access settings, click on your profile picture and select 'Settings' from the dropdown menu.")
    else:
        print("Invalid option. Please select a valid action.")

def main():
    # Display guide mode interface
    display_guide_mode()

    # Simulate user selection (replace this with actual user input)
    selected_action = int(input("Enter the number of the action you want to learn more about: "))

    # Display instructions for the selected action
    guide_mode_instructions(selected_action)

if __name__ == "__main__":
    main()
