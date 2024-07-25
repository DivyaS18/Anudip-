# Power BI Dashboard Documentation TASK 1(PART 1)

## 1. Introduction

### Purpose
The purpose of this dashboard is to provide a clear representation of account data from the Business data file. It specifically showcases account numbers and account holder names filtered by country.

### Audience
The intended audience for this dashboard includes business analysts, management, and stakeholders who need insights into account distribution across different countries.

## 2. Dashboard Structure

### Pages/Tabs
- **Overview**: This page provides a high-level summary of account data.
- **Account Data**: Contains detailed tables and filters to explore account data by country.

## 3. Data Sources

### Source Overview
- **Business Data File**: An Excel workbook containing various sheets, including the "Account" sheet.

### Connection Details
- The data is loaded directly from the provided Excel file using Power BI's data import functionality.

## 4. Data Preparation

### Data Cleaning/Transformation
- Only the “Account” sheet from the workbook is loaded.
- Necessary transformations include:
  - Removing any empty rows.
  - Ensuring the data types for each column are correctly set.

### Data Model
- **Tables**: The primary table used is the "Account" table.

## 5. Visualizations

### Visual Types
1. **Table**: To display the total count of account numbers against each country.
2. **Table**: To display country-wise account holder names.
3. **Slicer**: To filter data based on country.

### Visual Descriptions
- **Total Count Table**: Shows the number of account numbers for each country in a tabular format.
  ![1](https://github.com/user-attachments/assets/98fd6bd3-0e44-4b7e-813e-d9d003120809)
- **Account Holder Names Table**: Displays the account holder names grouped by country.
  ![2](https://github.com/user-attachments/assets/bc22443f-83f0-478e-9fde-5a110cf727b1)
- **Country Slicer**: Allows users to filter the data by country.
  ![3](https://github.com/user-attachments/assets/23f4c05f-b648-480b-90b3-904b37da82f4)


### Filters and Slicers
- **Country Slicer**: Enables filtering of data to show specific countries (e.g., India, Brazil, Greece, France).

**###Output DASHBOARD**
![Task 1(part 1)](https://github.com/user-attachments/assets/adc3ddd8-559c-4e55-b297-e125c819e260)

# Power BI Dashboard Documentation TASK 1(PART 2)

## 1. Introduction

### Purpose
The purpose of this dashboard is to visualize the data from the "Accounts," "Industry," and "Opportunities" worksheets of the Business data file. It aims to provide insights into industry-wise profitability margins, industry profitability percentages, profitability trends, and market values.

### Audience
The intended audience for this dashboard includes business analysts, management, and stakeholders who need to analyze industry performance and profitability across different countries.

## 2. Dashboard Structure

- **Overview**: Provides a high-level summary of industry and profitability data.
- **Industry Analysis**: Contains detailed visualizations including tables, pie charts, line & stacked column charts, and map charts to explore industry data by country.

## 3. Data Sources

### Source Overview
- **Business Data File**: An Excel workbook containing the "Accounts," "Industry," and "Opportunities" sheets.

### Connection Details
- The data is loaded directly from the provided Excel file using Power BI's data import functionality.

## 4. Data Preparation

### Data Cleaning/Transformation
- Import the worksheets named "Accounts," "Industry," and "Opportunities" from the Business data file.
- Necessary transformations include:
  - Removing any empty rows.
  - Ensuring the data types for each column are correctly set.

### Data Model
- **Tables**: "Accounts," "Industry," "Opportunities."
- **Relationships**: Establish relationships between the tables as needed.
- **Calculated Columns/Measures**: Calculated columns or measures for profitability margins and market values.

## 5. Visualizations

### Visual Types
1. **Table**: For country-wise industry and average profitability margin (in Percentage %).
2. **Pie Chart**: For industry-wise profitability percentage.
3. **Line & Stacked Column Chart**: For industry-wise profitability trends.
4. **Map Chart**: For country-wise industry market values and industry-wise presence.

### Visual Descriptions
- **Country-wise Industry and Profitability Margin Table**: Shows the average profitability margin by industry for each country.
  ![task 1 part 2 (2)](https://github.com/user-attachments/assets/5104f02b-890f-416a-a348-8d5e6d0aa37c)

- **Industry-wise Profitability Percentage Pie Chart**: Displays the profitability percentage for each industry.
  ![task 1 part 2 (3)](https://github.com/user-attachments/assets/4fa4b1de-96fc-4a1c-9265-3c7aecc4973e)
- **Industry-wise Profitability Trends Line & Stacked Column Chart**: Shows the trends in profitability for different industries over time.
  ![task 1 part 2 (4)](https://github.com/user-attachments/assets/5394895b-f86c-4545-8f0c-45090c0d4408)
- **Country-wise Industry Market Values Map Chart**: Visualizes the market values and industry presence across different countries.
  ![task 1 part 2 (5)](https://github.com/user-attachments/assets/9eed4497-dac9-4cf4-8a06-5e5e58993c45)

### Filters and Slicers
- **Country Filter**: Allows users to filter the data based on selected countries for all visualizations.
  ![task 1 part 2 (2a)](https://github.com/user-attachments/assets/4ec52dd6-b4c3-45b0-92a6-e98751b1dde4)

**###Output DASHBOARD**

![Task 1(part 2)](https://github.com/user-attachments/assets/5bd51b86-d492-48e7-b7ee-8237a4ae2e54)

