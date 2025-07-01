---
title: Excel File and  Data Operations
linktitle: File and  Data Operations
type: docs
weight: 10
url: /nodejs-cpp/mcp/file-operations
keywords: "Excel file operations, Excel data operations, create Excel workbook, Excel worksheet, read Excel data, write Excel data"
description: "Excel file and data operations - create workbooks, manage worksheets, read and write Excel data with AI automation"
---

# Excel File and  Data Operations

Manage **Excel files** and **data operations** with AI-powered automation. Create **Excel workbooks**, manage **worksheets**, and perform **Excel data** read/write operations.

## Available Tools

- `create_workbook` - Create new **Excel workbooks** with **AI Excel** automation
- `create_worksheet` - Add **Excel worksheets** to existing **Excel workbooks**
- `get_workbook_info` - Get **Excel workbook** metadata and information
- `read_data_from_excel` - Read data from **Excel worksheets** with **AI-powered** precision
- `write_data_to_excel` - Write data to **Excel worksheets** through **Excel MCP**

## Create Excel Workbooks

### Create Basic Workbook
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### Create Workbook with Custom Sheet
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## Manage Worksheets

### Add New Worksheet
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### Get Workbook Information
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Write Excel Data

### Write Headers and Data
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### Write Data to Custom Position
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Read Excel Data

### Read Full Used Range
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### Read Specific Range
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### Read from Default Position
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## Complete Workflow Example

### 1. Create Your First Excel Report
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. Add Summary Sheet
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. Write Sales Data
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. Verify Data
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. Check Workbook Structure
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## Best Practices

1. **File Paths**: Use relative paths for better portability
2. **Sheet Names**: Use descriptive names for worksheets
3. **Data Structure**: Organize data with clear headers
4. **Range Reading**: Specify ranges for large datasets
5. **Error Handling**: Verify file existence before operations

## Common Patterns

### Data Import Pattern
1. Create workbook
2. Write raw data
3. Read back to verify
4. Process with formulas

### Multi-Sheet Reports
1. Create workbook with main sheet
2. Add summary/analysis sheets
3. Write data to each sheet
4. Link sheets with formulas

### Data Validation
1. Write data
2. Read back specific ranges
3. Verify data integrity
4. Handle missing values 