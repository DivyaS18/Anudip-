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
  
- **Gender Breakdown**: Shows the number and percentage of male and female employees.

### **4.2 Stacked Column Charts**

- **Basic Pay by Employee Name**: Illustrates the distribution of basic pay across different employees.
  
- **Rating by Employee Name**: Visualizes the rating scores assigned to each employee.

### **4.3 Pie Chart**

- **Sum of Basic Pay by Gender**: Depicts the proportion of total basic pay allocated to male and female employees.

### **4.4 Doughnut Chart**

- **Sum of Basic Pay by Designation**: Represents the total basic pay categorized by employee designation.

### **4.5 Gauge Visualizations**

- **Percentage of Male Employees**: Displays the percentage of male employees compared to the total number of employees.
  
- **Percentage of Female Employees**: Displays the percentage of female employees compared to the total number of employees.

### **4.6 Additional Card Visualizations**

- **Designation-wise Sum of Basic Pay**: Four separate cards display the sum of basic pay for each designation, calculated through specific measures.

### **4.7 Slicers**

- **Designation**: Filters data by employee designation.
  
- **Performance**: Filters data based on a performance column derived from employee ratings.
  
- **Onsite**: Filters data according to an onsite status column created from the performance data.

## **5. Measures and Calculations**

- **Gender Count and Percentage**: Calculated measures for determining the number and percentage of male and female employees.
- **Sum of Basic Pay by Designation**: Measures used to compute the total basic pay for each designation category.

## **6. Table View Format**

The table view format presents raw data in a structured format. Below is a screenshot of the table view for reference:


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
