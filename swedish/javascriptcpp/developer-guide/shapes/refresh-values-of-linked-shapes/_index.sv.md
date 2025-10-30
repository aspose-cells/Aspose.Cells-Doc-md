---
title: Uppdatera värden för länkade former med JavaScript via C++
linktitle: Uppdatera värdena för länkade former
type: docs
weight: 3200
url: /sv/javascript-cpp/refresh-values-of-linked-shapes/
description: Lär dig hur man uppdaterar värden för länkade former i Excel med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Ibland har du en kopplad form i din Excel-fil som är kopplad till en cell. I Microsoft Excel ändras värdet av den kopplade cellen också värdet på den kopplade formen. Detta fungerar också bra med Aspose.Cells for JavaScript via C++ om du vill spara din arbetsbok i XLS eller XLSX format. Men om du vill spara din arbetsbok i PDF- eller HTML-format måste du kalla [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--)-metoden för att uppdatera värdet på den kopplade formen.

{{% /alert %}}

## Exempel

Följande skärmdump visar käll-Excel-filen som används i exempelnumret nedan. Den har en länkad bild kopplad till cellerna A1 till E4. Vi kommer att ändra värdet i cell B4 med Aspose.Cells och sedan anropa [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--)-metoden för att uppdatera värdet på bilden och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Du kan ladda ner [källa-Excelfilen](95584291.xlsx) och [utdata-PDF](95584292.pdf) från angivna länkar.

### JavaScript-kod för att uppdatera värdena för kopplade former

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
