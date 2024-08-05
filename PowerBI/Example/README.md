# **Employee Dashboard Documentation**

## **1. Introduction**

The Employee Dashboard is designed to provide a detailed analysis of employee data, including demographics, compensation, and performance metrics. This document outlines the features, components, and functionalities of the Power BI dashboard created using the provided employee dataset.

## **2. Data Source**

- **File Name**: `employee.xlsx`
- **File Format**: Excel
- **Headers**:
  - **Slno**: Serial Number (1, 2, 3, ..., 25)
  - **Empname**: Employee Names
  - **Gender**: Gender (Male, Female)
  - **Designation**: Designation (HR, Exe, Manager, Admin)
  - **Basic Pay**: Basic Pay of the Employee(ranging between 25000-50000)
  - **Rating**: Employee Rating (out of 5)


## **3. **Derived Insights Columns****

**3.1 Outing**

**Description**: Indicates whether an employee is eligible for outings or fieldwork based on their performance category.

**Eligibility Criteria**:

**Eligible**: Employees with a performance rating of "Excellent" or "Good".

**Not Eligible**: Employees with a performance rating of "Above Average", "Average", "Below Average", "Poor", or "Worst".

**Values**: Categorical values such as "Eligible" or "Not Eligible".

**3.2 Allowance**

**Description**: Represents additional compensation provided to employees based on their designation. The allowance is calculated as a percentage increase on the basic pay according to the employee's designation.

**Calculation**:

**Admin**: 6% hike on Basic Pay

**HR**: 9% hike on Basic Pay

**Exe**: 12% hike on Basic Pay

**Manager**: 15% hike on Basic Pay

**Values**: Numeric values representing the amount of allowance, calculated as a percentage of the basic pay.

**3.3 Performance**

**Description**: A calculated column that evaluates employee performance based on their ratings. It categorizes employees into performance bands to summarize their overall performance.

**Performance Categories**:

**Excellent**: Rating of 5

**Good**: Rating of 4.5

**Above Average**: Rating of 4

**Average**: Rating of 3.5

**Below Average**: Rating of 3

**Poor**: Rating of 2.5

**Worst**: Rating below 2.5

**Values**: Categorical values based on the rating, such as "Excellent", "Good", "Above Average", "Average", "Below Average", "Poor", or "Worst".


## **4. Dashboard Components**

### **4.1 Card Visualizations**

- **Total Employees**: Displays the aggregate number of employees.

![Card(Total Employee)](https://github.com/user-attachments/assets/d0eaa9a1-3282-4a2c-b074-da226d02b028)
  
- **Gender Breakdown**: Shows the number and percentage of male and female employees.

![Card(Male number and percentage)](https://github.com/user-attachments/assets/798755e4-34e2-41d8-9f50-e940819df58e)
![Card(Female number and percentage)](https://github.com/user-attachments/assets/1a18fa98-d28c-490a-ae07-c2d27a33b968)

### **4.2 Stacked Column Charts**

- **Basic Pay by Employee Name**: Illustrates the distribution of basic pay across different employees.

![Stacked Column Chart(Basic Pay)](https://github.com/user-attachments/assets/83796910-761d-4973-a124-1c77e75b4af0)
  
- **Rating by Employee Name**: Visualizes the rating scores assigned to each employee.

![Stacked Column Chart(Rating)](https://github.com/user-attachments/assets/b73cd568-f494-4ac1-8a57-1d35b3b45b69)

### **4.3 Pie Chart**

- **Sum of Basic Pay by Gender**: Depicts the proportion of total basic pay allocated to male and female employees.

![Pie Chart(Basic Pay)](https://github.com/user-attachments/assets/01978a99-32df-4a59-aa47-5c6117fb7d7a)

### **4.4 Doughnut Chart**

- **Sum of Basic Pay by Designation**: Represents the total basic pay categorized by employee designation.

![Doughnut Chart(Basic Pay)](https://github.com/user-attachments/assets/52387c31-7578-4393-a27e-bd2d386c3640)

### **4.5 Gauge Visualizations**

- **Percentage of Male Employees**: Displays the percentage of male employees compared to the total number of employees.
  
- **Percentage of Female Employees**: Displays the percentage of female employees compared to the total number of employees.

![Gauge](https://github.com/user-attachments/assets/0fae6301-2a1e-4d0d-89ef-1c263b738c3f)

### **4.6 Additional Card Visualizations**

- **Designation-wise Sum of Basic Pay**: Four separate cards display the sum of basic pay for each designation, calculated through specific measures.

![Cards(Designation wise total salary)](https://github.com/user-attachments/assets/a625a83a-10dd-4d15-b716-ed0af78c27b8)

### **4.7 Slicers**

- **Designation**: Filters data by employee designation.

![Slicer(Designation)](https://github.com/user-attachments/assets/9357ec90-c86b-4acb-a80c-9fad4dbd26ff)
  
- **Performance**: Filters data based on a performance column derived from employee ratings.

![Slicer(Performance)](https://github.com/user-attachments/assets/b913f849-e83c-4300-8301-8477ca6d01bd)
  
- **Onsite**: Filters data according to an onsite status column created from the performance data.

![Slicer(Onsite)](https://github.com/user-attachments/assets/639b7ace-00cf-42f0-b621-b2bb9dd67c9a)

## **5. Measures and Calculations**

- **Gender Count and Percentage**: Calculated measures for determining the number and percentage of male and female employees.

- **Sum of Basic Pay by Designation**: Measures used to compute the total basic pay for each designation category.

## **6. Table View Format**

The table view format presents raw data in a structured format. Below is a screenshot of the table view for reference:

![PowerBi Dashboard table](https://github.com/user-attachments/assets/6b34a6d8-c46c-4806-b0c1-2f70c8e36820)

- **Slno**: Serial number of the employee.
  
- **Empname**: Name of the employee.
  
- **Gender**: Gender of the employee.
  
- **Designation**: Employee's designation within the company.
  
- **Basic Pay**: Monthly or annual basic pay.
  
- **Rating**: Employee's performance rating.

## **7. Interactive Features**

- **Slicers**: Enable dynamic filtering of data based on designation, performance, and onsite status, allowing for granular analysis and visualization.

- **Charts and Cards**: Provide visual summaries and detailed insights into various aspects of employee data.

- **Gauges**: Offer a quick view of the percentage distribution of male and female employees.

## **8. Conclusion**

The Employee Dashboard offers an interactive and detailed view of employee data, making it easier to analyze and understand trends in compensation, demographics, and performance.

![PowerBi Dashboard](https://github.com/user-attachments/assets/2ae62553-f778-406c-b693-4c36c324a0d5)
