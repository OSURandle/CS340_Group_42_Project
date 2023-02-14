-- Joshua Randle
-- Edward G Breard
--Group 42
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

--Create or replace tables

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
    isMember tinyint(1) DEFAULT 1,
    membershipCredentialID int(10) NOT NULL,
    PRIMARY KEY(customerID),
    FOREIGN KEY(membershipCredentialID) REFERENCES Membership_Credentials(customerID)
    ON DELETE CASCADE
);

CREATE OR REPLACE TABLE Distributors(
    distributorID int(10) AUTO_INCREMENT unique NOT NULL,
    distributorName varchar(50) NOT NULL,
    distributorEmail varchar(100) NOT NULL,
    distributorPhone varchar(40) NOT NULL,
    distributorAddress varchar(100) NOT NULL,
    distributorCity varchar(50) NOT NULL,
    distributorState varchar(50) NOT NULL,
    distributorZipcode int(10) NOT NULL,
    distributorSpecialty varchar(50) NOT NULL,
    distributorPrice decimal(10,2) NOT NULL,
    PRIMARY KEY(distributorID)
);

CREATE OR REPLACE TABLE Distributor_Products(
    dandpID int NOT NULL unique AUTO_INCREMENT,
    dID int(10) NOT NULL,
    pID int(10) NOT NULL,
    PRIMARY KEY(dandpID),
    FOREIGN KEY(dID) REFERENCES Distributors(distributorID)
    ON DELETE CASCADE,
    FOREIGN KEY(pID) REFERENCES Products(productID)
    ON DELETE CASCADE
);

CREATE OR REPLACE TABLE Products(
    productID int(10) AUTO_INCREMENT unique NOT NULL,
    productPrice decimal(10,2) NOT NULL,
    productMembershipPrice decimal(10,2) NOT NULL,
    productServingSize int(2) NOT NULL,
    productBoxType varchar(50) NOT NULL,
    productMembershipFees decimal(10,2) NOT NULL,
    productSpiceBlend varchar(50) NOT NULL,
    productCookingAcc varchar(50) NOT NULL,
    PRIMARY KEY(productID)
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

CREATE OR REPLACE TABLE Membership_Credentials(
    customerID int(10) unique NOT NULL,
    hashedPwd varchar(50) NOT NULL,
    PRIMARY KEY(customerID) 
);

--Insert Data into Tables
--Need to troubleshoot membership credentials, returning 0
INSERT INTO Customers(customerFirstName, customerLastName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode, isMember, membershipCredentialID)
    VALUES('Greg', 'Abbot', 'gabb@gmail.com', '764-678-9873', '435 Looney Way', 'Houston', 'Texas', '39859', 1, (SELECT customerID FROM Membership_Credentials WHERE customerID = 1)),
    ('Courtney', 'Smith', 'csmith@gmail.com', '869-431-5465', '4357 Charity Lane', 'Salem', 'Massachusets', '85404', 1, (SELECT customerID FROM Membership_Credentials WHERE customerID = 2)),
    ('Felix', 'Harding', 'fharding@gmail.com', '687-345-0968', '235 Wallaby Way', 'Panama City', 'Florida', '38756', 1, (SELECT customerID FROM Membership_Credentials WHERE customerID = 3));

INSERT INTO Distributors(distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorSpecialty, distributorPrice)
    VALUES('Pork-R-Us', 'porker@gmail.com', '498-768-4823', '4345 Shoulder Lane', 'Vicksburg', 'Mississippi', '39768', 'Pork', 10.00),
    ('Chicken-Surplus', 'crazychick@yahoo.com', '473-584-3623', '473 Cluck Road', 'Gainesville', 'Florida', '83430', 'Chicken', 5.00),
    ('Moo-Moo-Room', 'cowmeat@hotmail.com', '483-584-3421', '892 Beefy Drive', 'Dayton', 'Georgia', '58493', 'Beef', 12.00);

INSERT INTO Distributor_Products(dID, pID)
    VALUES ((SELECT distributorID FROM Distributors WHERE distributorName = 'Pork-R-Us'), (SELECT productID FROM Products WHERE productPrice = 50.00)),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Chicken-Surplus'), (SELECT productID FROM Products WHERE productPrice = 45.00)),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Moo-Moo-Room'), (SELECT productID FROM Products WHERE productPrice = 25.00));

Insert INTO Products(productPrice, productMembershipPrice, productServingSize, productBoxType, productMembershipFees, productSpiceBlend, productCookingAcc)
    VALUES(25.00, 20.00, 5, 'Beef', 2.00, 'Steak Seasoning', 'Grill Tongs'),
    (45.00, 40.00, 8, 'Chicken', 2.00, 'Poultry Seasoning', 'Fryer Basket'),
    (50.00, 45.00, 10, 'Pork', 2.00, 'BBQ Rub', 'Basting Brush Set');

Insert INTO Purchases(customerID, productID, purchaseDate, purchaseRevenue)
    VALUES((SELECT customerID FROM Customers WHERE customerFirstName ='Greg'), (SELECT productID FROM Products WHERE productBoxType = 'Beef'), '2023-02-07', 15.00),
    ((SELECT customerID FROM Customers WHERE customerFirstName ='Courtney'), (SELECT productID FROM Products WHERE productBoxType = 'Chicken'),'2022-12-23', 20.00),
    ((SELECT customerID FROM Customers WHERE customerFirstName ='Felix'), (SELECT productID FROM Products WHERE productBoxType = 'Pork'),'2023-01-14', 30.00);

INSERT INTO Membership_Credentials(customerID, hashedPwd)
    VALUES((SELECT customerID FROM Customers where customerFirstName = 'Greg'), '483489g'),
    ((SELECT customerID FROM Customers where customerFirstName = 'Courtney'), '5jhwjw'),
    ((SELECT customerID FROM Customers where customerFirstName = 'Felix'), '8jhr54');
    
SELECT * from Customers;
SELECT * from Distributors;
SELECT * from Distributor_Products;
SELECT * from Products;
SELECT * from Purchases;
SELECT * from Membership_Credentials;

SET FOREIGN_KEY_CHECKS =1;
COMMIT;