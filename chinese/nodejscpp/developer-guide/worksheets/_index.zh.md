---  
title: 使用 Node.js 通过 C++ 管理Microsoft Excel文件的工作表  
linktitle: 工作表  
type: docs  
weight: 90  
url: /zh/nodejs-cpp/manage-worksheets/  
description: 使用Aspose.Cells for Node.js via C++添加、删除并激活工作表。  
---  

{{% alert color="primary" %}}  
开发人员可以利用Aspose.Cells灵活的API以编程方式轻松创建和管理Microsoft Excel文件中的工作表。本主题描述了在Microsoft Excel文件中添加和移除工作表的方法。  
{{% /alert %}}  

Aspose.Cells 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，它代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，可以访问Excel文件中的每个工作表。  

工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供了管理工作表的各种属性和方法。  

## **向新的Excel文件添加工作表**  

要通过程序创建新的Excel文件:  

1. 创建 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类的对象。  
1. 调用 [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 类的 [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) 方法。会自动向Excel文件中添加一个空白工作表。可以通过传递新工作表的索引到 [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合引用它。  
1. 获取工作表引用。  
1. 对工作表进行操作。  
1. 通过调用 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类的 [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法保存含有新工作表的Excel文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **向设计电子表格添加工作表**  

向设计器电子表格添加工作表的过程与添加新工作表相同，但前提是Excel文件已存在，并且需要在添加工作表前打开此文件。设计器电子表格可以通过 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类打开。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **使用工作表名称访问工作表**  

通过指定名称或索引来访问任何工作表。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **使用工作表名称移除工作表**  

若要从文件中移除工作表，调用 [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) 类的 [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) 方法。传递工作表名到 [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) 方法以删除特定工作表。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **通过页索引删除工作表**  

按名称移除工作表在已知工作表名称时效果良好。如果不知道工作表的名称，可以使用 [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) 方法的重载版本，该版本接受工作表索引而非名称。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **激活工作表并使工作表中的单元格处于活动状态**  

有时，用户在Excel中打开文件时希望某个特定工作表处于激活状态并显示。同样，也许需要激活特定单元格并让滚动条显示该单元格。Aspose.Cells 能完成以上所有任务。  

**活动工作表** 是您正在处理的工作表：标签上的活动工作表名称默认为粗体。  

**活动单元格** 是所选单元格，也就是在开始输入数据时输入数据的单元格。一次只有一个单元格处于活动状态。活动单元格由粗边框突出显示。  

### **激活工作表并使单元格处于活动状态**  

Aspose.Cells 提供了激活工作表和单元格的专用API调用。例如，[**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) 属性用于设置工作簿中的激活工作表。同样，[**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) 属性用于设置和获取工作表中的激活单元格。  

为了确保水平或垂直滚动条位于您希望显示特定数据的行和列索引位置，请使用 [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) 和 [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--) 属性。  

以下示例显示了如何激活工作表并将其中一个单元格设为活动单元格。在生成的输出中，滚动条将滚动以使第二行和第二列成为它们的第一个可见行和列。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **高级主题**  
- [复制和移动工作表](/cells/zh/nodejs-cpp/copying-and-moving-worksheets/)  
- [计算工作表中单元格的数量](/cells/zh/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [检测空工作表](/cells/zh/nodejs-cpp/detecting-empty-worksheets/)  
- [查找工作表是否为对话框工作表](/cells/zh/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [获取工作表的唯一标识](/cells/zh/nodejs-cpp/get-worksheet-unique-id/)  
- [在工作表中创建、操作或移除场景](/cells/zh/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [管理分页](/cells/zh/nodejs-cpp/managing-page-breaks/)  
- [页面设置功能](/cells/zh/nodejs-cpp/page-setup-features/)   
- [使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性](/cells/zh/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [工作表视图](/cells/zh/nodejs-cpp/worksheet-views/)  


