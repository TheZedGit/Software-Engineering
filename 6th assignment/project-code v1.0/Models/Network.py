import Community

class Network(Community):
    def __init__(self, community_id, type, followers, following):
        super().__init__(community_id, type)
        self.__followers = followers
        self.__following = following

    def get_followers(self):
        return self.__followers

    def get_following(self):
        return self.__following

    def update_followers(self, new_followers):
        self.__followers = new_followers

    def update_following(self, new_following):
        self.__following = new_following

    def display_network_details(self):
        super().display_community_details()
        print("Followers:", self.__followers)
        print("Following:", self.__following)