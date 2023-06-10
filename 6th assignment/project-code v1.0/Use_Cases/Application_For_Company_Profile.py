from Models.User import User
import sqlite3

class ChangingInCompanyProfile:
    def __init__(self):
        self.conn = None
        self.user = None

    def connect_to_database(self):
        self.conn = sqlite3.connect("database.db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY, username TEXT, password TEXT, "
                          "firstname TEXT, lastname TEXT, gender TEXT, phone_number TEXT, registration_date TEXT, "
                          "country TEXT, birthdate TEXT, email TEXT, socials_list BLOB, is_consultant INTEGER, "
                          "buyer_level TEXT, seller_level TEXT, experience_level TEXT, achievements_list BLOB, "
                          "comments_list BLOB)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS company_profiles (user_id TEXT PRIMARY KEY, company_name TEXT, "
                          "dou TEXT, afm TEXT, company_website TEXT)")

    def disconnect_from_database(self):
        if self.conn:
            self.conn.close()

    def run_use_case(self):
        self.connect_to_database()

        user_id = input("Enter your User ID: ")
        user = self.retrieve_user(user_id)
        if user is None:
            print("User not found.")
        else:
            self.user = user
            self.view_profile_menu()

        self.disconnect_from_database()

    def retrieve_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = ?"
        cursor = self.conn.execute(query, (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(*user_data)
        return None

    def view_profile_menu(self):
        while True:
            print("\nProfile Menu:")
            print("1. View Personal Profile")
            print("2. Switch to Company Profile")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.user.view_personal_profile()
            elif choice == "2":
                self.user.switch_to_company_profile(self.conn)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

        print("\nExiting the profile menu.")
