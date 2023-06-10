import Application

class ApplicationConsultant(Application):
    def __init__(self, application_id, application_result, application_date, application_model, text, consultant_id):
        super().__init__(application_id, application_result, application_date, application_model, text)
        self.__consultant_id = consultant_id

    def get_consultant_id(self):
        pass
    
    def update_consultant_id(self, new_consultant_id):
        pass

    def display_application_details(self):
        pass