# CS340_Group_42_Project
Sandbox for our project



Table Relationships


Customers table has a one-to-many relationship with Purchases table. One customer can make multiple purchases, and each purchase is associated with one customer.

Boxes table has a one-to-many relationship with both Distributors and Products tables. One box can be associated with multiple distributors and products.

Distributors table has a one-to-many relationship with Distributor_Products table. One distributor can have multiple products associated with their account.

Products table has a one-to-many relationship with both Purchases and Distributor_Products tables. One product can be associated with multiple purchases and multiple distributors.

Distributor_Products table has a many-to-many relationship with Distributors and Products tables. One distributor can have multiple products associated with their account, and one product can have multiple distributors associated with it.
