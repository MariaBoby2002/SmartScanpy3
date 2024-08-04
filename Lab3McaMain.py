from smartscan_registration_module import generate_smartscan, RegisterUserFromSmartScan, in_memory

# Define lambda functions
create, insert, fetch = in_memory()

# Print existing users
print("Existing users in the in-memory database:")
exusers = fetch()  
for user in exusers:
    print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")
else:
    print("No User")


# Prompt the user for their details to add directly to the in-memory database
print("\nEnter user details to add directly to the in-memory database:")
name = input("Name: ")
email = input("Email: ")
gender = input("Gender: ")

# Insert the user data directly into the in-memory storage
direct_user = create(name, email, gender)
insert(direct_user)

# Print updated user list
print("\nUpdated users in the in-memory database after direct entry:")
exusers = fetch()  # Fetch data again to see the updated list
for user in exusers:
    print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")

# Prompt the user for details to generate a SmartScan code
print("\nEnter details for SmartScan code generation:")
scan_name = input("Name: ")
scan_email = input("Email: ")
scan_gender = input("Gender: ")

# Prompt for QR code filename
filename = input("Enter the QR code file name (e.g., 'smartscan.png'): ")
if not filename.lower().endswith(".png"):
    print("Filename should end with '.png'. Appending '.png' to the filename.")
    filename += ".png"

# Generate a SmartScan Code with user input
generate_smartscan(scan_name, scan_email, scan_gender, filename)

# Register user from the generated SmartScan Code
print("\nRegistering user from SmartScan code...\n")
RegisterUserFromSmartScan(filename, create, insert, fetch)
users = fetch()  # Fetch data again to see the updated list
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}, Gender: {user['gender']}")


