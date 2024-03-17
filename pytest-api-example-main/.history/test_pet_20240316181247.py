from jsonschema import validate
import pytest
import api_helpers
from app import PET_STATUS
import schemas
from jsonschema.exceptions import ValidationError
def test_pet_schema():
    test_endpoint = "/pets/1"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 200

    # Get the 'id' field from the response
    pet_id = response.json().get('id')

    # Check if the 'id' field is an integer
    assert isinstance(pet_id, int), f"Expected 'id' to be an integer, but got {pet_id} of type {type(pet_id)}"

    try:
        # Validate the response schema against the defined schema in schemas.py
        validate(instance=response.json(), schema=schemas.pet)
    except ValidationError as e:
        assert False, f"Response does not match schema: {e}"

def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {"status": status}

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200

    for pet in response.json():
        pet_id = pet.get('id')
        assert isinstance(pet_id, int), f"Expected 'id' to be an integer, but got {pet_id} of type {type(pet_id)}"

        assert pet['status'] == status

        try:
            validate(instance=pet, schema=schemas.pet)
        except ValidationError as e:
            assert False, f"Response does not match schema: {e}"

def test_patch_order_by_id():
    # Create a test order
    response = api_helpers.post_api_data("/store/order", {"pet_id": 1})
    assert response.status_code == 201, f"Failed to create order: {response.json()}"

    order_id = response.json()["id"]

    # Update the order status
    update_response = api_helpers.patch_api_data(f"/store/order/{order_id}", {"status": "sold"})

    assert update_response.status_code == 200, f"Failed to update order: {update_response.json()}"

    assert update_response.json()["message"] == "Order and pet status updated successfully", f"Unexpected response message: {update_response.json()}"
