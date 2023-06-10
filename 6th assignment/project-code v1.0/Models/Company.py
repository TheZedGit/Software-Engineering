import User

class Company(User):
    def __init__(self, user_id, username, password, firstname, lastname,
                 gender, phone_number, registration_date, country, birthdate, email,
                 socials_list, is_consultant, buyer_level, seller_level, experience_level,
                 achievements_list, comments_list, afm, doy, company_name,
                 company_location, description, extra_info, company_website):
        super().__init__(user_id, username, password, firstname, lastname,
                         gender, phone_number, registration_date, country, birthdate, email,
                         socials_list, is_consultant, buyer_level, seller_level, experience_level,
                         achievements_list, comments_list)
        self.__afm = afm
        self.__doy = doy
        self.__company_name = company_name
        self.__company_location = company_location
        self.__description = description
        self.__extra_info = extra_info
        self.__company_website = company_website

    def get_afm(self):
        pass

    def get_doy(self):
        pass

    def get_company_name(self):
        pass

    def get_company_location(self):
        pass

    def get_description(self):
        pass
    
    def get_extra_info(self):
        pass

    def get_company_website(self):
        pass