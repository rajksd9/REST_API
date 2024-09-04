import pytest
from src.services.customer_services import CustomerService
 
@pytest.fixture
def customer_service():
    return CustomerService()
 
def test_get_all_customers_success(customer_service, mocker):
    mock_response = {
        "success": "true",
        "payload": [
            {
                "address": "Obere Str. 57",
                "city": "Berlin",
                "company_name": "Alfreds Futterkiste",
                "contact_name": "Maria Anders",
                "contact_title": "Sales Representative",
                "country": "Germany",
                "customer_id": "ALFKI",
                "fax": "030-0076545",
                "phone": "030-0074321",
                "postal_code": "12209",
                "region": "null"
            },
            {
                "address": "Avda. de la Constitución 2222",
                "city": "México D.F.",
                "company_name": "Ana Trujillo Emparedados y helados",
                "contact_name": "Ana Trujillo",
                "contact_title": "Owner",
                "country": "Mexico",
                "customer_id": "ANATR",
                "fax": "(5) 555-3745",
                "phone": "(5) 555-4729",
                "postal_code": "05021",
                "region": "null"
            },
            {
                "address": "Mataderos 2312",
                "city": "México D.F.",
                "company_name": "Antonio Moreno Taquería",
                "contact_name": "Antonio Moreno",
                "contact_title": "Owner",
                "country": "Mexico",
                "customer_id": "ANTON",
                "fax": "null",
                "phone": "(5) 555-3932",
                "postal_code": "05023",
                "region": "null"
            }
        ]
    }
 
    mocker.patch('src.services.customer_services.CustomerService.get_all_customers', return_value=mock_response)
    response = customer_service.get_all_customers()
    assert response['success'] == "true"
    assert len(response['payload']) == 3
    assert response['payload'][0]['customer_id'] == "ALFKI"

def test_get_customer_details_success(customer_service, mocker):
    mock_response = {
        "success": "true",
        "payload": [{
            "address": "Obere Str. 57",
            "city": "Berlin",
            "company_name": "Alfreds Futterkiste",
            "contact_name": "Maria Anders",
            "contact_title": "Sales Representative",
            "country": "Germany",
            "customer_id": "ALFKI",
            "fax": "030-0076545",
            "phone": "030-0074321",
            "postal_code": "12209",
            "region": "null"
        }]
    }
    mocker.patch('src.services.customer_services.CustomerService.get_customer_details', return_value=mock_response)
    response = customer_service.get_customer_details('ALFKI')
    assert response['success'] == "true"
    assert response['payload'][0]['customer_id'] == "ALFKI"


def test_create_customer_success(customer_service, mocker):
    customer_data = {
        "address": "Rue des Rosiers 4",
        "city": "Paris",
        "company_name": "Paris Gourmet",
        "contact_name": "Pierre Dupont",
        "contact_title": "Manager",
        "country": "France",
        "customer_id": "PARIS",
        "fax": "01-22334455",
        "phone": "01-22334455",
        "postal_code": "75004",
        "region": "Ile-de-France"
    }
    mock_response ={
        "success": "true",
        "message": "User Added Successfully",
        "payload": customer_data
    }
    mocker.patch('src.services.customer_services.CustomerService.create_customer', return_value=mock_response)
    response = customer_service.create_customer(customer_data)
    assert response['success'] == "true"
    assert response['payload']['customer_id'] == "PARIS"


def test_update_customer_success(customer_service, mocker):
    customer_data = {
        "contact_name": "Pierre Dupont",
        "contact_title": "Senior Manager"
    }

    updated_data = {
        "address": "Rue des Rosiers 4",
        "city": "Paris",
        "company_name": "Paris Gourmet",
        "contact_name": "Pierre Dupont",
        "contact_title": "Senior Manager",
        "country": "France",
        "customer_id": "PARIS",
        "fax": "01-22334455",
        "phone": "01-22334455",
        "postal_code": "75004",
        "region": "Ile-de-France"
    }

    mock_response ={
        "success": "true",
        "message": "Customer updated successfully.",
        "customer": updated_data
    }
    mocker.patch('src.services.customer_services.CustomerService.update_customer', return_value=mock_response)
    response = customer_service.update_customer('PARIS', customer_data)
    assert response['success'] == "true"
    assert response['customer']['contact_title'] == "Senior Manager"
