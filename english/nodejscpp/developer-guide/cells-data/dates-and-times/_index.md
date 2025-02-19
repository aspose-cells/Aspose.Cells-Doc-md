---  
title: How to Manage Dates and Times with Node.js via C++  
type: docs  
weight: 600  
url: /nodejs-cpp/how-to-manage-dates-and-times/  
description: Learn how to manage dates and times through the Aspose.Cells for Node.js via C++ API.  
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.  
---  

## **How to store Dates and Times in Excel**  
Dates and times are stored in cells as numbers. Thus, the values of cells that contain dates and times are of the numeric type. A number that specifies a date and time consists of the date (integer part) and time (fractional part) components. The Cell.DoubleValue property returns this number.  

## **How to Display Dates and Times in Aspose.Cells**  
To display a number as a date and time, apply the required date and time format to a cell via the [Style.Number](https://reference.aspose.com/cells/nodejs-cpp/style/#number-string-number-) or [Style.Custom]() property. The CellValue.DateTimeValue property returns the DateTime object, which specifies the date and time that is represented by the number contained in a cell.  
<br>  
<image src="1.png" width="70%" />  

## **How to switch two date systems in Aspose.Cells**  
MS-Excel stores dates as numbers that are called serial values. A serial value is an integer that is the number of elapsed days from the first day in the date system. Excel supports the following date systems for serial values:  

1. The 1900 date system. The first date is January 1, 1900, and its serial value is 1. The last date is December 31, 9999, and its serial value is 2,958,465. This date system is used in the workbook by default.  
1. The 1904 date system. The first date is January 1, 1904, and its serial value is 0. The last date is December 31, 9999, and its serial value is 2,957,003. To use this date system in the workbook, set the [Workbook.Settings.Date1904](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#date1904-) property to true.  

This example shows that the serial values stored on the same date in different date systems are different.  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
let workbook = new AsposeCells.Workbook();
workbook.getSettings().setDate1904(false);

// Obtaining the reference of the newly added worksheet
let ws = workbook.getWorksheets().get(0);
let cells = ws.getCells();

let dateData = new Date(2023, 10, 23); // JavaScript months are 0-based

// Setting the DateTime value to the cells
let a1 = cells.get("A1");
a1.putValue(dateData);

// Check if the cell contains a numeric value
if (a1.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A1 is Numeric Value: " + a1.getDoubleValue());
}

workbook.getSettings().setDate1904(true);
console.log("use The 1904 date system====================");

// Setting the DateTime value to the cells
let a2 = cells.get("A2");
a2.setValue(dateData);

// Check if the cell contains a numeric value
if (a2.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A2 is Numeric Value: " + a2.getDoubleValue());
}
```  
Output result:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **How to Set DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets custom format of A1 and number format of A2, and then outputs the value types.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
let workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
let ws = workbook.getWorksheets().get(0);
let cells = ws.getCells();

// Setting the DateTime value to the cells
let a1 = cells.get("A1");
a1.putValue(new Date());

// Check if the cell contains a numeric value
if (a1.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A1 is Numeric Value: " + a1.isNumericValue());
}

let a1Style = a1.getStyle();
// Set custom Datetime style
a1Style.setCustom("mm-dd-yy hh:mm:ss");
a1.setStyle(a1Style);

// Check if the cell contains a DateTime value
if (a1.getType() === AsposeCells.CellValueType.IsDateTime) {
    console.log("Cell A1 contains a DateTime value.");
} else {
    console.log("Cell A1 does not contain a DateTime value.");
}

// Setting the DateTime value to the cells
let a2 = cells.get("A2");
a2.putValue(new Date());

// Check if the cell contains a numeric value
if (a2.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A2 is Numeric Value: " + a2.isNumericValue());
}

let a2Style = a2.getStyle();
// Set the display format of numbers and dates.
a2Style.setNumber(22);
a2.setStyle(a2Style);

// Check if the cell contains a DateTime value
if (a2.getType() === AsposeCells.CellValueType.IsDateTime) {
    console.log("Cell A2 contains a DateTime value.");
} else {
    console.log("Cell A2 does not contain a DateTime value.");
}
```  

Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **How to Get DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets custom format of A1 and number format of A2, checks the value types of two cells, and then outputs the DateTime value and formatted string.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the DateTime value to the cells
const a1 = cells.get("A1");
a1.putValue(new Date());

// Check if the cell contains a numeric value
if (a1.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A1 is Numeric Value: " + a1.isNumericValue);
}

let a1Style = a1.getStyle();
// Set custom Datetime style
a1Style.setCustom("mm-dd-yy hh:mm:ss");
a1.setStyle(a1Style);

// Check if the cell contains a DateTime value
if (a1.getType() === AsposeCells.CellValueType.IsDateTime) {
    console.log("Cell A1 contains a DateTime value.");
    // Get the DateTime value
    const dateTimeValue = a1.getDateTimeValue();

    // Now, you can use dateTimeValue as needed
    console.log("A1 DateTime Value: " + dateTimeValue);

    // Output date formatted string
    console.log("A1 DateTime String Value: " + a1.getStringValue());
} else {
    console.log("Cell A1 does not contain a DateTime value.");
}

// Setting the DateTime value to the cells
const a2 = cells.get("A2");
a2.putValue(new Date());

// Check if the cell contains a numeric value
if (a2.getType() === AsposeCells.CellValueType.IsNumeric) {
    console.log("A2 is Numeric Value: " + a2.isNumericValue);
}

let a2Style = a2.getStyle();
// Set the display format of numbers and dates.
a2Style.setNumber(22);
a2.setStyle(a2Style);

// Check if the cell contains a DateTime value
if (a2.getType() === AsposeCells.CellValueType.IsDateTime) {
    console.log("Cell A2 contains a DateTime value.");
    // Get the DateTime value
    const dateTimeValue = a2.getDateTimeValue();

    // Now, you can use dateTimeValue as needed
    console.log("A2 DateTime Value: " + dateTimeValue);

    // Output date formatted string
    console.log("A2 DateTime String Value: " + a2.getStringValue());
} else {
    console.log("Cell A2 does not contain a DateTime value.");
}
```  

Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A1 DateTime Value: 11/23/2023 5:59:09 PM  
A1 DateTime String Value: 11-23-23 17:59:09  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
A2 DateTime Value: 11/23/2023 5:59:09 PM  
A2 DateTime String Value: 11/23/2023 17:59  
```  
  