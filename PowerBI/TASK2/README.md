# Power BI Dashboard Documentation TASK 2

## 1. Introduction

### Purpose
The purpose of this dashboard is to visualize and analyze customer data from three workbooks (Bank details, Bank details 1.1, and Bank Details 1.2). It aims to provide insights into the customer base, gender distribution, global presence, bank balances, and monthly balance trends by region.

### Audience
The intended audience for this dashboard includes bank analysts, management, and stakeholders who need insights into the customer demographics and financial statistics across different regions.

## 2. Dashboard Structure

### Pages/Tabs
1. **Overview**: Summary of key metrics and insights.
2. **Customer Analysis**: Detailed analysis of customer demographics and balances.
3. **Balance Trends**: Visualization of monthly balance trends.

### Page Descriptions
- **Overview**: Provides a high-level summary of customer demographics and financial data.
- **Customer Analysis**: Contains detailed tables and charts for region-wise customer numbers, gender distribution, and bank balances.
- **Balance Trends**: Displays the region-wise monthly balance availability trends.

## 3. Data Sources

### Source Overview
- **Bank details**: Workbook containing customer information and bank balances.
- **Bank details 1.1**: Workbook with additional customer information and demographic data.
- **Bank Details 1.2**: Workbook uploaded to Google Drive with further customer details and financial statistics.

### Connection Details
- **Bank details** and **Bank details 1.1** are imported directly into Power BI.
- **Bank Details 1.2** is accessed from Google Drive.

## 4. Data Preparation

### Data Cleaning/Transformation
- Import and transform the "Bank details" and "Bank details 1.1" workbooks into Power BI.
- Upload the "Bank Details 1.2" workbook to Google Drive and connect to it from Power BI.
- Necessary transformations include:
  - Removing any empty rows.
  - Ensuring the data types for each column are correctly set.
  - Creating relationships among the three workbooks based on common keys (e.g., Customer ID, Region).

### Data Model
- **Tables**: "Bank details," "Bank details 1.1," "Bank Details 1.2."
- **Relationships**: Establish relationships among the tables using common keys.
- **Calculated Columns/Measures**: Calculated columns or measures for aggregated customer counts and financial metrics.

## 5. Visualizations

### Visual Types
1. **Table**: For region-wise number of customers.
2. **Table**: For region-wise number of male and female customers.
3. **Map Chart**: For customer presence throughout the world based on the region-wise customer base.
4. **Bar Chart**: For region-wise customer bank balances.
5. **Line & Stacked Column Chart**: For region-wise monthly balance availability trends.

### Visual Descriptions

- **Region-wise Number of Customers Table**: Shows the number of customers in each region.

  ![S5](https://github.com/user-attachments/assets/67073ced-f5f4-464f-835f-f7669be027a1)


- **Region-wise Number of Male and Female Customers Table**: Displays the gender distribution of customers by region.

  ![SD4](https://github.com/user-attachments/assets/cb43316a-f0cf-453c-b2cd-643108a2159c)


- **Customer Presence Map Chart**: Visualizes the global distribution of customers based on their region.

  ![SD(1)](https://github.com/user-attachments/assets/03d3c804-cf52-48d4-a9ac-65403f2495a8)


- **Region-wise Customer Bank Balances Bar Chart**: Represents the total bank balances for customers in each region.

  ![SD5](https://github.com/user-attachments/assets/fb13724a-265a-42eb-a098-67570c4214b7)

  
- **Region-wise Monthly Balance Trends Line & Stacked Column Chart**: Shows the trends in monthly balance availability across different regions.

   ![SD6](https://github.com/user-attachments/assets/bf05ce37-c78c-46ce-a79e-f1c7e9589be3)
 

# Power BI Dashboard Documentation TASK 2 PART 2

## 1. Introduction

### Purpose
The purpose of this dashboard is to analyze sales data, specifically focusing on overall profit percentage, commission, work shifts of sales representatives, and trends. The goal is to identify areas for further improvement in business product sales.

### Audience
The intended audience for this dashboard includes sales managers, business analysts, and stakeholders who need insights into sales performance and work shifts of sales representatives.

## 2. Data Sources

### Source Overview
- **Sales Data File**: An Excel workbook containing detailed sales data, including sales representatives, profit, commission, and work shifts.

### Connection Details
- The data is loaded directly from the provided Sales Data file using Power BI's data import functionality.

## 3. Data Preparation

### Data Cleaning/Transformation
- Import and transform the data from the Sales Data file into Power BI.
- Necessary transformations include:
  - Removing any empty rows.
  - Ensuring the data types for each column are correctly set.
  - Calculating profit percentage and commission for each sales representative.

### Data Model
- **Tables**: The primary table used is the "Sales Data" table.
- **Calculated Columns/Measures**:
  - **Profit Percentage**: (Total Profit / Total Sales) * 100

## 4. Visualizations

### Visual Types
1. **Table**: For overall profit percentage and commission for sales against each sales representative.
2. **Table**: For sales representative-wise total number of work shifts (monthly basis) and work shifts (day & night) trends.

### Visual Descriptions

- **Overall Profit Percentage and Commission Table**: Displays the profit percentage and commission for each sales representative.

  ![SD(2)](https://github.com/user-attachments/assets/1b289a7b-32ea-4ab6-b5cc-48826c4e05c5)


- **Total Number of Work Shifts**: Shows the total number of work shifts per month for each sales representative, along with day and night shift trends.

  
  ![SD3](https://github.com/user-attachments/assets/e4292620-385e-4df7-93ba-d846705f9c17)


## 5. Action Items Based on Analysis

### Areas for Further Improvement
- **Product Sales**: 

### Work Shift Analysis
- **Shift Preference**: 

### Additional Business Impact
- **Sales Trends**: 


### Output Dashboard

![Sales Data](https://github.com/user-attachments/assets/cbf11754-2989-4e97-b9f7-74ae80f20de2)


