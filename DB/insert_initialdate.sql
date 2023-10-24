USE db_hotel;

-- Insert data into the "user" table
INSERT INTO user (email, password, role) VALUES
('user1@example.com', 'password1', 'CLIENT'),
('user2@example.com', 'password2', 'CLIENT'),
('manager@example.com', 'managerpassword', 'HOTEL_MANAGER');

-- Insert data into the "client" table
INSERT INTO client (address, name, phone, user_id) VALUES
('123 Main St', 'John Doe', '123-456-7890', 1),
('456 Elm St', 'Jane Smith', '987-654-3210', 2);

-- Insert data into the "pet" table
INSERT INTO pet (age, name, race, specie, client_id) VALUES
(3, 'Buddy', 'Labrador', 'Dog', 1),
(2, 'Fluffy', 'Persian', 'Cat', 2);

-- Insert data into the "room" table
INSERT INTO room (number, type, capacity, disponibility, price) VALUES
(101, 'Standard', 2, 1, 100.00),
(102, 'Deluxe', 4, 1, 150.00),
(201, 'Standard', 2, 1, 100.00),
(202, 'Deluxe', 4, 1, 150.00);
