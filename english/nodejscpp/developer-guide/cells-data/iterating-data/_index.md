---  
title: How and Where to Use Enumerators with Node.js via C++  
linktitle: Iterate Data  
type: docs  
weight: 55  
url: /nodejs-cpp/how-and-where-to-use-enumerators/  
description: Learn how to use Enumerators through the Aspose.Cells for Node.js via C++ API.  
keywords: How to use Enumerators Node.js via C++, Cells Enumerator Node.js via C++, Rows Enumerator Node.js via C++, Columns Enumerator Node.js via C++  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

An enumerator is an object that provides the ability to traverse a container or a collection. Enumerators can be used to read the data in the collection, but they cannot be used to modify the underlying collection, whereas an Array is an interface that defines one method `getEnumerator`, which returns an `IEnumerator` interface; this, in turn, allows read‑only access to a collection.  

Aspose.Cells APIs provide a bunch of enumerators; however, this article mainly discusses the three types listed below.  

1. Cells Enumerator  
2. Rows Enumerator  
3. Columns Enumerator  

{{% /alert %}}  

## **How to use Enumerators**  

### **Cells Enumerator**  

There are various ways to access the Cells Enumerator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells enumerator.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
2. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
3. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

All of the above‑mentioned methods return an enumerator that allows traversing the collection of cells which have been initialized.  

{{% alert color="primary" %}}  

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or an existing Cell to be deleted). Otherwise, the enumerator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).  

{{% /alert %}}  

The following code example demonstrates the implementation of the `IEnumerator` interface for a Cells collection.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
    console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
    console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
    console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Rows Enumerator**  

The Rows Enumerator can be accessed while using the [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
    const row = rows.get(i);
    console.log(row.getIndex());
}
```  

### **Columns Enumerator**  

The Columns Enumerator can be accessed while using the [**ColumnCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/columncollection/#getEnumerator--) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
    const col = columns.get(i);
    console.log(col.getIndex());
}
```  

## **Where to use Enumerators**  

In order to discuss the advantages of using enumerators, let's take a real‑time example.  

**Scenario**  

An application requirement is to traverse all cells in a given [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) to read their values. There are several ways to implement this goal; a few are demonstrated below.  

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

As you can observe, both of the above‑mentioned approaches use more or less similar logic, that is, loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons, as discussed below.  

1. APIs such as [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) & [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) require extra time to gather the corresponding statistics. In case the data matrix (rows × columns) is large, using these APIs could impose a performance penalty.  
2. In most cases, not all cells in a given range are instantiated. In such situations, checking every cell in the matrix is not as efficient as checking only the initialized cells.  
3. Accessing a cell in a loop as `Cells[row, column]` will cause all cell objects in a range to be instantiated, which may eventually cause an **OutOfMemoryException**.  

## **Conclusion**  

Based on the above‑mentioned facts, the following are the scenarios where enumerators should be used.  

1. Read‑only access of the cell collection is required; i.e., the requirement is to only inspect the cells.  
2. A large number of cells need to be traversed.  
3. Only initialized cells/rows/columns should be traversed.  

{{< app/cells/assistant language="nodejs-cpp" >}}
