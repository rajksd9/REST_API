# import logging
# from flask import Flask,request,make_response
# # from database.init_db import get_db_connection
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask_swagger_ui import get_swaggerui_blueprint




# #setting up logger
# logging.basicConfig(filename="src/logs/applog.log", format='%(asctime)s %(message)s', filemode='a')   

# app = Flask(__name__)  
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rajksd123%40@localhost:5432/northwinddb'

# CORS(app)
# db=SQLAlchemy(app)

# app.logger.setLevel(logging.INFO)



# #swagger setup
# SWAGGER_URL="/swagger"
# API_URL="/static/swagger.json"

# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': 'Access API'
#     }
# )







# @app.before_request
# def before_request():
#     app.logger.info(f'Incoming request to {request.path}')

# @app.after_request
# def after_request(response):
#     app.logger.info(f'Completed request to {request.path} with status {response.status}')
#     return response

# @app.route("/")
# def base_url():
#     response = make_response({
#         "success":"true",
#         "message":"The backend server is up and running."
#     })
#     response.status_code=200
#     return  response

# from src.controller.customer_controller import customer_bp
# app.register_blueprint(customer_bp)
# from src.controller.product_controller import product_bp
# app.register_blueprint(product_bp)
# from src.controller.order_controller import order_bp
# app.register_blueprint(order_bp)
# #swagger blueprint
# app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)



# if __name__ == "__main__":
#     app.run(debug=True)


# # import controller.product_controller as product_controller
# # import controller.customer_controller as customer_controller

import logging
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

# Initialize extensions
db = SQLAlchemy()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rajksd123%40@localhost:5432/northwinddb'
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Setting up logger
    logging.basicConfig(filename="src/logs/applog.log", format='%(asctime)s %(message)s', filemode='a')   
    app.logger.setLevel(logging.INFO)

    @app.before_request
    def before_request():
        app.logger.info(f'Incoming request to {request.path}')

    @app.after_request
    def after_request(response):
        app.logger.info(f'Completed request to {request.path} with status {response.status}')
        return response

    @app.route("/")
    def base_url():
        response = make_response({
            "success": "true",
            "message": "The backend server is up and running."
        })
        response.status_code = 200
        return response

    # Register blueprints
    register_blueprints(app)

    # Swagger setup
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Access API'
        }
    )

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app

def register_blueprints(app):
    from src.controller.customer_controller import customer_bp
    from src.controller.product_controller import product_bp
    from src.controller.order_controller import order_bp
    
    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
