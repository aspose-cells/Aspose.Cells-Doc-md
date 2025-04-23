---  
title: 如何以及在哪里使用Node.js通过C++的枚举器  
linktitle: 迭代数据  
type: docs  
weight: 55  
url: /zh/nodejs-cpp/how-and-where-to-use-enumerators/  
description: 学习如何通过Aspose.Cells for Node.js via C++ API使用枚举器。  
keywords: 如何使用Node.js via C++的枚举器，单元格枚举器，行枚举器，列枚举器  
---  

{{% alert color="primary" %}}  

枚举器是一种提供遍历容器或集合能力的对象。枚举器可以用来读取集合中的数据，但不能用来修改底层集合，而数组（Array）是一种定义了一个方法`getEnumerator`的接口，返回一个`IEnumerator`接口，从而实现对集合的只读访问。  

Aspose.Cells API提供了一堆枚举器，但本文主要讨论如下三种类型。  

1. 单元格枚举器  
1. 行枚举器  
1. 列枚举器  

{{% /alert %}}  

## **如何使用枚举器**  

### **单元格枚举器**  

有各种方式可以访问单元格枚举器，并且可以根据应用程序的要求使用任何这些方法。以下是返回单元格枚举器的方法。  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

上述所有方法都返回允许遍历初始化的单元格集合的枚举器。  

{{% alert color="primary" %}}  

在遍历单元格时，集合不应被修改（进行会导致实例化新单元格或删除现有单元格的操作）。否则，枚举器可能无法正确遍历所有单元格（某些元素可能会被重复遍历或被跳过）。  

{{% /alert %}}  

以下代码示例演示了如何实现Cells集合的`IEnumerator`接口。  

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

### **行枚举器**  

在使用[**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--)方法时，可以访问行的行枚举器（Rows Enumerator）。以下代码示例演示了如何为[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)实现`IEnumerator`接口。  

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

### **列枚举器**  

在使用[**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)方法时，可以访问列的列枚举器（Columns Enumerator）。以下代码示例演示了如何为[**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)实现`IEnumerator`接口。  

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

## **枚举器的使用场景**  

为了讨论使用枚举器的优势，让我们以一个实时案例来说明。  

**情景**  

一个应用程序要求是遍历给定的[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)中的所有单元格以读取它们的值。有几种实现此目标的方法。以下是一些示例。  

### **使用显示范围**  

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

### **使用MaxDataRow和MaxDataColumn**  

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

正如您所注意到的，上述两种方法都使用了几乎相似的逻辑，即在集合中循环遍历所有单元格以读取单元格的值。对于许多原因，这可能会有问题，如下所讨论的。  

1. 诸如[**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--)、[**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)、[**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--)、[**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--)和[**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)之类的API需要额外的时间来收集相应的统计信息。如果数据矩阵（行x列）很大，在使用这些API时可能会导致性能损失。  
1. 在大多数情况下，给定范围中并非所有单元格都被实例化。在这种情况下，检查矩阵中的每个单元格比仅检查初始化的单元格效率低。  
1. 在循环中访问单元格作为Cells row, column将导致范围内的所有单元格对象被实例化，这最终可能导致OutOfMemoryException。  

## **结论**  

基于上述事实，以下是应该使用枚举器的可能情况。  

1. 需要只读访问单元格集合，即只需检查单元格。  
1. 需要遍历大量的单元格。  
1. 只需遍历已初始化的单元格/行/列。  

