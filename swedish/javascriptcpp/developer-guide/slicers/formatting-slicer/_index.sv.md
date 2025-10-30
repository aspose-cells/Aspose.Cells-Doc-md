---
title: Formatera slicer med JavaScript via C++
linktitle: Formatering av Slicer
type: docs
weight: 20
url: /sv/javascript-cpp/formatting-slicer/
---

## **Möjliga användningsscenario**

Du kan formatera slicern i Microsoft Excel genom att ange antalet kolumner eller genom att ställa in dess stil, etc. Aspose.Cells for JavaScript via C++ tillåter dig också att göra detta med hjälp av [**Slicer.numberOfColumns**](https://reference.aspose.com/cells/javascript-cpp/slicer/#numberOfColumns--) och [**Slicer.styleType**](https://reference.aspose.com/cells/javascript-cpp/slicer/#styleType--)-egenskaperna.

## **Formatera skärva**

Vänligen se koden nedan, den laddar [test Excel-fil](67338473.xlsx) som innehåller en slicer. Den hämtar slicern och ställer in antalet kolumner och stiltyp och sparar den som [utgångs-Excel-fil](67338474.xlsx). Skärmbilden visar hur slicern ser ut efter att ha kört exemplet.

![todo:image_alt_text](formatting-slicer_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Slicer Formatting Example</title>
    </head>
    <body>
        <h1>Slicer Formatting Example</h1>
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

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Set the number of columns of the slicer
            slicer.numberOfColumns = 2;

            // Set the type of slicer style
            slicer.styleType = AsposeCells.SlicerStyleType.SlicerStyleLight6;

            // Save the workbook in output XLSX format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFormattingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer formatting updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
