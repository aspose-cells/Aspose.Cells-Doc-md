---  
title: Node.js与C++中的表格和区域  
linktitle: 表格和范围  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/tables-and-ranges/  
---  

## **介绍**  

有时您在Microsoft Excel中创建一个表格，但不想继续使用它带来的表格功能。相反，您想要看起来像表格的东西。为了在不丢失格式的情况下保留表格中的数据，可以将表格转换为普通数据范围。  
Aspose.Cells确实支持Microsoft Excel的表格和列表对象的此功能。  

## **使用Microsoft Excel**  

使用**转换为范围**功能快速将表格转换为常规数据范围，而不丢失格式。在Microsoft Excel 2007/2010中：  

1. 单击表中的任意位置，确保活动单元格位于表列中。  
1. 在**设计**选项卡的**工具**组中，单击**转换为范围**。  

## **使用Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

表格在转换为范围后将不再可用其表格功能。例如，行标头不再包含排序和筛选箭头，以及在公式中使用的结构引用（使用表名称的引用）会变成常规单元格引用。  

{{% /alert %}}  

## **使用选项将表格转换为范围**  

Aspose.Cells在将表格转换为范围时提供附加选项，通过[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/)类提供[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/)类,并提供[**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--)属性，允许您设置表格行的最后索引。表格格式将保留到指定的行索引，其余格式将被移除。  

以下给出的示例代码演示了[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/)类的使用。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
