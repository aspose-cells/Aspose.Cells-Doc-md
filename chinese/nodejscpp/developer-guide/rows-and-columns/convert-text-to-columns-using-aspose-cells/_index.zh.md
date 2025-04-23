---  
title: 使用 Aspose.Cells for Node.js via C++ 将文本转换为列  
linktitle: 将文本转换为列  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在 Excel 中将文本转换为列。  
---  

## **可能的使用场景**  

你可以使用 Microsoft Excel 将文本转换为列。该功能位于 *数据工具* 下的 *数据* 选项卡下。为了将某列内容拆分成多个列，数据中应包含特定的分隔符（如逗号或其他字符），否则 Microsoft Excel 无法根据该字符拆分单元格内容。Aspose.Cells for Node.js via C++ 也提供了此功能，通过 [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)。  

## **使用 Aspose.Cells for Node.js via C++ 将文本转换为列**  

以下示例代码说明了 [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) 方法的用法。代码首先在第一个工作表的 A 列添加一些人名。名和姓用空格字符分隔。然后对 A 列应用 [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) 方法，并将结果保存为输出的 Excel 文件。如果你打开 [输出 Excel 文件](25395213.xlsx)，会看到名字在 A 列，姓在 B 列，如截图所示。  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

