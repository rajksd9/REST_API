# from app import app
# from models.customer_model import customer_model
# from flask import request

# customerObj= customer_model()
# @app.route("/customer/getAllCustomers")
# def get_all_customers():
#     print("In customers")
#     return customerObj.get_all_customers()


# @app.route("/customer/createCustomer",methods=["POST"])
# def createCustomer():
#     data=request.form
#     print("Passed from Controller")
#     return customerObj.create_customer(data)



from flask import Blueprint, request, make_response
from src.services.customer_services import CustomerService

customer_service = CustomerService()
customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route("/customer", methods=["GET"])
def get_customers():
    if len(request.args) == 0:
        return customer_service.get_all_customers()
    else:
        customer_id = request.args.get('customer_id')
        if not customer_id:
            response = make_response({"error": "Customer ID is required"}, 400)
            return response
        return customer_service.get_customer_details(customer_id)
        

@customer_bp.route("/customer/createCustomer", methods=["POST"])
def create_customer():
    data = request.get_json()  # Assuming JSON payload  
    result = customer_service.create_customer(data)
    return result

@customer_bp.route('/customer/updateCustomer', methods=['PUT'])
def update_customer():
    customer_id = request.args.get('customer_id')
    if not customer_id:
        response= make_response({"error": "Customer ID is required"})
        response.status_code=400
        return response

    data = request.get_json()
    result = customer_service.update_customer(customer_id, data)
    return result
