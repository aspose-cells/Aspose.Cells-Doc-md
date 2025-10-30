---
title: Lägg till pivottabellanslutning med JavaScript via C++
linktitle: Lägg till pivottabellanslutning
type: docs
weight: 30
url: /sv/javascript-cpp/add-pivot-connection/
description: Lär dig hur du lägger till pivottabellanslutning med hjälp av Aspose.Cells for JavaScript via C++.
keywords: Lägg till pivottabellanslutning utan åtkomst till Office 2013, Office 2016, Office 2019 och Office 365 JavaScript via C++.
---

## **Möjliga användningsscenario**

Om du vill koppla en slicer och pivottabell i Excel måste du högerklicka på slicern och välja "Rapportanslutningar...". I funktionslistan kan du operera på kryssrutan. På liknande sätt, om du vill koppla en slicer och pivottabell programmatiskt med Aspose.Cells API, använd [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-)-metoden. Det kommer att koppla slicern och pivottabellen.

## **Associera slicer och Pivottabell**

Följande exempel laddar [exempel-Excel-filen](add-pivot-connection.xlsx) som innehåller en befintlig slicer. Det kommer åt slicern och kopplar sedan slicern och pivottabellen. Slutligen sparar det arbetsboken som [utdata-Excel-fil](add-pivot-connection-out.xlsx).

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
