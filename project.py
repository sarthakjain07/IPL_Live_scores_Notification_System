
import sports

from pynotifier import Notification

information=sports.get_sport("CRICKET")

Notification(title="IPL Live Score Updates",description=str(information),duration=60).send()
