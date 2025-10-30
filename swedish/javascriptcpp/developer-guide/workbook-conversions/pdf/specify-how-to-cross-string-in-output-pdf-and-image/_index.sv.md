---
title: Ange hur man korsar strängar i utmatad PDF och bild med JavaScript via C++
linktitle: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 120
url: /sv/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lär dig att kontrollera textöverflöd i utgående PDF/Bild genom att specificera korsreferenstypen med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

När en cell innehåller text eller en sträng men är större än cellens bredd, flödar strängen ut om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil till PDF/Bild kan du kontrollera detta överflöd genom att ange korsningstypen med [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Den har följande värden:

- **TextCrossType.Default**: Visar text som MS Excel, vilket beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller så kommer den att skäras av.

- **TextCrossType.CrossKeep**: Visa strängen som MS Excel-exporterar till PDF/Bild.

- **TextCrossType.CrossOverride**: Visa all text genom att korsar andra celler och åsidosätter texten i korsade celler.

- **TextCrossType.StrictInCell**: Visar endast strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande kod laddar standadexempel fil och sparar den i PDF/Bild-format genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Standadexempel fil och utdatafiler kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Exempelkod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
