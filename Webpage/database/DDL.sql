-- Joshua Randle
-- Edward G Breard
-- Group 42

-- READ/SELECT Statements

-- Customers 
SELECT customerID, customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode FROM Customers;

-- Boxes
SELECT boxID, boxType, boxPrice FROM Boxes;

-- Distributors
SELECT Distributors.distributorID, Boxes.boxType AS boxType, distributorName, distributorEmail, DistributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice FROM Distributors INNER JOIN Boxes ON Distributors.boxID = Boxes.boxID;

-- Distributor_Boxes
SELECT Distributor_Boxes.dandbID, Distributors.distributorName AS Distributor, Boxes.boxType AS boxType FROM Distributor_Boxes INNER JOIN Distributors ON Distributor_Boxes.distributorID = Distributors.distributorID INNER JOIN Boxes ON Distributor_Boxes.boxID = Boxes.boxID;

-- Purchases
SELECT Purchases.purchaseID, Customers.customerName AS customerName, Boxes.boxType AS boxType, purchaseDate, purchaseRevenue FROM Purchases INNER JOIN Customers ON Purchases.customerID = Customers.customerID INNER JOIN Boxes ON Purchases.boxID = Boxes.boxID;


-- CREATE Statements

-- Customers
INSERT INTO Customers(customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode)
VALUES (:customerName_input, :customerEmail_input, :customerPhone_input, :customerAddress_input, :customerCity_input, :customerState_input, :customerZipcode_input);

-- Boxes
INSERT INTO Boxes(boxType, boxPrice)
VALUES (:boxType_input, :boxPrice_input);

-- Distributors
INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice)
VALUES (:boxID_dropdown_input, :distributorName_input, :distributorEmail_input, :distributorPhone_input, :distributorAddress_input, :distributorCity_input, :distributorState_input, :distributorZipcode_input, :distributorPrice_input);

-- Distributor_Boxes
INSERT INTO Distributor_Boxes(distributorID, boxID)
VALUES (:distributorID_input, :boxID_dropdown_input);

-- Purchases
INSERT INTO Purchases(customerID, boxID, purchaseDate, purchaseRevenue)
VALUES (:customerID_input, :boxID_dropdown_input, :purchaseDate_input, :purchaseRevenue_input)


-- UPDATE Customers
UPDATE Customers
SET customerName = :customerName_input, customerEmail = :customerEmail_input, customerPhone = :customerPhone_input, customerAddress = :customerAddress_input, customerCity = :customerCity_input, customerState = :customerState_input, customerZipcode = :customerZipcode_input
WHERE customerID = :customerID_update_input;

-- UPDATE Distributor_Boxes
UPDATE Distributor_Boxes
SET distributorID = :distributorID_input, boxID = :boxID_dropdown_input
WHERE dandbID = :dandbID_input;

-- DELETE Distributors
DELETE FROM Distributors WHERE distributorID = :distributorID_user_selected_input;

-- DELETE Distributor_Boxes
DELETE FROM Distributor_Boxes WHERE dandbID = :dandbID_user_selected_input;

-- DELETE Customers
DELETE FROM Customers WHERE customerID = :customerID_user_selected_input;

-- DELETE Boxes
DELETE FROM Boxes WHERE boxID = :boxID_user_selected_input;

-- DELETE Purchases
DELETE FROM Purchases WHERE purchaseID = :purchaseID_user_selected_input;

-- DropDown Boxes
SELECT boxID, boxType FROM Boxes;

-- DropDown Distributors
SELECT distributorID, distributorName FROM Distributors;

-- DropDown Customers
SELECT customerID, customerName FROM Customers;