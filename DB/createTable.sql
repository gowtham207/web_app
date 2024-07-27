-- Create users table with additional fields
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Insert data into users table
INSERT INTO users (fname, lname, email, password, created_at, deleted_at, updated_at) 
VALUES 
    ('John', 'Doe', 'johndoe@example.com', 'Password@123', '2023-01-01 10:00:00', NULL, '2023-01-01 10:00:00'),
    ('Jane', 'Smith', 'janesmith@example.com', 'Password@123', '2023-01-02 11:00:00', NULL, '2023-01-02 11:00:00'),
    ('Alice', 'Johnson', 'alicejohnson@example.com', 'Password@123', '2023-01-03 12:00:00', NULL, '2023-01-03 12:00:00'),
    ('Bob', 'Brown', 'bobbrown@example.com', 'Password@123', '2023-01-04 13:00:00', NULL, '2023-01-04 13:00:00'),
    ('Charlie', 'Davis', 'charliedavis@example.com', 'Password@123', '2023-01-05 14:00:00', NULL, '2023-01-05 14:00:00');

-- Create product table
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    product_name TEXT,
    price TEXT,
    image TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Insert data into product table
INSERT INTO product (product_name, price, created_at, deleted_at, updated_at)
VALUES 
    ('Product 1', '10.00', '2023-01-01 10:00:00', NULL, '2023-01-01 10:00:00'),
    ('Product 2', '20.00', '2023-01-02 11:00:00', NULL, '2023-01-02 11:00:00'),
    ('Product 3', '30.00', '2023-01-03 12:00:00', NULL, '2023-01-03 12:00:00'),
    ('Product 4', '40.00', '2023-01-04 13:00:00', NULL, '2023-01-04 13:00:00'),
    ('Product 5', '50.00', '2023-01-05 14:00:00', NULL, '2023-01-05 14:00:00');



-- Create product table with corrected syntax
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    image_url TEXT,
    brand VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);


-- Insert sample products into the product table
INSERT INTO product (product_name, description, price, stock_quantity, image_url, brand, created_at, updated_at)
VALUES 
    ('Laptop', 'A high-performance laptop with 16GB RAM and 512GB SSD.', 999.99, 10, 'https://example.com/images/laptop.jpg', 'TechBrand', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Smartphone', 'Latest model with a 6.5-inch display and 128GB storage.', 499.99, 25, 'https://example.com/images/smartphone.jpg', 'MobileCo', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Headphones', 'Noise-cancelling wireless headphones with long battery life.', 149.99, 50, 'https://example.com/images/headphones.jpg', 'AudioX', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Smartwatch', 'Smartwatch with fitness tracking and heart rate monitoring.', 199.99, 30, 'https://example.com/images/smartwatch.jpg', 'FitLife', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Camera', 'Digital camera with 4K video recording and 20MP resolution.', 799.99, 15, 'https://example.com/images/camera.jpg', 'PhotoPro', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
