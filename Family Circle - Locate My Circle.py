import folium

# Function to display the family circle map
def display_family_circle(locations):
    # Create a map centered at a specific location (replace with actual center coordinates)
    m = folium.Map(location=[12.3456, 78.9101], zoom_start=12)

    # Add markers for each family member's location
    for name, location in locations.items():
        folium.Marker(location).add_to(m)

    # Display the map
    m.save('family_circle_map.html')
    print("Family Circle Map saved as 'family_circle_map.html'. Open the file to view the map.")

def main():
    # Predefined family member locations (replace with actual locations)
    family_locations = {
        "Family Member 1": [12.3456, 78.9101],
        "Family Member 2": [12.3457, 78.9102],
        "Family Member 3": [12.3458, 78.9103],
        # Add more family member locations as needed
    }

    # Display the family circle map
    display_family_circle(family_locations)

if __name__ == "__main__":
    main()
