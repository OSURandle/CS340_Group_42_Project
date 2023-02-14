# CS340_Group_42_Project
Sandbox for our project

Currently based on 2nd commit

Table Relationships
Customers and Purchases have a 1:M relationship, where a customer can have many purchases but a purchase is associated with only one customer. This is implemented with the customerID as a foreign key inside the Purchases table.

Boxes and Distributors have a 1:1 relationship, where a box is associated with only one distributor and a distributor is associated with only one box. This is implemented with the boxID as a foreign key inside the Distributors table.

Boxes and Products have a 1:1 relationship, where a box is associated with only one product and a product is associated with only one box. This is implemented with the boxID as a foreign key inside the Products table.

Distributors and Products have a M:N relationship, where a distributor can supply many products and a product can be supplied by many distributors. This is implemented with a junction table, Distributor_Products, which contains the foreign keys of both the Distributors and Products tables.

Distributors and Boxes have a 1:1 relationship, where a box is associated with only one distributor and a distributor is associated with only one box. This is implemented with the boxID as a foreign key inside the Distributors table.

Products and Purchases have a M:1 relationship, where many purchases can be associated with a single product, and a product can be associated with many purchases. This is implemented with the productID as a foreign key inside the Purchases table.
