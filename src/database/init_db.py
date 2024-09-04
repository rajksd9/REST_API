# import psycopg2
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(host='localhost',
#                             database='northwinddb',
#                             user="postgres",
#                             password="rajksd123@",port="5432")
#         print("connected to database")
#         return conn
#     except psycopg2.Error as e:
#         raise Exception("Failed to connect to database")