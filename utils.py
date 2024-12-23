# Installed libraries
from pywhatkit import whats

# Used for getting current time
from datetime import datetime as dt

# Main class that builds messages to be sent
class WhatsAppMessage:
    """
        A class that acts as a blueprint for messages that can be scheduled 
        to be sent on WhatsApp.
    """
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message
    
    def send(self) -> None:
        """
            Sends message instantly.
        """
        whats.sendwhatmsg_instantly(self.phone, self.message)
    
    def send_later(self, hours, minutes) -> None:
        """
            Sends message at a scheduled time.
        """
        whats.sendwhatmsg(self.phone, self.message, hours, minutes)

    def send_to_group(self, group_id: str) -> None:
        whats.sendwhatmsg_to_group_instantly(group_id, self.message, self.hours, self.minutes)

    def send_to_group_later(self, group_id: str, hours: int, minutes: int) -> None:
        whats.sendwhatmsg_to_group(group_id, self.message, hours, minutes)

# -Other tools-
def get_current_time() -> str:
    """
        Returns current time in hours and minutes.
    """
    current_time = dt.now()
    hours_now = current_time.hour
    minutes_now = current_time.minute
    current_hour_minute = f"{hours_now:02}:{minutes_now:02}"
    return current_hour_minute