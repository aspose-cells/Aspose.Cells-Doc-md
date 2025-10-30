---
title: Ta bort pivotanslutning med JavaScript via C++
linktitle: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/javascript-cpp/remove-pivot-connection/
description: Lär dig hur du tar bort pivotanslutning med Aspose.Cells for JavaScript via C++.
keywords: Ta bort pivotanslutning utan Office 2013, Office 2016, Office 2019 och Office 365 JavaScript via C++.
---

## **Möjliga användningsscenario**

Om du vill koppla bort en slicer och pivottabell i Excel måste du högerklicka på slicern och välja "Rapportanslutningar..." i menyn. I alternativlistan kan du hantera kryssrutorna. På liknande sätt, om du vill koppla bort en slicer och pivottabell med Aspose.Cells for JavaScript via C++ API-programmering, använd [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-)-metoden. Den kopplar bort slicern och pivottabellen.

## **Bryt isär snitt och pivottabell**

Följande exempel laddar [exempel-Excel-filen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Det kommer åt slicern och lösgör den från pivottabellen. Slutligen sparar det arbetsboken som [utdata-Excel-fil](remove-pivot-connection-out.xlsx).

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
