import Level

class ExperienceLevel(Level):
    def __init__(self, experience_level_id, has_challenges, is_active, bids_history, level_winning_points,
                 level_limit, level_remain_points, sells_history, buys_history):
        super().__init__(level_winning_points, level_limit, level_remain_points, sells_history, buys_history)
        self.__experience_level_id = experience_level_id
        self.__has_challenges = has_challenges
        self.__is_active = is_active
        self.__bids_history = bids_history

    def get_experience_level_id(self):
        pass

    def has_challenges(self):
        pass

    def is_active(self):
        pass

    def get_bids_history(self):
        pass

    def update_experience_level_id(self, new_experience_level_id):
        pass

    def update_has_challenges(self, new_has_challenges):
        pass

    def update_is_active(self, new_is_active):
        pass

    def update_bids_history(self, new_bids_history):
        pass

    def display_experience_level_details(self):
        pass