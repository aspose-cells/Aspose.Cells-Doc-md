---  
title: Data Validation with Node.js via C++  
type: docs  
weight: 90  
url: /nodejs-cpp/data-validation/  
description: Learn how to add data validation through the Aspose.Cells for Node.js via C++ API.  
keywords: Add Data Validation Node.js via C++, Get Validation Value Node.js via C++, Add Whole Number Data Validation Node.js via C++, Add List Data Validation Node.js via C++, Add Date Data Validation Node.js via C++, Add Time Data Validation Node.js via C++, Add Text Length Data Validation Node.js via C++, Add CellArea to existing Validation Node.js via C++, Check if validation in cell is dropdown Node.js via C++, Add Custom Validation Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel provides some good features to auto filter or validate worksheet data. Aspose.Cells fully supports Microsoft Excel's data validation and AutoFilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

## **Data Validation Types and Execution**  

Data validation is the ability to set rules pertaining to data entered on a worksheet. For example, use validation to ensure that a column labeled DATE contains only dates, or that another column contains only numbers. You could even ensure that a column labeled DATE contains only dates within a certain range. With data validation, you can control what is entered into cells in the worksheet.  

Microsoft Excel supports a number of different types of data validation. Each type is used to control what type of data is entered into a cell, or cell range. Below, code snippets illustrate how to validate that:  

- Numbers are whole, that is, that they don't have a decimal part.  
- Decimal numbers follow the right structure. The code example defines that a range of cells should have two decimal spaces.  
- Values are restricted to a list of values. List validation defines a separate list of values that can be applied to a cell, or cell range.  
- Dates fall within a specific range.  
- A time is within a specific range.  
- A text is within a given character length.  

### **Data Validation with Microsoft Excel**  

To create validations using Microsoft Excel:  

1. In a worksheet, select the cells to which you want to apply validation.  
1. From the **Data** menu, select **Validation**. The validation dialog will be displayed.  
1. Click the **Settings** tab and enter settings.  

### **Data Validation with Aspose.Cells for Node.js via C++**  

Data validation is a powerful feature for validating the information entered into worksheets. With data validation, developers can provide users with a list of choices, restrict data entries to a specific type or size, etc.  
In Aspose.Cells for Node.js via C++, each [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class has a [**Validations**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/validations) property which represents a collection of [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) objects. To set up validation, set some of the [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) class' properties as follows:  

- Type – represents the validation type, which may be specified by using one of the predefined values in the [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) enumeration.  
- Operator – represents the operator to be used in the validation, which may be specified by using one of the predefined values in the [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype) enumeration.  
- Formula1 – represents the value or expression associated with the first part of the data validation.  
- Formula2 – represents the value or expression associated with the second part of the data validation.  

When the [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) object's properties have been configured, developers can use the [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) structure to store information about the cell range that will be validated using the created validation.  

#### **Types of Data Validation**  

The [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) enumeration has the following members:  

|**Member Name**|**Description**|  
| :- | :- |  
|AnyValue|Denotes a value of any type.|  
|WholeNumber|Denotes validation type for whole numbers.|  
|Decimal|Denotes validation type for decimal numbers.|  
|List|Denotes validation type for drop-down list.|  
|Date|Denotes validation type for dates.|  
|Time|Denotes validation type for time.|  
|TextLength|Denotes validation type for the length of the text.|  
|Custom|Denotes custom validation type.|  

##### **Whole Number Data Validation**  

With this type of validation, users can enter only whole numbers within a specified range into the validated cells. The code examples that follow show how to implement the WholeNumber validation type. The example creates the same data validation using Aspose.Cells for Node.js via C++ that we created using Microsoft Excel above.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Create a workbook object.
const workbook = new AsposeCells.Workbook();

// Create a worksheet and get the first worksheet.
const ExcelWorkSheet = workbook.getWorksheets().get(0);

// Accessing the Validations collection of the worksheet
const validations = workbook.getWorksheets().get(0).getValidations();

// Create Cell Area
const ca = new AsposeCells.CellArea();
ca.StartRow = 0;
ca.EndRow = 0;
ca.StartColumn = 0;
ca.EndColumn = 0;

// Creating a Validation object
const validation = validations.get(validations.add(ca));

// Setting the validation type to whole number
validation.setType(AsposeCells.ValidationType.WholeNumber);

// Setting the operator for validation to Between
validation.setOperator(AsposeCells.OperatorType.Between);

// Setting the minimum value for the validation
validation.setFormula1("10");

// Setting the maximum value for the validation
validation.setFormula2("1000");

// Applying the validation to a range of cells from A1 to B2 using the
// CellArea structure
const area = new AsposeCells.CellArea();
area.StartRow = 0;
area.EndRow = 1;
area.StartColumn = 0;
area.EndColumn = 1;

// Adding the cell area to Validation
validation.addArea(area);

// Save the workbook.
workbook.save(path.join(dataDir, "output.out.xls"));
```  

##### **List Data Validation**  

This type of validation allows the user to enter values from a drop-down list. It provides a list: a series of rows that contain data. In the example, a second worksheet is added to hold the list source. Users can only select values from the list. The validation area is the cell range A1:A5 in the first worksheet.  

It is important here that you set the [**Validation.inCellDropDown**](https://reference.aspose.com/cells/nodejs-cpp/validation/properties/incelldropdown) property to **true**.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Create a workbook object.
let workbook = new AsposeCells.Workbook();

// Get the first worksheet.
let worksheet1 = workbook.getWorksheets().get(0);

// Add a new worksheet and access it.
let i = workbook.getWorksheets().add();
let worksheet2 = workbook.getWorksheets().get(i);

// Create a range in the second worksheet.
let range = worksheet2.getCells().createRange("E1", "E4");

// Name the range.
range.setName("MyRange");

// Fill different cells with data in the range.
range.get(0, 0).putValue("Blue");
range.get(1, 0).putValue("Red");
range.get(2, 0).putValue("Green");
range.get(3, 0).putValue("Yellow");

// Get the validations collection.
let validations = worksheet1.getValidations();

// Create Cell Area
let ca = new AsposeCells.CellArea();
ca.StartRow = 0;
ca.EndRow = 0;
ca.StartColumn = 0;
ca.EndColumn = 0;

// Create a new validation to the validations list.
let validation = validations.get(validations.add(ca));

// Set the validation type.
validation.setType(AsposeCells.ValidationType.List);

// Set the operator.
validation.setOperator(AsposeCells.OperatorType.None);

// Set the in cell drop down.
validation.setInCellDropDown(true);

// Set the formula1.
validation.setFormula1("=MyRange");

// Enable it to show error.
validation.setShowError(true);

// Set the alert type severity level.
validation.setAlertStyle(AsposeCells.ValidationAlertType.Stop);

// Set the error title.
validation.setErrorTitle("Error");

// Set the error message.
validation.setErrorMessage("Please select a color from the list");

// Specify the validation area.
let area = new AsposeCells.CellArea();
area.StartRow = 0;
area.EndRow = 4;
area.StartColumn = 0;
area.EndColumn = 0;

// Add the validation area.
validation.addArea(area);

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```  

##### **Date Data Validation**  

With this type of validation, users enter date values within a specified range, or meeting specific criteria, into the validated cells. In the example, the user is restricted to enter dates between 1970 to 1999. Here, the validation area is the B1 cell.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Create a workbook.
let workbook = new AsposeCells.Workbook();

// Obtain the cells of the first worksheet.
let cells = workbook.getWorksheets().get(0).getCells();

// Put a string value into the A1 cell.
cells.get("A1").putValue("Please enter Date b/w 1/1/1970 and 12/31/1999");

// Set row height and column width for the cells.
cells.setRowHeight(0, 31);
cells.setColumnWidth(0, 35);

// Get the validations collection.
let validations = workbook.getWorksheets().get(0).getValidations();

// Create Cell Area
let ca = new AsposeCells.CellArea();
ca.StartRow = 0;
ca.EndRow = 0;
ca.StartColumn = 0;
ca.EndColumn = 0;

// Add a new validation.
let validation = validations.get(validations.add(ca));

// Set the data validation type.
validation.setType(AsposeCells.ValidationType.Date);

// Set the operator for the data validation
validation.setOperator(AsposeCells.OperatorType.Between);

// Set the value or expression associated with the data validation.
validation.setFormula1("1/1/1970");

// The value or expression associated with the second part of the data validation.
validation.setFormula2("12/31/1999");

// Enable the error.
validation.setShowError(true);

// Set the validation alert style.
validation.setAlertStyle(AsposeCells.ValidationAlertType.Stop);

// Set the title of the data-validation error dialog box
validation.setErrorTitle("Date Error");

// Set the data validation error message.
validation.setErrorMessage("Enter a Valid Date");

// Set and enable the data validation input message.
validation.setInputMessage("Date Validation Type");
validation.setIgnoreBlank(true);
validation.setShowInput(true);

// Set a collection of CellArea which contains the data validation settings.
let cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 0;
cellArea.EndRow = 0;
cellArea.StartColumn = 1;
cellArea.EndColumn = 1;

// Add the validation area.
validation.addArea(cellArea);

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```  

##### **Time Data Validation**  

With this type of validation, users can enter times within a specified range, or meeting some criteria, into the validated cells. In the example, the user is restricted to enter times between 09:00 to 11:30 AM. Here, the validation area is the B1 cell.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtain the cells of the first worksheet.
const cells = workbook.getWorksheets().get(0).getCells();

// Put a string value into A1 cell.
cells.get("A1").putValue("Please enter Time b/w 09:00 and 11:30 'o Clock");

// Set the row height and column width for the cells.
cells.setRowHeight(0, 31);
cells.setColumnWidth(0, 35);

// Get the validations collection.
const validations = workbook.getWorksheets().get(0).getValidations();

// Create Cell Area
const ca = new AsposeCells.CellArea();
ca.StartRow = 0;
ca.EndRow = 0;
ca.StartColumn = 0;
ca.EndColumn = 0;

// Add a new validation.
const validation = validations.get(validations.add(ca));

// Set the data validation type.
validation.setType(AsposeCells.ValidationType.Time);

// Set the operator for the data validation.
validation.setOperator(AsposeCells.OperatorType.Between);

// Set the value or expression associated with the data validation.
validation.setFormula1("09:00");

// The value or expression associated with the second part of the data validation.
validation.setFormula2("11:30");

// Enable the error.
validation.setShowError(true);

// Set the validation alert style.
validation.setAlertStyle(AsposeCells.ValidationAlertType.Information);

// Set the title of the data-validation error dialog box.
validation.setErrorTitle("Time Error");

// Set the data validation error message.
validation.setErrorMessage("Enter a Valid Time");

// Set and enable the data validation input message.
validation.setInputMessage("Time Validation Type");
validation.setIgnoreBlank(true);
validation.setShowInput(true);

// Set a collection of CellArea which contains the data validation settings.
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 0;
cellArea.EndRow = 0;
cellArea.StartColumn = 1;
cellArea.EndColumn = 1;

// Add the validation area.
validation.addArea(cellArea);

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```  

##### **Text Length Data Validation**  

With this type of validation, users can enter text values of a specified length into the validated cells. In the example, the user is restricted to enter string values with no more than 5 characters. The validation area is the B1 cell.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Create a new workbook.
const workbook = new AsposeCells.Workbook();

// Obtain the cells of the first worksheet.
const cells = workbook.getWorksheets().get(0).getCells();

// Put a string value into A1 cell.
cells.get("A1").putValue("Please enter a string not more than 5 chars");

// Set row height and column width for the cell.
cells.setRowHeight(0, 31);
cells.setColumnWidth(0, 35);

// Get the validations collection.
const validations = workbook.getWorksheets().get(0).getValidations();

// Create Cell Area
const ca = new AsposeCells.CellArea();
ca.setStartRow(0);
ca.setEndRow(0);
ca.setStartColumn(0);
ca.setEndColumn(0);

// Add a new validation.
const validation = validations.get(validations.add(ca));

// Set the data validation type.
validation.setType(AsposeCells.ValidationType.TextLength);

// Set the operator for the data validation.
validation.setOperator(AsposeCells.OperatorType.LessOrEqual);

// Set the value or expression associated with the data validation.
validation.setFormula1("5");

// Enable the error.
validation.setShowError(true);

// Set the validation alert style.
validation.setAlertStyle(AsposeCells.ValidationAlertType.Warning);

// Set the title of the data-validation error dialog box.
validation.setErrorTitle("Text Length Error");

// Set the data validation error message.
validation.setErrorMessage(" Enter a Valid String");

// Set and enable the data validation input message.
validation.setInputMessage("TextLength Validation Type");
validation.setIgnoreBlank(true);
validation.setShowInput(true);

// Set a collection of CellArea which contains the data validation settings.
const cellArea = new AsposeCells.CellArea();
cellArea.setStartRow(0);
cellArea.setEndRow(0);
cellArea.setStartColumn(1);
cellArea.setEndColumn(1);

// Add the validation area.
validation.addArea(cellArea);

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Data Validation Rules**  

When data validations are implemented, validation can be checked by assigning different values in the cells. [**Cell.getValidationValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/methods/getvalidationvalue) can be used to fetch the validation result. The following example demonstrates this feature with different values. The sample file can be downloaded from the following link for testing:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate the workbook from sample Excel file
const workbook = new AsposeCells.Workbook(dataDir + "sample.xlsx");

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access Cell C1
// Cell C1 has the Decimal Validation applied on it.
// It can take only the values Between 10 and 20
const cell = worksheet.getCells().get("C1");

// Enter 3 inside this cell
// Since it is not between 10 and 20, it should fail the validation
cell.putValue(3);

// Check if number 3 satisfies the Data Validation rule applied on this cell
console.log("Is 3 a Valid Value for this Cell: " + cell.getValidationValue());

// Enter 15 inside this cell
// Since it is between 10 and 20, it should succeed the validation
cell.putValue(15);

// Check if number 15 satisfies the Data Validation rule applied on this cell
console.log("Is 15 a Valid Value for this Cell: " + cell.getValidationValue());

// Enter 30 inside this cell
// Since it is not between 10 and 20, it should fail the validation again
cell.putValue(30);

// Check if number 30 satisfies the Data Validation rule applied on this cell
console.log("Is 30 a Valid Value for this Cell: " + cell.getValidationValue());
```  

## **Check if validation in cell is dropdown**  

As we have seen there are many types of validations that can be implemented within a cell. If you want to check whether validation is a dropdown or not, the [**Validation.inCellDropDown**](https://reference.aspose.com/cells/nodejs-cpp/validation/properties/incelldropdown) property can be used to test this. The following sample code demonstrates the usage of this property. A sample file for testing can be downloaded from the following link:  

[sampleValidation.xlsx](79527947.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

const workbook = new AsposeCells.Workbook(dataDir + "sampleValidation.xlsx");
const sheet = workbook.getWorksheets().get("Sheet1");
const cells = sheet.getCells();

const checkDropDown = (cell, cellRef) => {
    const validation = cell.getValidation();
    if (validation.getInCellDropDown()) {
        console.log(`${cellRef} is a dropdown`);
    } else {
        console.log(`${cellRef} is NOT a dropdown`);
    }
};

checkDropDown(cells.get("A2"), "A2");
checkDropDown(cells.get("B2"), "B2");
checkDropDown(cells.get("C2"), "C2");
```  

## **Add CellArea to existing Validation**  

There might be cases where you might want to add [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) to existing [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). When you add [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) using [**Validation.addArea(CellArea cellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/methods/addarea), Aspose.Cells checks all existing areas to see if the new area already exists. If the file has a large number of validations, this takes a performance hit. To overcome this, the API provides the [**Validation.addArea(CellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/nodejs-cpp/validation/addarea/methods/1) method. The *checkIntersection* parameter indicates whether to check the intersection of a given area with existing validation areas. Setting it to **false** will disable the checking of other areas. The *checkEdge* parameter indicates whether to check the applied areas. If the new area becomes the top-left area, internal settings are rebuilt. If you are sure that the new area is not the top-left area, you may set this parameter as **false**.  

The following code snippet demonstrates the use of the [**Validation.addArea(CellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/nodejs-cpp/validation/addarea/methods/1) method to add a new [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) to existing [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "ValidationsSample.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Accessing the Validations collection of the worksheet
const validation = worksheet.getValidations().get(0);

// Create your cell area.
const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

// Adding the cell area to Validation
validation.addArea(cellArea, false, false);

// Save the output workbook.
workbook.save(path.join(outputDir, "ValidationsSample_out.xlsx"));
```  

The source and output excel files are attached for reference.  

[Source File](96928093.xlsx)  

[Output File](96928220.xlsx)  

## **Advance topics**  
- [Get Cell Validation in ODS Files](/cells/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Get Validation Applied on a Cell](/cells/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Verify that Cell Value Satisfies Data Validation Rules](/cells/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  
  