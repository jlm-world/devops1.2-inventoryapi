CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INTEGER NOT NULL
);

INSERT INTO products (name, price, quantity)
VALUES
    ('Laptop', 75000, 5),
    ('Keyboard', 2500, 10),
    ('Mouse', 1200, 15)
ON CONFLICT DO NOTHING;
