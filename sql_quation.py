## Question 1
# Problem: Create a Customers table / collection with the following fields: id (unique identifier), name, email, address, and phone_number.


# CREATE TABLE Customers (
#   id INT PRIMARY KEY AUTO_INCREMENT,
#   name VARCHAR(255),
#   email VARCHAR(255),
#   address VARCHAR(255),
#   phone_number VARCHAR(20)
# );



# Question 2

# Problem: Insert five rows / documents into the Customers table / collection with data of your choice.



# INSERT INTO Customers (name, email, address, phone_number)
# VALUES
#   ('John Doe', 'johndoe@example.com', '123 Main St', '1234567890'),
#   ('Jane Smith', 'janesmith@example.com', '456 Elm St', '0987654321'),
#   ('Mike Johnson', 'mikejohnson@example.com', '789 Oak St', '9876543210'),
#   ('Sarah Williams', 'sarahwilliams@example.com', '321 Pine St', '0123456789'),
#   ('David Lee', 'davidlee@example.com', '654 Maple St', '9876540123');





# Question 3

# Problem: Write a query to fetch all data from the Customers table / collection.


# SELECT * FROM Customers;





# Question 4

# Problem: Write a query to select only the name and email fields for all customers.


# SELECT name, email FROM Customers;




# Question 5

# Problem: Write a query to fetch the customer with the id of 3.


# SELECT * FROM Customers WHERE id = 3;



# Question 6

# Problem: Write a query to fetch all customers whose name starts with 'A'.


# SELECT * FROM Customers WHERE name LIKE 'A%';




# Question 7

# Problem: Write a query to fetch all customers, ordered by name in descending order.

# SELECT * FROM Customers ORDER BY name DESC;




# Question 8

# - **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.


# UPDATE Customers SET address = 'New Address' WHERE id = 4;




# Question 9

# Problem: Write a query to fetch the top 3 customers when ordered by id in ascending order.


# SELECT * FROM Customers ORDER BY id ASC LIMIT 3;


# Question 10

# Problem: Write a query to delete the customer with id 2.

# DELETE FROM Customers WHERE id = 2;



# Question 11

# Problem: Write a query to count the number of customers.

# SELECT COUNT(*) FROM Customers;


# Question 12

# Problem: Write a query to fetch all customers except the first two when ordered by id in ascending order.


# SELECT * FROM Customers ORDER BY id ASC OFFSET 2;



# Question 13

# Problem: Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.


# SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';




# Question 14

# Problem: Write a query to fetch all customers whose id is less than 3 or name ends with 's'.


# SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';



# Question 15

# Problem: Write a query to fetch all customers where the phone_number field is not set or is null.

# SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';





