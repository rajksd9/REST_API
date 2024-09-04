# from app import app
# from models.product_model import product_model

# productObj= product_model()

# @app.route("/products/getAllProducts")
# def getProduct():
#     return productObj.getAllProducts()
    
# @app.route("/product:id")
# def createProduct():
#     return ""


from flask import Blueprint, request, make_response
from src.services.product_services import ProductService

product_service=ProductService()
product_bp= Blueprint('product_bp',__name__)

@product_bp.route("/products",methods=["GET"])
def get_all_products():
    return product_service.get_all_products()


@product_bp.route('/products/createProduct',methods=["POST"])
def create_product():
    product=request.get_json()
    result= product_service.create_product(product)
    return result

@product_bp.route("/products/updateProduct",methods=["PUT"])
def update_product():
    product_id=request.args.get('product_id')
    if not product_id:
        response= make_response({"error": "Product ID is required"})
        response.status_code=400
        return response

    data = request.get_json()
    result = product_service.update_product(product_id, data)
    return result

