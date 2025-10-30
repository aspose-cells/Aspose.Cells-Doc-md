---
title: Hämta område med externa länkar med JavaScript via C++
linktitle: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/javascript-cpp/get-range-with-external-links/
description: Lär dig hur du hämtar områden med externa länkar med Aspose.Cells for JavaScript via C++. Hämta data från olika Excel filer effektivt.
---

## **Hämta intervall med externa länkar**

 Många gånger hämtar Excel-filer data från andra Excel-filer via externa länkar. Aspose.Cells for JavaScript via C++ ger möjlighet att hämta dessa externa länkar genom att använda metoden [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-). Metoden [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea). Klassen [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) tillhandahåller en egenskap [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--) som returnerar namnet på den externa filen. Klassen [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) exponerar följande medlemmar.

- [**ReferredArea.endColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endColumn--): ändens kolumn för området
- [**ReferredArea.endRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endRow--): ändens rad för området
- [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--): Hämta det externa filnamnet om detta är en extern referens
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isArea--): Indikerar om detta är ett område
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isExternalLink--): Indikerar om detta är en extern länk
- [**ReferredArea.sheetName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#sheetName--): Indikerar vilken bladreferens detta är i
- [**ReferredArea.startColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startColumn--): Startkolumn för området
- [**ReferredArea.startRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startRow--): Startrad för området

Kodexemplet nedan visar hur man använder [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) metoden för att hämta områden med externa länkar.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External References</title>
    </head>
    <body>
        <h1>Sample External References</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SampleExternalReferences.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing named ranges via worksheets.names
            const names = workbook.worksheets.names;
            const namesCount = names.count;
            const outputLines = [];
            outputLines.push(`<p>Processing file: ${file.name}</p>`);
            outputLines.push(`<p>Named Ranges Count: ${namesCount}</p>`);

            for (let i = 0; i < namesCount; i++) {
                const namedRange = names.get(i);
                outputLines.push(`<h3>Named Range ${i}: ${namedRange.name || ('Index ' + i)}</h3>`);

                // Get referred areas (including external references)
                const referredAreas = namedRange.referredAreas(true);
                if (referredAreas) {
                    referredAreas.forEach((referredArea, idx) => {
                        outputLines.push(`<h4>Referred Area ${idx}</h4>`);
                        outputLines.push(`<ul>`);
                        outputLines.push(`<li>IsExternalLink: ${referredArea.isExternalLink}</li>`);
                        outputLines.push(`<li>IsArea: ${referredArea.isArea}</li>`);
                        outputLines.push(`<li>SheetName: ${referredArea.sheetName}</li>`);
                        outputLines.push(`<li>ExternalFileName: ${referredArea.externalFileName}</li>`);
                        outputLines.push(`<li>StartColumn: ${referredArea.startColumn}</li>`);
                        outputLines.push(`<li>StartRow: ${referredArea.startRow}</li>`);
                        outputLines.push(`<li>EndColumn: ${referredArea.endColumn}</li>`);
                        outputLines.push(`<li>EndRow: ${referredArea.endRow}</li>`);
                        outputLines.push(`</ul>`);
                    });
                } else {
                    outputLines.push(`<p>No referred areas for this named range.</p>`);
                }
            }

            resultDiv.innerHTML = outputLines.join('');
        });
    </script>
</html>
```
