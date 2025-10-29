---  
title: 通过 C++ 使用 Node.js 将工作簿保存为严格的 Open XML 电子表格格式  
linktitle: 将工作簿保存为严格的 Open XML 电子表格格式  
type: docs  
weight: 150  
url: /zh/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: 了解如何使用 Aspose.Cells for Node.js via C++ 将工作簿保存为严格的 Open XML 电子表格格式。为此，它提供了 {0} 属性。如果将其值设为 {1}，则输出的 Excel 文件将以严格的 Open XML 电子表格格式保存。  
---  

## **可能的使用场景**  

Aspose.Cells for Node.js via C++ 允许您将工作簿保存为 *严格的 Open XML 电子表格* 格式。为此，它提供了 [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) 属性。如果将其值设置为 [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance)，那么输出的 Excel 文件将以严格的 Open XML 电子表格格式保存。  

## **将工作簿保存为严格的 Open XML 电子表格格式**  

以下示例代码创建一个工作簿，并将 [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) 属性值设为 [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance)，然后保存为 [输出Excel文件](67338272.xlsx)。如果你在Microsoft Excel中打开输出的Excel文件，选择另存为...，你将看到其格式为*严格Open XML电子表格*，如下截图所示。  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
