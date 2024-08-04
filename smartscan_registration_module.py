import pyqrcode
import cv2

# In-Memory Storage
users_db = []

def in_memory():
    # Lambda functions
    create = lambda name, email, gender: {"name": name, "email": email, "gender": gender}
    insert = lambda user: users_db.append(user)
    fetch = lambda: users_db
    return create, insert, fetch

# SmartScan Code Generation
def generate_smartscan(name, email, gender, filename):
    data = f"{name},{email},{gender}"
    qrcode = pyqrcode.create(data)
    qrcode.png(filename, scale=8)
    print(f"QR code saved to {filename}")

# SmartScan Code Decoding
def decode_smartscan(path):
    img = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)
    if vertices_array is not None:
        return data
    else:
        return None

# Decode User Data
def decode_smartscan_code(code):
    name, email, gender = code.split(',')
    return {"name": name, "email": email, "gender": gender}

# User Registration Function 
def RegisterUserFromSmartScan(path, create, insert, fetch):
    # Decode the SmartScan Code
    decoded_data = decode_smartscan(path)
    if not decoded_data:
        print("No user data found in the SmartScan code.")
        return

    # Extract user data from the decoded SmartScan code
    user_data = decode_smartscan_code(decoded_data)
    name = user_data['name']
    email = user_data['email']
    gender = user_data['gender']

    # Create a new user record
    new_user = create(name, email, gender)
    
    # Insert the user record into the in-memory list
    insert(new_user)
    
   

