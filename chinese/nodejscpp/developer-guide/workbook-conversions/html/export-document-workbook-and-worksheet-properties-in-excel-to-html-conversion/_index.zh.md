---  
title: 在使用Node.js通过C++将Excel导出为HTML时导出文档、工作簿和工作表属性  
linktitle: 将Excel中的文档、工作簿和工作表属性导出为HTML  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: 了解如何使用Aspose.Cells for Node.js via C++导出Excel中的文档、工作簿和工作表属性为HTML。  
---  

## **可能的使用场景**  

 当使用Microsoft Excel或Aspose.Cells for Node.js via C++将Microsoft Excel文件导出为HTML时，还会导出各种类型的文档、工作簿和工作表属性，如下截图所示。可以通过设置[**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--)、[**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--)和[**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--)为**false**来避免导出这些属性。这些属性的默认值为**true**。以下截图显示了这些属性在导出HTML中的效果。  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **将Excel中的文档、工作簿和工作表属性导出为HTML**  

下方示例代码加载【示例Excel文件】(61767776.xlsx)，并将其转换为HTML，未导出文档、工作簿及工作表属性，输出的HTML文件为(61767779.zip)。  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
