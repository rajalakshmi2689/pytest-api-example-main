from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    # Create a test order
    response = api_helpers.post_api_data("/store/order", {"pet_id": 1})
    assert response.status_code == 201
    order_id = response.json()["id"]

    # Update the order status
    update_response = api_helpers.patch_api_data(f"/store/order/{order_id}", {"status": "sold"})

    # Check if the status code is as expected
    assert update_response.status_code == 200, f"Expected status code 200, but got {update_response.status_code}"

    # Check if the response message is correct
    assert update_response.json()["message"] == "Order and pet status updated successfully"

# Helper functions to create and cleanup test orders
def create_test_order():
    # Creating a test order using POST request
    response = api_helpers.post_api_data("/store/order", {"pet_id": 1})
    assert response.status_code == 201
    order_id = response.json()["id"]
    return order_id

def cleanup_test_order(order_id):
    # Cleaning up the test order by deleting it using DELETE request
    response = api_helpers.delete_api_data(f"/store/order/{order_id}")
    assert response.status_code == 200
