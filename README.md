# CS340_Group_42_Project
Sandbox for our project



Table Relationships


Customers and Purchases tables have a one-to-many relationship, where one customer can make many purchases, but each purchase can only be made by one customer. The customerID field in the Purchases table is a foreign key that references the customerID field in the Customers table.

Boxes and Distributors tables have a one-to-many relationship, where one box can be sold by many distributors, but each distributor can only sell one type of box. The boxID field in the Distributors table is a foreign key that references the boxID field in the Boxes table.

Distributors and Distributor_Boxes tables have a many-to-many relationship, where one distributor can sell many boxes, and one box can be sold by many distributors. The distributorID and boxID fields in the Distributor_Boxes table are foreign keys that reference the distributorID field in the Distributors table and the boxID field in the Boxes table, respectively.

Purchases and Boxes tables have a one-to-many relationship, where one purchase can be for one type of box, but each box can be purchased many times. The boxID field in the Purchases table is a foreign key that references the boxID field in the Boxes table.

Purchases and Customers tables have a one-to-many relationship, where one purchase can be made by one customer, but each customer can make many purchases. The customerID field in the Purchases table is a foreign key that references the customerID field in the Customers table.
