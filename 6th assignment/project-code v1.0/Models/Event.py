import Community
import LiveAuction

class Event(Community):
    def __init__(self, community_id, type, host_id, auction_items_list, description, start_date, participants, live_video, photos, live_room_link):
        super().__init__(community_id, type)
        self.__host_id = host_id
        self.__auction_items_list = auction_items_list
        self.__description = description
        self.__start_date = start_date
        self.__participants = participants
        self.__live_video = live_video
        self.__photos = photos
        self.__live_room_link = live_room_link
        self.__live_auction = None

    def set_live_auction(self, live_auction_id, participants_list, participant_id, live_room_id):
        self.__live_auction = LiveAuction(live_auction_id, participants_list, participant_id, live_room_id)

    def get_live_auction(self):
        return self.__live_auction

    def get_host_id(self):
        pass

    def get_auction_items_list(self):
        pass

    def get_description(self):
        pass

    def get_start_date(self):
        pass

    def get_participants(self):
        pass

    def get_live_video(self):
        pass

    def get_photos(self):
        pass

    def get_live_room_link(self):
        pass

    def update_host_id(self, new_host_id):
        pass

    def update_auction_items_list(self, new_auction_items_list):
        pass

    def update_description(self, new_description):
        pass

    def update_start_date(self, new_start_date):
        pass

    def update_participants(self, new_participants):
        pass

    def update_live_video(self, new_live_video):
        pass

    def update_photos(self, new_photos):
        pass

    def update_live_room_link(self, new_live_room_link):
        pass

    def display_event_details(self):
        pass
    
    def participate(self):
        pass
    
    def mopdifyevent(self, host_id):
        pass
    
    def deleteEvent(self, host_id):
        pass
    
    def addEvent(self, host_id):
        pass