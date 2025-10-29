---  
title: 保持空行的分隔符在导出电子表格到 CSV 格式时通过 Node.js 和 C++  
linktitle: 在将电子表格导出为CSV格式时保留空行的分隔符  
type: docs  
weight: 160  
url: /zh/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **在将电子表格导出为CSV格式时保留空行的分隔符**  

Aspose.Cells 提供在转换电子表格到 CSV 格式时保留换行符的能力。为此，你可以使用 [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/) 的 [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) 属性。[**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) 是一个布尔属性。要在转换 Excel 文件到 CSV 时保留空白行的分隔符，请将 [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) 属性设置为 **true**。  

以下示例代码加载 [源Excel文件](84378743.xlsx)，将 [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) 属性设置为 **true** 并保存为 [output.csv](84378744.csv)。屏幕截图显示源Excel文件、转换成csv时生成的默认输出以及设置 [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) 为 **true** 时的输出的对比。  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
