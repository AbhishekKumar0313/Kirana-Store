# Kirana Store Management System

The **Kirana Store Management System** is a Python-based application designed to manage a small store. It provides interfaces for both customers and store owners (managers) with functionalities like product browsing, purchasing, billing, and inventory management. The application uses JSON files for data storage and pandas for converting bills to CSV format.

## Features

### Customer Interface:
- **Register/Login**: Customers can register and log in to the system.
- **Product Browsing**: Customers can view the available products with details like price and quantity.
- **Purchase**: Customers can select and purchase products, with a bill generated at the end.
- **Billing**: After purchasing products, a bill is generated, saved in JSON and CSV format.

### Owner (Manager) Interface:
- **Register/Login**: Store owners (managers) can register and log in.
- **Product Management**: Owners can add, view, update, and delete products.
- **Inventory Management**: Owners can manage store inventory by adding, modifying, and removing products.

### Data Storage:
- **JSON**: All customer, owner, and product data is stored in JSON files for persistence.
- **CSV**: Customer bills are saved as CSV files using pandas for easy record-keeping.

## Project Structure

- `Kirana.py`: Main file containing the Kirana Store system code.
- `users.json`: Stores registered customer data.
- `owner.json`: Stores registered owner data.
- `product.json`: Stores product details (id, name, price, quantity).
- `bill.json`: Temporarily stores purchase information for generating bills.
- `bill.csv`: Stores the final customer bill in CSV format.

## Installation & Setup

  1. **Clone the Repository**:
     ```bash
     git clone https://github.com/yourusername/kirana-store-management.git
     cd kirana-store-management
  2. **Import Required Libraries**:
     ```bash
      install pandas
      install os
      install os
  3. **Run the Application: Run the Python script to start the application.**:
    ```bash
      python Kirana.py

## How to Use
Customer:
  - On running the application, select Customer.
  - Login or Register if you're a new user.
  - Browse available products.
  - Select the products to purchase and enter the desired quantity.
  - Review the total bill generated and collect a CSV version of the bill.
  
   Owner (Manager):
  - Select Owner upon launching the application.
  - Login or Register if you're a new manager.
  - Add new products to the store, update existing products, view the product list, or delete       products.
  - Manage inventory as required.
  
## Screenshots
![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185713.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185724.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185736.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185748.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185805.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20185950.png)

![Alt text](https://github.com/AbhishekKumar0313/Kirana-Store/blob/main/Screenshot%202024-09-11%20190002.png)



