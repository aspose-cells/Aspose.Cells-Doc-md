---
title: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/javascript-cpp/detect-hyperlink-type/
description: Lär dig hur du upptäcker hyperlänktstyp via Aspose.Cells for JavaScript via C++ API.
keywords: Upptäck hyperlink typ JavaScript via C++, Upptäck typen av hyperlänk JavaScript via C++, Hämta typen av hyperlänk JavaScript via C++
---

## **Identifiera hyperlänkstyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filväg, etc. Aspose.Cells for JavaScript via C++ stödjer funktionen att upptäcka typen av hyperlänk. Typerna av hyperlänkar är representerade av [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enumeration. [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enumeration har följande medlemmar.

- Extern: Extern länk
- Filväg: Lokal och fullständig sökväg till filer/mappar.
- E-post: E-post
- Cellreferens: Länk till cell eller namngiven intervall.

För att kontrollera typen av hyperlänk, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) klassen en [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). Följande kodbubbla demonstrerar användningen av [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) egenskapen genom att använda denna [källa Excel-fil](94896195.xlsx).

### Källkod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Följande är utdatan som genereras av den tidigare givna kodsnutten.

### Konsolutfall
