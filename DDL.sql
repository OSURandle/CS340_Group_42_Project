-- Joshua Randle
-- Edward G Breard
-- Group 42
SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

-- Create or replace tables

CREATE OR REPLACE TABLE Customers(
    customerID int(10) AUTO_INCREMENT NOT NULL,
    customerName varchar(150) NOT NULL,
    customerEmail varchar(100) NULL,
    customerPhone varchar(40) NULL,
    customerAddress varchar(100) NOT NULL,
    customerCity varchar(50) NOT NULL,
    customerState varchar(50) NOT NULL,
    customerZipcode varchar(10) NULL,
    PRIMARY KEY(customerID)
);

CREATE OR REPLACE TABLE Boxes (
    boxID INT(10) AUTO_INCREMENT NOT NULL,
    boxType VARCHAR(50) NOT NULL UNIQUE,
    boxPrice decimal(10,2) NOT NULL,
    PRIMARY KEY(boxID)
);

CREATE OR REPLACE TABLE Distributors(
    distributorID int(10) AUTO_INCREMENT NOT NULL,
    boxID int(10) NOT NULL,
    distributorName varchar(50) NOT NULL,
    distributorEmail varchar(100) NULL,
    distributorPhone varchar(40) NULL,
    distributorAddress varchar(100) NOT NULL,
    distributorCity varchar(50) NOT NULL,
    distributorState varchar(50) NOT NULL,
    distributorZipcode int(10) NULL,
    distributorPrice decimal(10,2) NOT NULL,
    PRIMARY KEY(distributorID),
    FOREIGN KEY (boxID) REFERENCES Boxes(boxID)
    ON DELETE CASCADE
);


CREATE OR REPLACE TABLE Distributor_Boxes(
    dandbID int NOT NULL AUTO_INCREMENT,
    distributorID INT(10) NULL,
    boxID INT(10) NULL,
    PRIMARY KEY(dandbID),
    FOREIGN KEY(distributorID) REFERENCES Distributors(distributorID)
    ON DELETE CASCADE,
    FOREIGN KEY(boxID) REFERENCES Boxes(boxID)
    ON DELETE CASCADE
);

CREATE OR REPLACE TABLE Purchases(
    purchaseID int(10) AUTO_INCREMENT NOT NULL,
    customerID int(10) NOT NULL,
    boxID int(10) NOT NULL,
    purchaseDate datetime NOT NULL,
    purchaseRevenue decimal (10,2) NOT NULL,
    PRIMARY KEY(purchaseID),
    FOREIGN KEY(boxID) REFERENCES Boxes(boxID)
    ON DELETE CASCADE,
    FOREIGN KEY(customerID) REFERENCES Customers(customerID)
    ON DELETE CASCADE
);

-- Insert Data into Tables
INSERT INTO Customers(customerName, customerEmail, customerPhone, customerAddress, customerCity, customerState, customerZipcode)
    VALUES('Greg Abbot', 'gabb@gmail.com', '764-678-9873', '435 Looney Way', 'Houston', 'Texas', '39859'),
    ('Courtney Smith', 'csmith@gmail.com', '869-431-5465', '4357 Charity Lane', 'Salem', 'Massachusets', '85404'),
    ('Felix Harding', 'fharding@gmail.com', '687-345-0968', '235 Wallaby Way', 'Panama City', 'Florida', '38756');

INSERT INTO Boxes(boxType, boxPrice)
    VALUES('Lean Meats', 30.00),
    ('Seafood', 40.00),
    ('Veggie', 25.00),
    ('Fruit', 25.00),
    ('Nuts and Seeds', 20.00);

INSERT INTO Distributors(boxID, distributorName, distributorEmail, distributorPhone, distributorAddress, distributorCity, distributorState, distributorZipcode, distributorPrice)
    VALUES((SELECT boxID from Boxes WHERE boxType = 'Lean Meats'),'Farmer Jack', 'leaner@gmail.com', '498-768-4823', '4345 Shoulder Lane', 'Vicksburg', 'Mississippi', '39768', 10.00),
    ((SELECT boxID from Boxes WHERE boxType = 'Fruit'), 'Fruit-Surplus', 'crazyfruit@yahoo.com', '473-584-3623', '473 Cluck Road', 'Gainesville', 'Florida', '83430', 5.00),
    ((SELECT boxID from Boxes WHERE boxType = 'Nuts and Seeds'), 'Nut-and-Seed-Palace', 'buckwheat@hotmail.com', '483-584-3421', '892 Seedy Drive', 'Dayton', 'Georgia', '58493', 12.00);


INSERT INTO Distributor_Boxes(distributorID, boxID)
    VALUES ((SELECT distributorID FROM Distributors WHERE distributorName = 'Farmer Jack'), (SELECT boxID FROM Boxes WHERE boxType = 'Nuts and Seeds')),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Farmer Jack'), (SELECT boxID FROM Boxes WHERE boxType = 'Fruit')),
    ((SELECT distributorID FROM Distributors WHERE distributorName = 'Nut-and-Seed-Palace'), (SELECT boxID FROM Boxes WHERE boxType = 'Lean Meats'));
    
Insert INTO Purchases(customerID, boxID, purchaseDate, purchaseRevenue)
    VALUES((SELECT customerID FROM Customers WHERE customerName ='Greg Abbot'), (SELECT boxID FROM Boxes WHERE boxType = 'Nuts and Seeds'), '2023-02-07', 15.00),
    ((SELECT customerID FROM Customers WHERE customerName ='Courtney Smith'), (SELECT boxID FROM Boxes WHERE boxType = 'Lean Meats'),'2022-12-23', 20.00),
    ((SELECT customerID FROM Customers WHERE customerName ='Felix Harding'), (SELECT boxID FROM Boxes WHERE boxType = 'Fruit'),'2023-01-14', 30.00);

    


SET FOREIGN_KEY_CHECKS =1;
COMMIT;
