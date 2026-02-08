import allure
import pytest
import json
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_Manager import *
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be "
        "200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Utils().common_header_json_with_Cookies(),
                                payload=payload_create_booking())

        booking_id = response.json()["bookingid"]

        verfiy_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null(booking_id)
