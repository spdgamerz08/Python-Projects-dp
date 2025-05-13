import pywhatkit as kit
import pandas as pd
import time

# Load numbers from Excel file
file_path = "your_file.xlsx"  # Update this with your actual file path
df = pd.read_excel(file_path)

message = "Hello, this is an automated message from Python!"

for index, row in df.iterrows():
    phone_number = row["PhoneNumber"]  # Ensure the column name matches your Excel file
    kit.sendwhatmsg_instantly(f"+{phone_number}", message, wait_time=10)
    time.sleep(5)  # Wait time to avoid issues

print("Messages sent successfully!")
