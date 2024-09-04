from flask import Blueprint, request, make_response
from src.services.order_services import OrderService

order_service = OrderService()
order_bp = Blueprint('order_bp', __name__)

@order_bp.route("/orders", methods=["GET"])
def get_all_orders():
    return order_service.get_all_orders()

@order_bp.route('/orders/createOrder', methods=["POST"])
def create_order():
    order = request.get_json()
    result = order_service.create_order(order)
    return result

@order_bp.route("/orders/updateOrder", methods=["PUT"])
def update_order():
    order_id = request.args.get('order_id')
    if not order_id:
        response = make_response({"error": "Order ID is required"})
        response.status_code = 400
        return response

    data = request.get_json()
    result = order_service.update_order(order_id, data)
    return result


@order_bp.route("/orders/getCustomerOrders",methods=["POST"])
def get_customer_orders():
    customer_id= request.args.get("customer_id")
    return order_service.get_customer_order_history(customer_id)