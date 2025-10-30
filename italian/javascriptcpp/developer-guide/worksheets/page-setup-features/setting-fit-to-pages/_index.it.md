---
title: Come stampare Excel come pagine adattate in larghezza e altezza con JavaScript tramite C++
linktitle: Come stampare Excel in pagine larghe e alte adattate
type: docs
weight: 200
url: /it/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Questo articolo mostra come impostare FitToPagesWide e FitToPagesTall usando Aspose.Cells for JavaScript tramite C++.
keywords: JavaScript tramite C++ Come impostare FitToPagesWide e FitToPagesTall, Come aggiungere FitToPagesWide e FitToPagesTall in JavaScript, Come impostare FitToPagesWide e FitToPagesTall in Excel, Come eliminare FitToPagesWide e FitToPagesTall in Excel, Come stampare Excel come pagine adattate in larghezza e altezza, Come stampare foglio di lavoro come una pagina, Come stampare tutte le colonne del foglio di lavoro in una sola pagina.
---

## **Introduzione**

Le impostazioni FitToPagesWide e FitToPagesTall sono usate nelle applicazioni di fogli di calcolo (come Microsoft Excel) per controllare come viene scalato un foglio di calcolo durante la stampa. Queste impostazioni aiutano a garantire che il risultato stampato si adatti a un numero specificato di pagine, sia orizzontalmente che verticalmente. Ecco una spiegazione di ogni impostazione:

1. FitToPagesWide: questa impostazione specifica il numero di pagine di larghezza in cui il risultato stampato deve adattarsi. Ad esempio, impostando FitToPagesWide su 1 significa che il contenuto sarà ridimensionato per adattarsi a una singola pagina di larghezza, indipendentemente dalla larghezza del foglio di calcolo.
2. FitToPagesTall: Questa impostazione specifica il numero di pagine in altezza in cui il output stampato dovrebbe adattarsi. Ad esempio, impostando FitToPagesTall a 1, il contenuto verrà ridimensionato per adattarsi a un'unica altezza di pagina, indipendentemente dal numero di righe.

## **Perché usare FitToPagesWide e FitToPagesTall**
Ecco alcuni motivi per impostare FitToPagesWide e FitToPagesTall:
1. Controllo del Layout di Stampa: specificando il numero di pagine di larghezza e altezza, puoi garantire che il tuo documento stampato sia facile da leggere e ben organizzato, senza che colonne o righe siano divise in modo inappropriato tra le pagine.
2. Coerenza: Se stai stampando più fogli o report, usare queste impostazioni aiuta a mantenere un formato coerente, rendendo più facile confrontare e analizzare i documenti stampati.
3. Presentazione professionale: Ridimensionando e adattando correttamente i contenuti a un numero specificato di pagine si può ottenere una presentazione dei dati più professionale e curata.

## **Come stampare il file come pagine adattate in larghezza e altezza in Excel**

Per impostare le impostazioni FitToPagesWide e FitToPagesTall in Microsoft Excel, segui questi passaggi:

1. Apri il tuo file Excel e vai sul foglio che desideri stampare.
2. Vai alla scheda Layout di pagina sulla barra multifunzione.
3. Nella sezione Imposta pagina, clicca sulla piccola freccia in basso a destra per aprire la finestra di dialogo Imposta pagina.
4. Nella finestra di dialogo Imposta pagina, vai alla scheda Pagina.
5. Sotto Scala, seleziona l'opzione "Adatta a" e poi specifica il numero di pagine in larghezza e altezza desiderate: inserisci il numero di pagine in larghezza nel primo riquadro (Adatta a x pagine in larghezza). inserisci il numero di pagine in altezza nel secondo riquadro (Adatta a y pagine in altezza).
<br>
<img src="2.png" width=60% />

6. Clicca su OK per applicare le impostazioni.

## ** Come stampare Excel come pagine adattate in larghezza e altezza usando Aspose.Cells for JavaScript tramite C++**

 Per impostare FitToPagesWide e FitToPagesTall in un foglio di lavoro specifico: prima, caricare il [file di esempio](input.xlsx), e poi modificare le proprietà [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) e [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) dell’oggetto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per il foglio desiderato. Ecco un esempio in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Il risultato dell'output:
<br>
<img src="1.png" width=60% />

## ** Come stampare un foglio di lavoro come una pagina usando Aspose.Cells for JavaScript tramite C++**

 Per stampare un foglio di lavoro come una pagina: prima, caricare il [file di esempio](sample.xlsx), e poi impostare la proprietà [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) dell’oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Ecco un esempio in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Il risultato dell'output:
<br>
<img src="3.png" width=60% />

## **Come stampare tutte le colonne del foglio di lavoro in una pagina usando Aspose.Cells for JavaScript via C++**

Per stampare tutte le colonne del foglio di lavoro in una pagina: Prima, carica il [file di esempio](sample.xlsx), e poi devi impostare la proprietà [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) dell'oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Ecco un esempio in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Il risultato dell'output:
<br>
<img src="4.png" width=60% />
