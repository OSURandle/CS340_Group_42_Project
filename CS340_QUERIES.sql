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


UPDATE Boxes SET boxType = :boxTypeInput, boxPrice= :boxPriceInput, WHERE 
id= :box_ID_from_the_update_form


-- Distributors Table

INSERT INTO Distributors(distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice)
VALUES (:distributorName, :distributorEmail, :distributorPhone, :distributorAddress, :distributorCity, :distributorState, :distributorZipcode, :distributorProduct, :distributorPrice)

SELECT distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice FROM Disributors;

DELETE FROM Distributors WHERE id = :distributorID_selected_from_browse_distributor_page


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
