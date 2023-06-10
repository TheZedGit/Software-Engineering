import Community

class Notification(Community):
    def __init__(self, community_id, type, notification_id, message, notifier_id):
        super().__init__(community_id, type)
        self.__notification_id = notification_id
        self.__message = message
        self.__notifier_id = notifier_id

    def get_notification_id(self):
        pass

    def get_message(self):
        pass
    
    def get_notifier_id(self):
        pass
    
    def update_notification_id(self, new_notification_id):
        pass
    
    def update_message(self, new_message):
        pass
    
    def update_notifier_id(self, new_notifier_id):
        pass
    
    def display_notification_details(self):
        pass
    
    def notication():
        pass
    
    def sendNotification():
        pass