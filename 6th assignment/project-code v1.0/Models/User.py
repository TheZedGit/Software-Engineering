import Company

class User:
    def __init__(self, user_id, username, password, firstname, lastname,
                 gender, phone_number, registration_date, country, birthdate, email,
                 socials_list, is_consultant, buyer_level, seller_level, experience_level,
                 achievements_list, comments_list):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__phone_number = phone_number
        self.__registration_date = registration_date
        self.__country = country
        self.__birthdate = birthdate
        self.__email = email
        self.__socials_list = socials_list
        self.__is_consultant = is_consultant
        self.__buyer_level = buyer_level
        self.__seller_level = seller_level
        self.__experience_level = experience_level
        self.__achievements_list = achievements_list
        self.__comments_list = comments_list
        
    def get_user_id(self):
        pass

    def get_username(self):
        pass

    def get_fullname(self):
        pass

    def get_gender(self):
        pass

    def get_phone_number(self):
        pass

    def get_registration_date(self):
        pass

    def get_country(self):
        pass

    def get_birthdate(self):
        pass

    def get_email(self):
        pass

    def get_socials_list(self):
        pass

    def is_consultant(self):
        pass

    def get_buyer_level(self):
        pass

    def get_seller_level(self):
        pass

    def get_experience_level(self):
        pass

    def get_achievements_list(self):
        pass

    def get_comments_list(self):
        pass
    
    def modifyProfile(self):
        pass
    
    def update_username(self, new_username):
        pass

    def update_password(self, new_password):
        pass

    def update_email(self, new_email):
        pass

    def update_phone_number(self, new_phone_number):
        pass

    def update_socials_list(self, new_socials_list):
        pass

    def update_profile_info(self, new_firstname, new_lastname, new_gender, new_birthdate):
        pass
    
    
def switch_to_company_profile(self):
    if self.isConsultant == 0:  
        company_name = input("Enter company name: ")
        doy = input("Enter DOY: ")
        afm = input("Enter company AFM: ")
        company_website = input("Enter company website (optional): ")
        if company_name and doy and afm:
            self.isConsultant = 1  
            self.company = Company(afm, doy, company_name, company_website)
            print("Switch to company profile successful!")
        else:
            print("Please fill in the required fields.")
    else:
        print("You already have a company profile.")