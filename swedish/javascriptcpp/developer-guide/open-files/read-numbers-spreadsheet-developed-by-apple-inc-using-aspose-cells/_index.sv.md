---
title: Läsa Numbers kalkylblad utvecklat av Apple Inc. med Aspose.Cells for JavaScript via C++
linktitle: 1.  Hantering av olika celltyper  Om de flesta cellerna innehåller strängvärden eller formler, kommer minneskostnaden att vara densamma som Normal läget men om det finns massor av tomma celler, eller cellvärden är numeriska, booleska och så vidare, kommer {0} alternativet att ge bättre prestanda.
type: docs
weight: 140
url: /sv/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Lär dig hur du läser Numbers kalkylblad utvecklat av Apple Inc. med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**

Numbers är en kalksladdsapplikation utvecklad av Apple Inc. Aspose.Cells kan läsa Numbers kalkblad, men stöder inte att skriva till dem. Det kan läsa Numbers kalkblads data, stil och formler.

## ** Läs Numbers-kalkylblad utvecklat av Apple Inc. med Aspose.Cells for JavaScript via C++**

Följande exempel laddar [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) och konverterar det till [Output PDF Format](outputNumbersByAppleInc.pdf). Du måste använda [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)-klass och ange [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) som parameter i dess konstruktör för att ladda det framgångsrikt. Ladda ner båda från de angivna länkarna. Du kan testa koden med vilket Numbers kalkblad som helst. Läs även kommentarerna i koden för mer hjälp.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
