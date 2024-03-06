import time
from plyer import notification

if __name__ == "__main__":
    
    notification.notify(
        title = "Welcome to my github account.",
        message = "This is my  my first project which i upload on github repository.",
        app_icon  = None,
        timeout  = 10
)
    
    time.sleep(7)