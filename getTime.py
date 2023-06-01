import time
import ntptime
import utime

def set_local_timezone():
    # Stel de tijdzone in op de lokale tijdzone
    # Pas het onderstaande offset aan op basis van jouw lokale tijdzone
    timezone_offset = 2 * 3600  # Offset van 2 uur voor UTC+2
    
    utime.timezone(timezone_offset)

def get_local_time_string():
    # Set the system time using an NTP server
    #set_local_timezone();
    
    ntptime.settime()
    
    # Get the local time
    local_time = time.localtime()
    
    # Extract the desired components
    year, month, day, hour+2, minute, _, _, _ = local_time
    
    # Create the string representation of the local time
    time_string = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}".format(year, month, day, hour, minute)
    
    # Return the time string
    return time_string



