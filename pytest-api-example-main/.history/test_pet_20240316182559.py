from jsonschema import validate
import pytest
import api_helpers
from app import PET_STATUS
import schemas
from jsonschema.exceptions import ValidationError 

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
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
'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", PET_STATUS)
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
'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("invalid_id", [-1, 9999])  # Edge cases for invalid IDs
def test_get_by_id_404(invalid_id):
    test_endpoint = f"/pets/{invalid_id}"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 404