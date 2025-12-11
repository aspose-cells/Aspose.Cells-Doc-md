---  
title: How to Prevent Users from Printing Excel File with Node.js via C++  
linktitle: How to Prevent Users from Printing Excel File  
type: docs  
weight: 600  
url: /nodejs-cpp/how-to-prevent-printing-excel/  
description: Learn how to prevent users from printing Excel files using Aspose.Cells for Node.js via C++.  
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, prevent users from printing the whole workbook with VBA.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**  
In our daily work, there may be important information in an Excel file; in order to protect internal data from being spread, the company may not allow it to be printed. This document explains how to prevent others from printing Excel files.  

## **How to Prevent Users from Printing a File in MS Excel**  
You can apply the following VBA code to protect your specific file from being printed.  

1. Open the workbook that you don’t want others to print.  
2. Select the **Developer** tab in the Excel ribbon and click the **View Code** button in the **Controls** section. Alternatively, you can press **ALT + F11** to open the Microsoft Visual Basic for Applications window.  
   <br>  
   <img src="1.png" width=70% />  
3. In the left Project Explorer, double‑click **ThisWorkbook** to open the module, and add the VBA code.  
   <br>  
   <img src="2.png" width=70% />  
4. Save and close the code, return to the workbook, and now when you try to print the file you will receive a warning box indicating that printing is not allowed.  
   <br>  
   <img src="3.png" width=70% />  

## **How to Prevent Users from Printing an Excel File using Aspose.Cells for Node.js via C++**  

The following sample code illustrates how to prevent users from printing an Excel file:  

1. Load the [sample file](sample.xlsx).  
2. Get the `VbaModuleCollection` object from the `VbaProject` property of the workbook.  
3. Retrieve the `VbaModule` object using the name **ThisWorkbook**.  
4. Set the `codes` property of the `VbaModule`.  
5. Save the file in **xlsm** format.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes(
    "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n" +
    "  Cancel = True\r\n" +
    "  MsgBox \"Refusing to print in paperless office\"\r\n" +
    "End Sub\r\n"
);

wb.save("out.xlsm");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
