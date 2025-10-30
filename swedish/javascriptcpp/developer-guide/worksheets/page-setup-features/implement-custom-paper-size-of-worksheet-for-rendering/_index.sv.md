---
title: Implementera anpassad pappersstorlek för arbetsblad för rendering med JavaScript via C++
linktitle: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering
type: docs
weight: 70
url: /sv/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Denna artikel förklarar hur man använder JavaScript API via C++ för att ange en anpassad pappersstorlek för dina önskade arbetsblad när man renderar en Excel fil till PDF format programmatisk.
keywords: Anpassa sidstorlek när du renderar Excel till PDF JavaScript via C++
---

## **Möjliga användningsscenario**  

Det finns inget direkt alternativ för att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in en anpassad pappersstorlek för dina önskade arbetsblad när du renderar en Excel-fil till PDF. Detta dokument förklarar hur man sätter en anpassad pappersstorlek för ett arbetsblad med hjälp av Aspose.Cells API:er.  

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**  

Aspose.Cells låter dig implementera din önskade pappersstorlek för arbetsbladet. Du kan använda [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-)-metoden av [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-klassen för att specificera en anpassad sidstorlek. Följande exempel kod visar hur man specificerar en anpassad pappersstorlek för det första arbetsbladet i arbetsboken. Se också den [utgångs PDF](45056028.pdf) som genererades med koden för referens.  

## **Skärmdump**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
