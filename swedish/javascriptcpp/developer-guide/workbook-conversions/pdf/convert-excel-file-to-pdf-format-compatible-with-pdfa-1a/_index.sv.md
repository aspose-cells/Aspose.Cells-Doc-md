---
title: Konvertera Excel fil till PDF format som är kompatibelt med PDF/A 1a med JavaScript via C++
linktitle: Konvertera Excel fil till PDF format kompatibelt med PDF/A 1a
type: docs
weight: 130
url: /sv/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Lär dig hur man konverterar Excel filer till PDF/A kompatibla PDF filer med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

PDF/A är en unik version av PDF utformad för långsiktig arkivering av dokument. PDF/A är en ISO-standardiserad version av Portable Document Format (PDF) som är ett arkivformat för PDF som inbäddar alla teckensnitt som används i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuda funktioner, såsom teckensnittslänkning (jämfört med teckensnittsinbäddning) och kryptering. Aspose.Cells for JavaScript via C++ gör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Denna guide beskriver hur du sparar arbetsboken till en PDF/A-kompatibel (PDF/A-1a) PDF-fil.  

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**  

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) för att ställa in olika attribut för konverteringen. Att ställa in olika egenskaper för klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) ger dig kontroll över utskrift, typsnitt, säkerhet och kompressionsinställningar för den valda PDF-filen. Den viktigaste egenskapen är [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--), som gör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer.  

Följande exempel visar hur man konverterar en Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se dess [output PDF](outputCompliancePdfA1a.pdf) samt skärmbilder för referens.  

## **Skärmdump**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
