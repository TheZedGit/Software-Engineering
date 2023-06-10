import Level

class SellerLevel(Level):
    def __init__(self, seller_level_id, total_sells, level_winning_points, level_limit,
                 level_remain_points, sells_history, buys_history):
        super().__init__(level_winning_points, level_limit, level_remain_points, sells_history, buys_history)
        self.__seller_level_id = seller_level_id
        self.__total_sells = total_sells

    def get_seller_level_id(self):
        pass

    def get_total_sells(self):
        pass

    def update_seller_level_id(self, new_seller_level_id):
        pass

    def update_total_sells(self, new_total_sells):
        pass
    
    def display_seller_level_details(self):
        pass