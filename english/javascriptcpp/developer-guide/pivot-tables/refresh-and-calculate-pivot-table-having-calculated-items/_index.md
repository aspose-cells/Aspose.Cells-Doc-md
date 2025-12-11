---
title: Refresh and Calculate Pivot Table having Calculated Items
type: docs
weight: 40
url: /javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ now supports refreshing and calculating **pivot tables** having calculated items. Please use the [**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--) and [**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) as usual to perform this function.

{{% /alert %}}

## **Refresh and Calculate Pivot Table having Calculated Items**

The following sample code loads the [source Excel file](5115238.xlsx) which contains a pivot table that has three calculated items, such as "add", "div", and "div2". **First, we change** the value of cell D2 to 20 and then refresh and calculate the pivot table using Aspose.Cells for JavaScript via C++ APIs and save the workbook in PDF format. The results in the [output PDF](5115229.pdf) **show** that Aspose.Cells for JavaScript via C++ refreshed and calculated the pivot table having calculated items successfully. You can verify it using Microsoft Excel by manually putting the value 20 in cell D2 and then refreshing the pivot table via the Alt+F5 shortcut key or clicking the pivot table **Refresh** button.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```