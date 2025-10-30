---
title: Ändra slicerinställningar med JavaScript via C++
linktitle: Ändra sliceregenskaper
type: docs
weight: 70
url: /sv/javascript-cpp/change-slicer-properties/
---

## **Möjliga användningsscenario**

Det kan finnas situationer där du vill ändra slicerns egenskaper, som placering eller radhöjd. Aspose.Cells for JavaScript via C++ ger dig möjlighet att uppdatera dessa egenskaper.

## **Ändra Slicer-egenskaper**

Var god se följande exempelkod. Den laddar in den [exempel-Excel-filen](sampleCreateSlicerToExcelTable.xlsx) som innehåller en tabell. Den skapar sedan slicern baserat på den första kolumnen och ändrar dess egenskaper som radhöjd, bredd, är utskrivbar, titel, osv. Den sparar arbetsboken som [utdataChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Slicer to Excel Table Example</title>
    </head>
    <body>
        <h1>Create Slicer to Excel Table Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first table inside the worksheet.
            const table = worksheet.listObjects.get(0);

            // Add slicer
            const idx = worksheet.slicers.add(table, 0, "H5");

            const slicer = worksheet.slicers.get(idx);
            slicer.placement = AsposeCells.PlacementType.FreeFloating;
            slicer.rowHeightPixel = 50;
            slicer.widthPixel = 500;
            slicer.title = "Aspose";
            slicer.alternativeText = "Alternate Text";
            slicer.isPrintable = false;
            slicer.isLocked = false;

            // Refresh the slicer.
            slicer.refresh();

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeSlicerProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Slicer added and properties changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
