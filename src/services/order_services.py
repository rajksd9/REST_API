from src.models.order_model import Order
from flask import make_response
from src.app import db

class OrderService:
    def get_all_orders(self):
        try:
            orders = Order.query.all()
            response = make_response({"success": "true", "payload": [order.as_dict() for order in orders]})
            response.status_code = 200
            return response
        except Exception as e:
            response = make_response({"success": "false", "payload": f"Failed to fetch orders. Error: {e}"})
            response.status_code = 404
            return response

    def create_order(self, order):
        try:
            new_order = Order(
                order_id=order['order_id'],
                customer_id=order['customer_id'],
                employee_id=order['employee_id'],
                order_date=order['order_date'],
                required_date=order['required_date'],
                shipped_date=order['shipped_date'],
                ship_via=order['ship_via'],
                freight=order['freight'],
                ship_name=order['ship_name'],
                ship_address=order['ship_address'],
                ship_city=order['ship_city'],
                ship_region=order['ship_region'],
                ship_postal_code=order['ship_postal_code'],
                ship_country=order['ship_country']
            )
            db.session.add(new_order)
            db.session.commit()
            response = make_response({"success": "true", "message": "Order Added Successfully", "payload": new_order.as_dict()})
            response.status_code = 201
            return response
        except Exception as e:
            print(e)
            response = make_response({"success": "false", "payload": f"Failed to create new order. Error: {e}"})
            response.status_code = 404
            return response

    def update_order(self, order_id, order_data):
        try:
            order = Order.query.filter_by(order_id=order_id).first()
            if order is None:
                response = make_response({
                    "success": "false",
                    "message": "Order does not exist"
                })
                response.status_code = 404
                return response
            for key, value in order_data.items():
                if hasattr(order, key):
                    setattr(order, key, value)
            db.session.commit()
            response = make_response({
                "success": "true",
                "message": "Order details updated successfully.",
                "order": order.as_dict()
            })
            response.status_code = 202
            return response
        except Exception as e:
            db.session.rollback()
            print(f"Error while updating the data. Error: {e}")
            response = make_response({
                "success": "false",
                "message": "Failed to update order",
                "error": str(e)
            })
            response.status_code = 500
            return response


    def get_customer_order_history(self,customer_id):
        try:
            print(type(customer_id))
            order_details= Order.query.filter_by(customer_id=customer_id).all()
            if order_details is None:
                response= make_response({
                    "success":"false",
                    "message":"No customer with the given customer id"

                })
                response.status_code=404
                return response
            response=make_response({
                "success":"true",
                "message":"All orders for the given customerId fetched",
                "orders": [order.as_dict() for order in order_details]})
            response.status_code=200
            return  response
        except Exception as e:
            print(f"Error while updating the data. Error: {e}")
            response = make_response({
                "success": "false",
                "message": "Failed to fetch order for the given customer id",
                "error": str(e)})
            response.status_code = 500
            return response



