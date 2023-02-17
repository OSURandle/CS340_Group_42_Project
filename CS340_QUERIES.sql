-- Joshua Randle
-- Edward G Breard
-- Group 42

-- Customer Table

INSERT INTO Customers (customerFirstName, customerLastName, customerPhone, customerAddress, customerCity, customerState, customerZipcode)
VALUES (:customerFirstName, :customerLastName, :customerEmail, :customerPhone, :customerAddress, :customerCity, :customerState, :customerZipcode)


SELECT customerFirstName, customerLastName, customerPhone, customerAddress, customerCity, customerState, customerZipcode FROM Customers;


-- Boxes Table

INSERT INTO Boxes (boxType, boxPrice)
VALUES (:boxType, :boxPrice)


SELECT boxType, boxPrice from Boxes;


UPDATE Boxes


-- Distributors Table

INSERT INTO Distributors(distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice)
VALUES (:distributorName, :distributorEmail, :distributorPhone, :distributorAddress, :distributorCity, :distributorState, :distributorZipcode, :distributorProduct, :distributorPrice)

SELECT distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice FROM Disributors;

DELETE


-- Products Table

INSERT INTO Products(productPrice, productQuantity, productBoxType)
VALUES (:productPrice, :productQuantity, :productBoxType)

SELECT productPrice, productQuantity, productBoxType FROM Products;


-- Drop-down


-- Distributor_Products Table

INSERT INTO

SELECT dandpID, distributorID, productID FROM Distributor_Products;

-- Purchases Table

INSERT INTO Purchases(purchaseDate, purchaseRevenue)
VALUES (:purchaseDate, :purchaseRevenue)

SELECT purchaseDate, purchaseRevenue FROM Purchases;
