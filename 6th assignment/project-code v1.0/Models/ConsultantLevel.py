import Level

class ConsultantLevel(Level):
    def __init__(self, consultant_level_id, total_hires, level_winning_points, level_limit,
                 level_remain_points, sells_history, buys_history):
        super().__init__(level_winning_points, level_limit, level_remain_points, sells_history, buys_history)
        self.__consultant_level_id = consultant_level_id
        self.__total_hires = total_hires

    def get_consultant_level_id(self):
        pass

    def get_total_hires(self):
        pass

    def update_consultant_level_id(self, new_consultant_level_id):
        pass

    def update_total_hires(self, new_total_hires):
        pass
    
    def display_consultant_level_details(self):
        pass