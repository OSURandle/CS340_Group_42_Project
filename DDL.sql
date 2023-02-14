-- Joshua Randle
-- Edward G Breard
-- Group 42
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

-- Create or replace tables

CREATE OR REPLACE TABLE Customers(
    customerID int(10) AUTO_INCREMENT unique NOT NULL,
    customerFirstName varchar(50) NOT NULL,
    customerLastName varchar(50) NOT NULL,
    customerEmail varchar(100) NOT NULL,
    customerPhone varchar(40) NOT NULL,
    customerAddress varchar(100) NOT NULL,
    customerCity varchar(50) NOT NULL,
    customerState varchar(50) NOT NULL,
    customerZipcode varchar(10) NOT NULL,
    PRIMARY KEY(customerID)
);

CREATE OR REPLACE TABLE Boxes (
    boxID INT(10) AUTO_INCREMENT UNIQUE NOT NULL,
    boxType VARCHAR(50) NOT NULL,
    boxPrice decimal(10,2) NOT NULL,
    PRIMARY KEY(boxID)
);

CREATE OR REPLACE TABLE Distributors(
    distributorID int(10) AUTO_INCREMENT unique NOT NULL,
    boxID int(10) NOT NULL,
    distributorName varchar(50) NOT NULL,
    distributorEmail varchar(100) NOT NULL,
    distributorPhone varchar(40) NOT NULL,
    distributorAddress varchar(100) NOT NULL,
    distributorCity varchar(50) NOT NULL,
    distributorState varchar(50) NOT NULL,
    distributorZipcode int(10) NOT NULL,
    distributorProduct varchar(50) NOT NULL,
    distributorPrice decimal(10,2) NOT NULL,
    PRIMARY KEY(distributorID),
    FOREIGN KEY (boxID) REFERENCES Boxes(boxID)
);

CREATE OR REPLACE TABLE Products(
    productID int(10) AUTO_INCREMENT unique NOT NULL,
    boxID int(10) NOT NULL,
    productPrice decimal(10,2) NOT NULL,
    productQuantity int(2) NOT NULL,
    productBoxType varchar(50) NOT NULL,
    PRIMARY KEY(productID),
    FOREIGN KEY (boxID) REFERENCES Boxes(boxID)
);

CREATE OR REPLACE TABLE Distributor_Products(
    dandpID int NOT NULL unique AUTO_INCREMENT,
    distributorID INT(10) NOT NULL,
    productID INT(10) NOT NULL,
    PRIMARY KEY(dandpID),
    FOREIGN KEY(distributorID) REFERENCES Distributors(distributorID)
    ON DELETE CASCADE,
    FOREIGN KEY(productID) REFERENCES Products(productID)
    ON DELETE CASCADE
);

CREATE OR REPLACE TABLE Purchases(
    customerID int(10) NOT NULL,
    productID int(10) NOT NULL,
    purchaseID int(10) AUTO_INCREMENT unique NOT NULL,
    purchaseDate datetime NOT NULL,
    purchaseRevenue decimal (10,2) NOT NULL,
    PRIMARY KEY(purchaseID),
    FOREIGN KEY(productID) REFERENCES Products(productID),
    FOREIGN KEY(customerID) REFERENCES Customers(customerID)
    ON DELETE CASCADE
);

--Insert Data into Tables
--Need to troubleshoot membership credentials, returning 0
INSERT INTO Customers(customerFirstName, customerLastName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode)
    VALUES('Greg', 'Abbot', 'gabb@gmail.com', '764-678-9873', '435 Looney Way', 'Houston', 'Texas', '39859'),
    ('Courtney', 'Smith', 'csmith@gmail.com', '869-431-5465', '4357 Charity Lane', 'Salem', 'Massachusets', '85404'),
    ('Felix', 'Harding', 'fharding@gmail.com', '687-345-0968', '235 Wallaby Way', 'Panama City', 'Florida', '38756');

INSERT INTO Boxes(boxType, boxPrice)
    VALUES('Lean Meats', 30.00),
    ('Seafood', 40.00),
    ('Veggie', 25.00),
    ('Fruit', 25.00),
    ('Nuts and Seeds', 20.00);

INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorProduct, distributorPrice)
    VALUES((SELECT boxID from Boxes WHERE boxType = 'Lean Meats'),'Farmer Jack', 'leaner@gmail.com', '498-768-4823', '4345 Shoulder Lane', 'Vicksburg', 'Mississippi', '39768', (SELECT boxType FROM Boxes WHERE boxID = 1), 10.00),
    ((SELECT boxID from Boxes WHERE boxType = 'Fruit'), 'Fruit-Surplus', 'crazyfruit@yahoo.com', '473-584-3623', '473 Cluck Road', 'Gainesville', 'Florida', '83430', (SELECT boxType FROM Boxes WHERE boxID = 4), 5.00),
    ((SELECT boxID from Boxes WHERE boxType = 'Nuts and Seeds'), 'Nut-and-Seed-Palace', 'buckwheat@hotmail.com', '483-584-3421', '892 Seedy Drive', 'Dayton', 'Georgia', '58493', (SELECT boxType FROM Boxes WHERE boxID = 5), 12.00);



Insert INTO Products(boxID, productPrice, productQuantity, productBoxType)
    VALUES((SELECT boxID from Boxes WHERE boxType = 'Lean Meats'), 25.00, 5, (SELECT boxType from Boxes WHERE boxID = 1)),
    ((SELECT boxID from Boxes WHERE boxType = 'Nuts and Seeds'), 45.00, 8, (SELECT boxType from Boxes WHERE boxID = 5)),
    ((SELECT boxID from Boxes WHERE boxType = 'Fruit'), 50.00, 10, (SELECT boxType from Boxes WHERE boxID = 4));

INSERT INTO Distributor_Products(distributorID, productID)
    VALUES ((SELECT distributorID FROM Distributors WHERE distributorName = 'Farmer Jack'), (SELECT productID FROM Products WHERE productBoxType = 'Nuts and Seeds')),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Farmer Jack'), (SELECT productID FROM Products WHERE productBoxType = 'Fruit')),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Nut-and-Seed-Palace'), (SELECT productID FROM Products WHERE productBoxType = 'Lean Meats'));
    
Insert INTO Purchases(customerID, productID, purchaseDate, purchaseRevenue)
    VALUES((SELECT customerID FROM Customers WHERE customerFirstName ='Greg'), (SELECT productID FROM Products WHERE productBoxType = 'Nuts and Seeds'), '2023-02-07', 15.00),
    ((SELECT customerID FROM Customers WHERE customerFirstName ='Courtney'), (SELECT productID FROM Products WHERE productBoxType = 'Lean Meats'),'2022-12-23', 20.00),
    ((SELECT customerID FROM Customers WHERE customerFirstName ='Felix'), (SELECT productID FROM Products WHERE productBoxType = 'Fruit'),'2023-01-14', 30.00);

    
SELECT * from Customers;
SELECT * from Boxes;
SELECT * from Distributors;
SELECT * from Products;
SELECT * from Distributor_Products;
SELECT * from Purchases;


SET FOREIGN_KEY_CHECKS =1;
COMMIT;
