import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def verify_number():
    phone_number = entry_number.get()
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            messagebox.showerror("Error", "Invalid phone number!")
            return
        
        # Fetch details
        country = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        time_zones = ", ".join(timezone.time_zones_for_number(parsed_number))
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        # Display details
        result_text.set(
            f"Formatted Number: {formatted_number}\n"
            f"Country: {country}\n"
            f"Service Provider: {service_provider}\n"
            f"Time Zone(s): {time_zones}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Create the interface
app = tk.Tk()
app.title("Phone Number Verification")
app.geometry("400x300")

# Input field
label_instruction = tk.Label(app, text="Enter phone number with country code (e.g., +11234567890):")
label_instruction.pack(pady=10)

entry_number = tk.Entry(app, width=30)
entry_number.pack(pady=5)

# Verify button
button_verify = tk.Button(app, text="Verify", command=verify_number)
button_verify.pack(pady=10)

# Display result
result_text = tk.StringVar()
label_result = tk.Label(app, textvariable=result_text, justify="left")
label_result.pack(pady=10)

# Run the app
app.mainloop()
