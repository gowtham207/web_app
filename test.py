import mysql.connector
from mysql.connector import Error

def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='database-1.ccnffyqoutvy.us-east-1.rds.amazonaws.com',        # e.g., 'localhost'
            database='app_database', # e.g., 'test_db'
            user='admin',         # e.g., 'root'
            password='postgres'  # e.g., 'password123'
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()

            # cursor.execute("drop table product")

            # quer = "CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(255) NOT NULL, description TEXT, price DECIMAL(10, 2) NOT NULL, stock_quantity INT DEFAULT 0, image_url TEXT, brand VARCHAR(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, deleted_at TIMESTAMP NULL DEFAULT NULL);"
            # data = cursor.execute(quer)

            # # query=  f"INSERT I
            
            # insert_query = """
            # INSERT INTO product (product_name, description, price, stock_quantity, image_url, brand, created_at, updated_at) 
            # VALUES 
            #     ('Laptop', 'A high-performance laptop with 16GB RAM and 512GB SSD.', 999.99, 10, 'laptop.jpg', 'TechBrand', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
            #     ('Smartphone', 'Latest model with a 6.5-inch display and 128GB storage.', 499.99, 25, 'mobile.jpeg', 'MobileCo', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
            #     ('Headphones', 'Noise-cancelling wireless headphones with long battery life.', 149.99, 50, 'headphone.jpg', 'AudioX', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
            #     ('Smartwatch', 'Smartwatch with fitness tracking and heart rate monitoring.', 199.99, 30, 'watch.jpeg', 'FitLife', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
            #     ('Camera', 'Digital camera with 4K video recording and 20MP resolution.', 799.99, 15, 'camera.jpeg', 'PhotoPro', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
            # """
            # cursor.execute(insert_query)
            # connection.commit()

            # cursor.execute('SELECT * FROM product;')
            # results = cursor.fetchall()
            # for row in results:
            #     print(row)

            # print("Connected to MySQL Server version ", db_info)
            # cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            # print("You're connected to database: ", record)

            # cursor = connection.cursor()
            # # SQL command to create a new database
            # # create_db_query = f"CREATE DATABASE app_database;"
            # # cursor.execute(create_db_query)
            # print(f"Database created successfully.")
            # cursor = connection.cursor()


            # usr_query = f"CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, role VARCHAR(50) DEFAULT 'user', status VARCHAR(50) DEFAULT 'active', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, deleted_at TIMESTAMP NULL DEFAULT NULL, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"

            # cursor.execute(usr_query)

            # quer= f"select * from users"

            # cursor.execute(quer)

            # quer = "CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(255) NOT NULL, description TEXT, price DECIMAL(10, 2) NOT NULL, stock_quantity INT DEFAULT 0, image_url TEXT, brand VARCHAR(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, deleted_at TIMESTAMP NULL DEFAULT NULL);"
            # cursor.execute(quer)
            # quer= f"select * from product"
            # cursor.execute(quer)

            # cursor.execute(quer)

            # result = cursor.fetchall()

            # query=  f"INSERT INTO product (product_name, description, price, stock_quantity, image_url, brand, created_at, updated_at) VALUES ('Laptop', 'A high-performance laptop with 16GB RAM and 512GB SSD.', 999.99, 10, 'https://example.com/images/laptop.jpg', 'TechBrand', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Smartphone', 'Latest model with a 6.5-inch display and 128GB storage.', 499.99, 25, 'https://example.com/images/smartphone.jpg', 'MobileCo', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Headphones', 'Noise-cancelling wireless headphones with long battery life.', 149.99, 50, 'https://example.com/images/headphones.jpg', 'AudioX', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Smartwatch', 'Smartwatch with fitness tracking and heart rate monitoring.', 199.99, 30, 'https://example.com/images/smartwatch.jpg', 'FitLife', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Camera', 'Digital camera with 4K video recording and 20MP resolution.', 799.99, 15, 'https://example.com/images/camera.jpg', 'PhotoPro', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            # cursor.execute(query)
            # result = cursor.fetchall()
            # for row in result:
            #     print(row)

            # quer= f"select * from product"

            # cursor.execute(quer)

            # result = cursor.fetchall()
            # print(result)

            # query = f"INSERT INTO product (product_name, description, price, stock_quantity, image_url, brand, created_at, updated_at) VALUES ('Laptop', 'A high-performance laptop with 16GB RAM and 512GB SSD.', 999.99, 10, 'https://example.com/images/laptop.jpg', 'TechBrand', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Smartphone', 'Latest model with a 6.5-inch display and 128GB storage.', 499.99, 25, 'https://example.com/images/smartphone.jpg', 'MobileCo', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Headphones', 'Noise-cancelling wireless headphones with long battery life.', 149.99, 50, 'https://example.com/images/headphones.jpg', 'AudioX', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Smartwatch', 'Smartwatch with fitness tracking and heart rate monitoring.', 199.99, 30, 'https://example.com/images/smartwatch.jpg', 'FitLife', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), ('Camera', 'Digital camera with 4K video recording and 20MP resolution.', 799.99, 15, 'https://example.com/images/camera.jpg', 'PhotoPro', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            # cursor.execute(query)

            # quer= f"select * from product"

            # cursor.execute(quer)
            # result = cursor.fetchall()
            # print(result)


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_database()
