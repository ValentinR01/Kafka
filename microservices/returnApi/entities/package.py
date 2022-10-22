from datetime import datetime


class Package:
    def __init__(self:object, package_id: int, sender_id: int, receiver_id: int, state: str, sending_date: datetime):
        self.package_id = package_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.state = state
        self.sending_date = sending_date



    




