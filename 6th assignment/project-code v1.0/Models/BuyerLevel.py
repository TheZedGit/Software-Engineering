import Level

class BuyerLevel(Level):
    def __init__(self, buyer_level_id, total_buys, level_winning_points, level_limit,
                 level_remain_points, sells_history, buys_history):
        super().__init__(level_winning_points, level_limit, level_remain_points, sells_history, buys_history)
        self.__buyer_level_id = buyer_level_id
        self.__total_buys = total_buys

    def get_buyer_level_id(self):
        pass

    def get_total_buys(self):
        pass

    def update_buyer_level_id(self, new_buyer_level_id):
        pass

    def update_total_buys(self, new_total_buys):
        pass

    def display_buyer_level_details(self):
        pass