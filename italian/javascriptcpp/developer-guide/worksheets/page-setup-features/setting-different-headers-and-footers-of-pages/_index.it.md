---
title: Impostare intestazioni e piè di pagina diversi per pagine diverse con JavaScript tramite C++
linktitle: Impostazione di diversi intestazioni e piè di pagina per pagine diverse
type: docs
weight: 35
url: /it/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Questo articolo fornisce codice di esempio che mostra come impostare automaticamente intestazioni e piè di pagina della configurazione pagina del foglio Excel usando Aspose.Cells for JavaScript tramite C++. Imposta intestazioni e piè di pagina per prime, dispari e pagine pari.
keywords: impostare intestazione piè di pagina in excel prima pagina JavaScript tramite C++, impostare intestazione piè di pagina pagine dispari JavaScript tramite C++, impostare intestazione piè di pagina pagine pari JavaScript tramite C++
---

{{% alert color="primary" %}}

 MS Excel supporta la possibilità di impostare intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e le pagine pari dall'Excel 2007.
Aspose.Cells for JavaScript tramite C++ supporta la stessa funzionalità.

{{% /alert %}}

## **Impostazione di Intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su **Layout di pagina > Titoli di stampa > Intestazione/piè di pagina**.
1. Seleziona **Pagine dispari e pari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## ** Impostare intestazioni e piè di pagina diversi con Aspose.Cells for JavaScript tramite C++**

Aspose.Cells si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) e [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Inserisci intestazioni e piè di pagina diversi.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
