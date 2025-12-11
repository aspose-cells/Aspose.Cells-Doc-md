---
title: Get Pivot Table Refresh Date and Refresh‑by‑Who Information
type: docs
weight: 100
url: /javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: How to get Pivot Table refresh date and refresh‑by‑who information with Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, Excel JavaScript library, Get Pivot Table refresh date and refresh‑by‑who information using Aspose.Cells for JavaScript Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ now supports fetching the refresh date and refresh‑by‑who information from a workbook.

{{% /alert %}}

## **How to Get Pivot Table Refresh Date and Refresh‑by‑Who Information**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) returns the date on which the PivotTable report was last refreshed. Similarly, the [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) property returns the name of the user who last refreshed the report. The following example demonstrates this feature, and the sample file can be downloaded from the link below.

[SourcePivotTable.xlsx](77496335.xlsx)

**Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refreshed by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refreshed by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```