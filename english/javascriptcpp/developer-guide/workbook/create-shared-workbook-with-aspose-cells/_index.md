---  
title: Create Shared Workbook with Aspose.Cells for JavaScript via C++  
linktitle: Create Shared Workbook with Aspose.Cells  
type: docs  
weight: 40  
url: /javascript-cpp/create-shared-workbook-with-aspose-cells/  
description: Learn how to create a shared workbook using Aspose.Cells for JavaScript via C++.  
---  

## **Possible Usage Scenarios**  

Microsoft Excel allows you to share a workbook, as shown in the following screenshot. When you share the workbook, more than one user can edit the workbook on the network. Aspose.Cells for JavaScript via C++ enables you to create a shared workbook with the [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) property.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Create Shared Workbook with Aspose.Cells**  

The following sample code creates a shared workbook by setting the [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) property to **true**. When you open the [output Excel file](55541786.xlsx) in Microsoft Excel, you will see **Shared** displayed with the workbook name, as shown in this screenshot.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();
            
            // Share the workbook (converted getter/setter to property)
            wb.settings.shared = true;
            
            // Save the shared workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```