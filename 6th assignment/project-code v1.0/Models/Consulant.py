import User

class Consultant(User):
    def __init__(self, user_id, username, password, firstname, lastname,
                 gender, phone_number, registration_date, country, birthdate, email,
                 socials_list, is_consultant, buyer_level, seller_level, experience_level,
                 achievements_list, comments_list, resume, extra_info, specialization,
                 residence, tk, face_to_face_evaluation):
        super().__init__(user_id, username, password, firstname, lastname,
                         gender, phone_number, registration_date, country, birthdate, email,
                         socials_list, is_consultant, buyer_level, seller_level, experience_level,
                         achievements_list, comments_list)
        self.__resume = resume
        self.__extra_info = extra_info
        self.__specialization = specialization
        self.__residence = residence
        self.__tk = tk
        self.__face_to_face_evaluation = face_to_face_evaluation

    def get_resume(self):
        pass

    def get_extra_info(self):
        pass

    def get_specialization(self):
        pass
    
    def get_residence(self):
        pass

    def get_tk(self):
        pass

    def has_face_to_face_evaluation(self):
        pass