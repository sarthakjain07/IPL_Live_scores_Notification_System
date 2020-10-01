''' working : This program will automatically display the notifications 
    of the IPL match on your desktop after a short duration'''

# Gather live up-to-date sports scores.    
import sports

# Module for displaying desktop notificatioms
from pynotifier import Notification

# Fetching information about cricket 
information=sports.get_sport("CRICKET")
    
# Getting notification using fetched information
Notification(title="IPL Live Score Updates",description=str(information),duration=60).send()
