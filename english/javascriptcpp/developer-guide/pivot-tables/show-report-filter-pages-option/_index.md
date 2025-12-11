---
title: Show report filter pages option
type: docs
weight: 110
url: /javascript-cpp/show-report-filter-pages-option/
---

## **Show report filter pages option**
Excel supports creating pivot tables, adding report filters, and enabling the "Show Report Filter Pages" option. Aspose.Cells for JavaScript via C++ also supports this feature, enabling the "Show Report Filter Pages" option on the created pivot table. The following is a screen showing the "Show Report Filter Pages" option in Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Sample source file and output files can be downloaded from here for testing the sample code:

[Source Excel File](81920786.xlsx)

[Output Excel File](81920787.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Sample Pivot Table Example</title>
    </head>
    <body>
        <h1>Sample Pivot Table Example</h1>
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
            
            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the second worksheet (index 1) and first pivot table
            const worksheet = workbook.worksheets.get(1);
            const pt = worksheet.pivotTables.get(0);
            
            // Set pivot field - show report filter page for first page field
            pt.showReportFilterPage(pt.pageFields.get(0));
            
            // Set position index for showing report filter pages
            pt.showReportFilterPageByIndex(pt.pageFields.get(0).position);
            
            // Set the page field name
            pt.showReportFilterPageByName(pt.pageFields.get(0).name);
            
            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSamplePivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```