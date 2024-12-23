# Installed libraries
from pywhatkit import whats

# My own modules
from utils import WhatsAppMessage, get_current_time

# Gets current time in hours and minutes
current_time = get_current_time()

test_msg = WhatsAppMessage(
    '', # Insert the receiver's number here
    f'Test message sent at {current_time}.',
)

try:
    test_msg.send()

except Exception as e:
    print("error in sending message:", e)