---
title: Specifica come attraversare la stringa nel PDF di output e nelle immagini con JavaScript via C++
linktitle: Specifica come incrociare la stringa in PDF ed immagine di output
type: docs
weight: 120
url: /it/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Impara a controllare il traboccare del testo nel PDF/Immagine di uscita specificando il tipo di attraversamento usando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o una stringa ma è più larga della larghezza della cella, allora la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in PDF/Image, puoi controllare questo trabocco specificando il tipo di attraversamento usando l'enumerazione [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Ha i seguenti valori:

- **TextCrossType.Default**: Visualizza il testo come MS Excel che dipende dalla cella successiva. Se la cella successiva è nulla, la stringa attraverserà o sarà troncata.

- **TextCrossType.CrossKeep**: visualizza la stringa come MS Excel esportando in PDF/Immagine.

- **TextCrossType.CrossOverride**: visualizza tutto il testo attraversando le altre celle e sovrascrive il testo delle celle attraversate.

- **TextCrossType.StrictInCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specificare come incrociare la stringa nel PDF / Immagine di output utilizzando TextCrossType**

Il seguente esempio di codice carica il file Excel di esempio e lo salva in formato PDF/Immagine specificando vari [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Il file Excel di esempio e i file di output possono essere scaricati dai link seguenti:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Codice di esempio

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
