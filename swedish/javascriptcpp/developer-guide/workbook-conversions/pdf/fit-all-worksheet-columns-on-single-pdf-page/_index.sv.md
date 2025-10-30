---
title: Anpassa alla kalkylbladskolumner till en enda PDF sida med JavaScript via C++
linktitle: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil där alla kalkylbladets kolumner passar på en sida. Egenskapen [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjden och bredden på utdata-PDF:en hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) säkerställer att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan sträcka sig över flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)-egenskapen för att rendera ett stort kalkylblad med 100 kolumner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create and initialize an instance of Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and initialize an instance of PdfSaveOptions
            const saveOptions = new PdfSaveOptions();
            // Set AllColumnsInOnePagePerSheet to true (converted from setter to property)
            saveOptions.allColumnsInOnePagePerSheet = true;

            // Save Workbook to PDF format by passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
