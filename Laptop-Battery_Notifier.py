import time
import psutil
from pynotifier import Notification

def Notify(description,percent):
    Notification(title="Battery Notification By Masum",
                 description=description + "\n...poweredBy Abdullah Al Masum".format(percent),
                 duration=16,
                 urgency=Notification.URGENCY_CRITICAL,
                 icon_path='C:/Users/Malware/Desktop/masum.ico').send();
def main():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    plugged = battery.power_plugged
    global msg;
    msg=""
    global urgency;
    if plugged:
        msg = "Charger Plugged In \n"
        if(percentage<80):
            msg += "Your battery is charging {}% now \nKeep Charging...".format(percentage)
        elif(percentage>=80 and percentage<100):
            msg +="Battery right now {}% \nYou can remove your charger.".format(percentage)
        elif(percentage==100):
            msg +="Battery is {}% full\nPlease plugged out the charger.".format(percentage)
    else:
        msg = "Charger is not plugged in\n"
        if(percentage<=20):
            msg += "Your battery is running low.\nOnly {}% battery remaining\nCharge right now.".format(percentage)
        elif(percentage==100):
            msg +="Battery is fully charged {}%\nEnjoy your time.".format(percentage)
        else:
            msg += "Battery charge remaining {}%".format(percentage)

    time.sleep(4)
    Notify(msg,percentage)

if __name__ == '__main__':
    main();
