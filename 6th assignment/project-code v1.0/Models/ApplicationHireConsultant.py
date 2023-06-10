import Application

class ApplicationConsultant(Application):
    def __init__(self, application_id, application_result, application_date, application_model, text, applicant_id):
        super().__init__(application_id, application_result, application_date, application_model, text)
        self.__applicant_id = applicant_id

    def get_applicant_id(self):
        pass

    def update_applicant_id(self, new_applicant_id):
        pass

    def display_application_details(self):
        pass