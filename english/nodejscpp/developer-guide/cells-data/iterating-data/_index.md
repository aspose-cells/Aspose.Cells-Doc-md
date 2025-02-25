---  
title: How and Where to Use Enumerators with Node.js via C++  
linktitle: Iterate Data  
type: docs  
weight: 55  
url: /nodejs-cpp/how-and-where-to-use-enumerators/  
description: Learn how to use Enumerators through the Aspose.Cells for Node.js via C++ API.  
keywords: How to use Enumerators Node.js via C++, Cells Enumerator Node.js via C++, Rows Enumerator Node.js via C++, Columns Enumerator Node.js via C++  
---  

{{% alert color="primary" %}}  

An enumerator is an object that provides the ability to traverse a container or a collection. Enumerators can be used to read the data in the collection, but they cannot be used to modify the underlying collection, whereas Array is an interface that defines one method `getEnumerator` which returns an `IEnumerator` interface, this, in turn, allows read-only access to a collection.  

Aspose.Cells APIs provide a bunch of enumerators however, this article mainly discusses the three types as listed below.  

1. Cells Enumerator  
1. Rows Enumerator  
1. Columns Enumerator  

{{% /alert %}}  

## **How to use Enumerators**  

### **Cells Enumerator**  

There are various ways to access the Cells Enumerator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells enumerator.  

1. [**Cells.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/getenumerator)  
1. [**Row.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/row/methods/getenumerator)  
1. [**Range.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/range/methods/getenumerator)  

All of the above-mentioned methods return the enumerator that allows traversing the collection of cells which have been initialized.  

{{% alert color="primary" %}}  

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or existing Cell to be deleted). Otherwise, the enumerator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).  

{{% /alert %}}  

The following code example demonstrates the implementation of the `IEnumerator` interface for a Cells collection.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the enumerator from Cells collection
const cellEnumerator = workbook.getWorksheets().get(0).getCells().getEnumerator();
// Traverse cells in the collection
while (cellEnumerator.moveNext()) {
    const cell = cellEnumerator.getCurrent();
    console.log(`${cell.getName()} ${cell.getValue()}`);
}

// Get enumerator from an object of Row
const rowEnumerator = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
// Traverse cells in the given row
while (rowEnumerator.moveNext()) {
    const cell = rowEnumerator.getCurrent();
    console.log(`${cell.getName()} ${cell.getValue()}`);
}

// Get enumerator from an object of Range
const rangeEnumerator = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
// Traverse cells in the range
while (rangeEnumerator.moveNext()) {
    const cell = rangeEnumerator.getCurrent();
    console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Rows Enumerator**  

The Rows Enumerator can be accessed while using the [**RowCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/methods/getenumerator) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the enumerator for RowCollection
const rowsEnumerator = workbook.getWorksheets().get(0).getCells().getRows().getEnumerator();

// Traverse rows in the collection
while (rowsEnumerator.moveNext()) {
    const row = rowsEnumerator.getCurrent();
    console.log(row.getIndex());
}
```  

### **Columns Enumerator**  

The Columns Enumerator can be accessed while using the [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get the enumerator for ColumnsCollection
const colsEnumerator = workbook.getWorksheets().get(0).getCells().getColumns().getEnumerator();
// Traverse columns in the collection
while (colsEnumerator.moveNext()) {
    const col = colsEnumerator.getCurrent();
    console.log(col.getIndex());
}
```  

## **Where to use Enumerators**  

In order to discuss the advantages of using enumerators, let's take a real-time example.  

**Scenario**  

An application requirement is to traverse all cells in a given [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) to read their values. There could be several ways to implement this goal. A few are demonstrated below.  

### **Using Display Range**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
    for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
        // Read the Cell value
        console.log(displayRange.get(row, col).getStringValue());
    }
}
```  

### **Using MaxDataRow & MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
    for (let col = 0; col <= maxDataColumn; col++) {
        // Read the Cell value
        const currentCell = cells2.checkCell(row, col);
        if (currentCell) {
            console.log(currentCell.getStringValue());
        }
    }
}
```  

As you can observe that both of the above-mentioned approaches use more or less similar logic, that is; loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons as discussed below.  

1. APIs such as [**MaxRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/maxdisplayrange) require extra time to gather the corresponding statistics. In case the data matrix (rows x columns) is large, using these APIs could impose a performance penalty.  
1. In most of the cases, not all cells in a given range are instantiated. In such situations to check every cell in the matrix is not so efficient as compared to check only the initialized cells.  
1. Accessing a cell in a loop as Cells row, column will cause all cell objects in a range to be instantiated, which may eventually cause OutOfMemoryException.  

## **Conclusion**  

Based on above-mentioned facts, the following are the possible scenarios where enumerators should be used.  

1. Read-only access of the cell collection is required, that is; the requirement is to only inspect the cells.  
1. A large number of cells are to be traversed.  
1. Only initialized cells/rows/columns to be traversed.  
  