---  
title: 创建命名区域并复制命名区域内容的示例，使用Node.js via C++  
linktitle: 创建访问并复制已命名区域  
type: docs  
weight: 200  
url: /zh/nodejs-cpp/create-access-and-copy-named-ranges/  
description: 学习如何使用Aspose.Cells for Node.js via C++在Excel中创建、访问和复制命名区域。  
---  

## **介绍**  

通常，列和行标签用于引用单个单元格。可以创建描述性名称以表示单元格、单元格范围、公式或常数值。**名称**一词可能指代表单元格、单元格范围、公式或常数值的字符序列。为范围命名意味着可以通过其名称引用该范围。使用易于理解的名称，例如Products，来指代难以理解的范围，例如Sales!C20:C30。标签可用于引用同一工作表上的数据的公式；如果要表示另一工作表上的范围，可以使用名称。*命名范围是Microsoft Excel最强大的功能之一，特别是在用作列表控件、透视表、图表等的源范围时。*  

## **使用Microsoft Excel处理已命名区域**  

### **创建已命名范围**  

以下步骤描述了如何使用 **MS Excel** 命名单元格或范围。这种方法适用于 **Microsoft Office Excel 2003**、**Excel 97**、**2000** 和 **2002**。  

1. 选择你想命名的单元格或单元格范围。  
2. 点击公式栏左端的**名称框**。  
3. 输入单元格的名称。  
4. 按 ENTER。  

{{% alert color="primary" %}}  
在更改单元格内容时，不能为单元格命名。  
{{% /alert %}}  

## **使用Aspose.Cells处理命名范围**  

在这里，我们使用Aspose.Cells API来完成任务。  
Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合。  

### **创建已命名范围**  

通过调用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合的重载 [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) 方法，可以创建命名范围。 [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) 方法的典型版本使用以下参数：  

- 左上角单元格的名称，范围中左上角单元格的名称。  
- 右下角单元格的名称，范围中右下角单元格的名称。  

调用 [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) 方法时，它将返回新创建的范围，作为 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 类的实例。使用此 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 对象来配置命名范围。例如，使用 [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--) 属性设置范围的名称。以下示例展示了如何创建跨越 B4:G14 的单元格命名范围。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **将数据输入到命名范围内的单元格**  

您可以按照模式将数据插入到范围内单个单元格中  

- **JavaScript**：Range[row,column]  

假设您有一个跨越 A1:C4 的命名范围。该矩阵包含 4 * 3 = 12 个单元格。单个范围单元按顺序排列：Range[0,0]，Range[0,1]，Range[0,2]，Range[1,0]，Range[1,1]，Range[1,2]，Range[2,0]，Range[2,1]，Range[2,2]，Range[3,0]，Range[3,1]，Range[3,2]。  

使用以下属性来识别范围中的单元格:  

- firstRow 返回命名范围中第一行的索引。  
- firstColumn 返回命名范围中第一列的索引。  
- rowCount 返回命名范围中总行数。  
- columnCount 返回命名范围中总列数。  

以下示例显示如何向指定范围的单元格输入一些值。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **标识命名范围中的单元格**  

您可以按照以下模式向范围内的单个单元格插入数据：  

- **JavaScript**：Range[row,column]  

如果您有一个跨越 A1:C4 的命名范围。该矩阵包含 4 * 3 = 12 个单元格。单个范围单元按顺序排列：Range[0,0]，Range[0,1]，Range[0,2]，Range[1,0]，Range[1,1]，Range[1,2]，Range[2,0]，Range[2,1]，Range[2,2]，Range[3,0]，Range[3,1]，Range[3,2]。  

使用以下属性来识别范围中的单元格:  

- firstRow 返回命名范围中第一行的索引。  
- firstColumn 返回命名范围中第一列的索引。  
- rowCount 返回命名范围中总行数。  
- columnCount 返回命名范围中总列数。  

以下示例显示如何向指定范围的单元格输入一些值。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **访问命名范围**  

#### **访问特定的命名范围**  

调用 [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 集合的 [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) 方法，以按指定名称获取范围。典型的 [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) 方法接受命名范围的名称，并将所指定的命名范围作为 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 类的实例返回。以下示例显示如何通过名称访问指定的范围。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **访问电子表格中的所有命名范围**  

调用 [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 集合的 [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) 方法以获取电子表格中的所有命名范围。[**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) 方法返回所有命名范围的数组，属于[**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)集合。  

以下示例显示如何访问工作簿中的所有命名范围。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **复制命名范围**  

Aspose.Cells提供了[**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-)方法，用于将具有格式的单元格范围复制到另一个范围。  

以下示例显示如何将源单元格范围复制到另一个命名范围。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
