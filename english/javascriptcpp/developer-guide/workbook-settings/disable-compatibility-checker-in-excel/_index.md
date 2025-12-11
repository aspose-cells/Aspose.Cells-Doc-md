---  
title: Disable Compatibility Checker in Excel with JavaScript via C++  
linktitle: Disable Compatibility Checker in Excel  
type: docs  
weight: 170  
url: /javascript-cpp/disable-compatibility-checker-in-excel/  
description: Learn how to disable the compatibility checker through the Aspose.Cells for JavaScript via C++ API.  
keywords: JavaScript Disable Compatibility Checker, Excel Disable Compatibility Checker in JavaScript via C++, Disable Compatibility Checker in Workbook.  
---  

## Disable Compatibility Checker in Excel Worksheets in JavaScript  

{{% alert color="primary" %}}  
Microsoft Excel's Compatibility Checker flags that saving a file in an earlier file format might cause functionality issues or loss of fidelity. The Compatibility Checker is a feature of Microsoft Office Excel 2007 and Microsoft Excel 2010.  

When you save a workbook in a previous version (Excel 97 through Excel 2003) from Excel 2007 or Excel 2010, the Compatibility Checker scans the workbook to see if it contains features that are not supported by the earlier version. To help you make decisions about how to handle compatibility issues, the Compatibility Checker displays dialog boxes with options. It can also be used to create a report on any issues in the workbook, or disable the feature.  

Sometimes, you need to disable the Compatibility Checker for a particular spreadsheet. With Aspose.Cells' APIs, you can do this programmatically so that users don't get frustrated or confused by the Compatibility Checker dialog box popping up when they re‑save the file in Microsoft Excel manually.  
{{% /alert %}}  

## **How to Disable Compatibility Checker using Microsoft Excel**  

To disable the Compatibility Checker in Microsoft Excel (for example Microsoft Excel 2007/2010):  

- (Excel 2007) On the Office button, click **Prepare**, then **Run Compatibility Checker**, and then clear the **Check compatibility when you save this workbook** option.  
- (Excel 2010) On the File tab, click **Info**, then **Check for issues**, click **Check Compatibility**, and, finally, clear the **Check compatibility when you save this workbook** option.  

## **How to Disable Compatibility Checker using Aspose.Cells APIs**  

Set the [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) property to **false** to disable Microsoft Excel's Compatibility Checker.  

### **Code Examples**  

The code examples that follow show how to disable the Compatibility Checker with Aspose.Cells for JavaScript via C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;
            
            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```