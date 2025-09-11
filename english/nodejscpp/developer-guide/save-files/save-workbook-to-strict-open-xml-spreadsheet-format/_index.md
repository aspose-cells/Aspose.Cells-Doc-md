---  
title: Save Workbook to Strict Open XML Spreadsheet Format with Node.js via C++  
linktitle: Save Workbook to Strict Open XML Spreadsheet Format  
type: docs  
weight: 150  
url: /nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Learn how to save a workbook in Strict Open XML Spreadsheet format using Aspose.Cells for Node.js via C++.  
---  
  
## **Possible Usage Scenarios**  
  
Aspose.Cells for Node.js via C++ allows you to save the workbook in *Strict Open XML Spreadsheet* format. For that purpose, it provides the [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) property. If you set its value as [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), then the output Excel file will be saved in Strict Open XML Spreadsheet format.  
  
## **Save Workbook to Strict Open XML Spreadsheet Format**  
  
The following sample code creates a workbook and sets the value of the [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) property as [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) and saves it as [output Excel file](67338272.xlsx). If you open the output Excel file in Microsoft Excel and open the Save As... dialog box, you will see its format as *Strict Open XML Spreadsheet* as shown in this screenshot.  
  
![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  
  
## **Sample Code**  
  
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