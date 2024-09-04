from src.models.product_model import Product

from flask import make_response

from src.app import db

class ProductService:
    def get_all_products(self):
        """
    Get all products
    ---
    tags:
      - Products
    """
        try:
            products= Product.query.all()
            response= make_response({"success":"true","payload":[product.as_dict() for product in products]})
            response.status_code=200
            return response
        except Exception as e:
            response= make_response({"success":"false","payload":f"Failed to fetch products. Error: {e}"})
            response.status_code=404
            return response
    
    def create_product(self,product):
        try:
            new_product= Product(product_id=product['product_id'],product_name=product['product_name'],supplier_id=product['supplier_id'],category_id=product['category_id'],quantity_per_unit=product['quantity_per_unit'],unit_price=product['unit_price'],units_in_stock=product['units_in_stock'],units_on_order=product['units_on_order'],reorder_level=product['reorder_level'],discontinued=product['discontinued'])
            db.session.add(new_product)
            db.session.commit()
            response= make_response({"success":"true","message":"Product Added Successful","payload":new_product.as_dict()})
            response.status_code=201
            return response
        except Exception as e:
            print(e)
            response= make_response({"success":"false","payload":f"Failed to create new product. Error: {e}"})
            response.status_code=404
            return response

    def update_product(self,product_id,product_data):
        try:
            print(product_id)
            product=Product.query.filter_by(product_id=product_id).first()
            if product is None:
                response= make_response({
                    "success":"false",
                    "message":"Product doesnot exist"         
                })
                response.status_code=404
                return response
            for key,value in product_data.items():
                if hasattr(product,key):
                    setattr(product,key,value)
            db.session.commit()
            response=make_response({
                "success":"true",
                "message":"Product details updated successfully.",
                "product": product.as_dict()
            })
            response.status_code=202
            return response
        except Exception as e:
            db.session.rollback()
            print(f"Error while updating the data. Error:  {e}")
            response= make_response({
                "success":"false",
                "message": "Failed to update product",
                "error":e})
            response.status_code=500
            return response
            

