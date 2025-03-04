---
title: Shift First Row down when inserting Cells Data Table Rows with Node.js via C++
linktitle: Shift First Row down when inserting Cells Data Table Rows
type: docs
weight: 270
url: /nodejs-cpp/shift-first-row-down-when-inserting-cells-data-table-rows/
description: Learn how to shift the first row down when inserting Cells Data Table Rows through the Aspose.Cells for Node.js via C++ API.
keywords: Node.js via C++ shift the first row down when inserting a table into the worksheet, shift first row down, shift first row down when adding a table into worksheet
---

## **Possible Usage Scenarios**

Aspose.Cells for Node.js via C++ allows you to shift the first row down when inserting a table into the worksheet. This document explains how you may accomplish the task using Aspose.Cells APIs.

## **Shift First Row down when inserting Cells Data Table Rows**

The following sample code illustrates how to shift the first row down when inserting a table into the worksheet. We use a simple template Excel file in code to demonstrate the feature. You can exercise the feature by setting the boolean [**ImportTableOptions.shiftFirstRowDown**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#shiftFirstRowDown) attribute to **True**/**False** to better understand it. Please see the [sample Excel file](45056031.xlsx), [output Excel False file](45056032.xlsx), and [output Excel True file](45056033.xlsx) for your reference.

## **Screenshot**

![todo:image_alt_text](shift-first-row-down-when-inserting-cells-data-table-rows_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class CellsDataTable {
//This is the current row index
m_index = -1;

//These are your column names
static colsNames = ["Pet", "Fruit", "Country", "Color"];

//These are the data of each column
static col0data = ["Dog", "Cat", "Duck"];
static col1data = ["Apple", "Pear", "Banana"];
static col2data = ["UK", "USA", "China"];
static col3data = ["Red", "Green", "Blue"];

//Combine all of the data into a single two dimensional array
static colsData = [CellsDataTable.col0data, CellsDataTable.col1data, CellsDataTable.col2data, CellsDataTable.col3data];

//Leave this unimplemented because we do not need it
getColumnData(columnName) {
throw new Error("Not Implemented");
}

//It will return the current item data of given column
getItem(columnIndex) {
return CellsDataTable.colsData[columnIndex][this.m_index];
}

//It will return names of all the columns
getColumns() {
return CellsDataTable.colsNames;
}

//It will return the count of all the items
getCount() {
return CellsDataTable.col0data.length;
}

//Set it -1
beforeFirst() {
this.m_index = -1;
}

//Increase the row index by 1
next() {
this.m_index++;
return true;
}
}

function run() {
//Source directory
const sourceDir = path.join(__dirname, "data");

//Output directory
const outputDir = path.join(__dirname, "output");

//Create the instance of Cells Data Table
const cellsDataTable = new CellsDataTable();

//Load the sample workbook
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleImportTableOptionsShiftFirstRowDown.xlsx"));

//Access first worksheet
const ws = wb.getWorksheets().get(0);

//Import data table options
const opts = new AsposeCells.ImportTableOptions();

//We do now want to shift the first row down when inserting rows. 
opts.setShiftFirstRowDown(false);

//Import cells data table 
ws.getCells().importData(cellsDataTable, 2, 2, opts);

//Save the workbook
wb.save(path.join(outputDir, "outputImportTableOptionsShiftFirstRowDown-False.xlsx"));
}
```
