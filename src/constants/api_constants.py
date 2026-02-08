#Keep all api ulrs
#static Method--> which can be call by without the obbeject dicrectly by using class you can call it
class APIConstants:
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_token():
        return f"{APIConstants.base_url()}/auth"

    @staticmethod
    def url_create_booking():
        return f"{APIConstants.base_url()}/booking"

    @staticmethod
    def url_put_patch_delete(self,booking_id):
        return f"{APIConstants.base_url()}/booking/{booking_id}"
