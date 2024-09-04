from flask import make_response
from src.app import db
class CustomerService:
    def get_all_customers(self):
        from src.models.customer_model import Customer  
        try:
            customers = Customer.query.all()
            response = make_response({"success": "true", "payload": [customer.as_dict() for customer in customers]})
            response.status_code = 200
            return response
        except Exception as e:
            print(f"Error fetching customers: {e}")
            response = make_response({"success": "false", "payload": f"Failed to fetch the data. Error: {e}"})
            response.status_code = 404
            return response

    def get_customer_details(self, customer_id):
        from src.models.customer_model import Customer  
        try:
            customer_detail = Customer.query.filter_by(customer_id=customer_id).first()
            if customer_detail is None:
                response = make_response({"success": "false", "message": "No customer with the given customer id exists."})
                response.status_code = 404
                return response
            response = make_response({"success": "true", "payload": [customer_detail.as_dict()]})
            response.status_code = 200
            return response
        except Exception as e:
            print(f"Error fetching customer details: {e}")
            response = make_response({"success": "false", "payload": f"Failed to fetch the data. Error: {e}"})
            response.status_code = 404
            return response

    def create_customer(self, customer):
        from src.models.customer_model import Customer  
        try:
            new_customer = Customer(**customer)
            db.session.add(new_customer)
            db.session.commit()
            response = make_response({"success": "true", "message": "User Added Successfully", "payload": new_customer.as_dict()})
            response.status_code = 201
            return response
        except Exception as e:
            response = make_response({"success": "false", "payload": f"Failed to create customer. Error: {e}"})
            response.status_code = 404
            return response

    def update_customer(self, customer_id, customer_data):
        from src.models.customer_model import Customer 
        try:
            customer = Customer.query.filter_by(customer_id=customer_id).first()
            if customer is None:
                response = make_response({"status": "false", "error": "Customer not found"})
                response.status_code = 404
                return response

            for key, value in customer_data.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)

            db.session.commit()
            response = make_response({
                "success": "true",
                "message": "Customer updated successfully.",
                "customer": customer.as_dict()
            })
            response.status_code = 202
            return response
        except Exception as e:
            db.session.rollback() 
            print(f"Error updating customer: {e}")
            response = make_response({
                "success": "false",
                "message": "Failed to update customer",
                "error": e
            })
            response.status_code = 500
            return response

