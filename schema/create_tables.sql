-- ============================================
-- RetailPulse — Database Schema
-- ============================================

-- ────────────────────────────────────────────
-- Table: customers
-- Stores customer demographic information
-- ────────────────────────────────────────────
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    city VARCHAR(50),
    state VARCHAR(50),
    registration_date DATE
);

-- ────────────────────────────────────────────
-- Table: products
-- Stores product catalog with categories
-- ────────────────────────────────────────────
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0
);

-- ────────────────────────────────────────────
-- Table: employees
-- Stores sales team information
-- ────────────────────────────────────────────
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hire_date DATE
);

-- ────────────────────────────────────────────
-- Table: orders
-- Stores order headers linked to customers
-- and handling employees
-- ────────────────────────────────────────────
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- ────────────────────────────────────────────
-- Table: order_items
-- Stores individual line items for each order
-- ────────────────────────────────────────────
CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ────────────────────────────────────────────
-- Table: payments
-- Stores payment details for each order
-- ────────────────────────────────────────────
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
