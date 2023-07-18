# Function for Guest Dashboard
def guest_dashboard():
    print("Welcome to the Guest Dashboard!")
    # Add guest-specific functionalities and content here

# Function for Admin Dashboard
def admin_dashboard():
    print("Welcome to the Admin Dashboard!")
    # Add admin-specific functionalities and content here

# Function for Old Person Dashboard
def old_person_dashboard():
    print("Welcome to the Old Person Dashboard!")
    # Add functionalities and content suitable for older users here

# Function for Working Professional Dashboard
def working_professional_dashboard():
    print("Welcome to the Working Professional Dashboard!")
    # Add functionalities and content suitable for working professionals here

# Function for Special Person Dashboard
def special_person_dashboard():
    print("Welcome to the Special Person Dashboard!")
    # Add functionalities and content for users with special needs here

# Function for Normal User Dashboard
def normal_user_dashboard():
    print("Welcome to the Normal User Dashboard!")
    # Add general functionalities and content for regular users here

def main():
    # Simulate user type (you can replace this with actual user type detection or input)
    user_type = "Admin"  # Replace with the actual user type

    # Display the appropriate dashboard based on the user type
    if user_type == "Guest":
        guest_dashboard()
    elif user_type == "Admin":
        admin_dashboard()
    elif user_type == "Old Person":
        old_person_dashboard()
    elif user_type == "Working Professional":
        working_professional_dashboard()
    elif user_type == "Special Person":
        special_person_dashboard()
    else:
        normal_user_dashboard()

if __name__ == "__main__":
    main()
