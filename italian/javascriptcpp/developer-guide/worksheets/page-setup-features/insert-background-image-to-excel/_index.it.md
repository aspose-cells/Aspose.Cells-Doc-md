---
title: Inserisci immagine di sfondo in Excel con JavaScript tramite C++
linktitle: Inserire un immagine di sfondo in Excel
type: docs
weight: 90
url: /it/javascript-cpp/insert-background-image-to-excel/
description: "Come inserire un immagine di sfondo in Excel usando Aspose.Cells for JavaScript tramite C++."
---

{{% alert color="primary" %}} 

Puoi rendere un foglio di lavoro più accattivante aggiungendo un'immagine come sfondo del foglio. Questa funzionalità può essere molto efficace se hai una grafica aziendale speciale che aggiunge un tocco di sfondo senza oscurare i dati nel foglio. Puoi impostare l'immagine di sfondo per un foglio utilizzando l'API Aspose.Cells.

{{% /alert %}} 

## **Impostare lo sfondo del foglio in Microsoft Excel**

Impostare un'immagine di sfondo di un foglio in Microsoft Excel (ad esempio, Microsoft Excel 2019):

1. Dal menu **Layout di pagina**, individuare l'opzione **Imposta pagina** e fare clic sull'opzione **Sfondo**.
1. Seleziona un'immagine da impostare come sfondo del foglio.

   **Impostazione di uno sfondo del foglio**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Impostare lo sfondo del foglio con Aspose.Cells for JavaScript tramite C++**

Il codice di seguito imposta un'immagine di sfondo utilizzando un'immagine da un flusso.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## Articoli correlati

- [Lavorare con lo sfondo nei file ODS](/cells/it/javascript-cpp/working-with-background-in-ods-files/)
