---
title: Populera Data Först per Rad och sedan per Kolumn
type: docs
weight: 1000
url: /sv/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Lär dig att fylla på data först rad för rad och sedan kolumnvis genom Aspose.Cells for JavaScript via C++ API.
keywords: Fyll på data först rad för rad sedan kolumnvis JavaScript via C++, infoga data först rad för rad sedan kolumnvis JavaScript via C++, lägg till data först rad för rad sedan kolumnvis JavaScript via C++, högeffektivt data inlägg JavaScript via C++, högeffektivt datatillskott JavaScript via C++
---

{{% alert color="primary" %}}  

Att fylla i ett kalkylblad med data först per rad och sedan per kolumn förbättrar den övergripande prestandan.  

{{% /alert %}}  

Att placera data i sekvensen A1, B1, A2, B2 går snabbare än A1, A2, B1, B2. Om det finns många celler i ett kalkylblad och du följer den andra sekvensen, det vill säga fyller i data rad för rad, kan detta tips göra programmet mycket snabbare.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
