---
title: Caricamento e gestione di file Excel, OpenOffice, Json, Csv e Html
linktitle: Aprire i file
type: docs
weight: 20
url: /it/javascript-cpp/loading-saving-and-managing/
description: Con Aspose.Cells, è semplice creare, aprire e gestire file Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht e XPS usando JavaScript tramite C++.
---

{{% alert color="primary" %}}

Con Aspose.Cells, è semplice creare, aprire e gestire file Excel, ad esempio per recuperare dati, o usare un modello di designer per accelerare lo sviluppo.

{{% /alert %}}

## **Creazione di un nuovo foglio di lavoro**
Il seguente esempio crea un nuovo workbook da zero.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Apertura e salvataggio di un file**
Con Aspose.Cells, è semplice aprire, salvare e gestire file Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Diversi modi per aprire i file](/cells/it/javascript-cpp/different-ways-to-open-files/)
- [Filtra i nomi definiti durante il caricamento del foglio di lavoro](/cells/it/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Filtra gli oggetti durante il caricamento del foglio di lavoro o del foglio di calcolo](/cells/it/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrare il tipo di dati durante il caricamento del libro di lavoro da file modello](/cells/it/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Ottieni avvisi durante il caricamento del file Excel](/cells/it/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Carica il file Excel di origine senza grafici](/cells/it/javascript-cpp/load-source-excel-file-without-charts/)
- [Carica fogli di lavoro specifici in un libro di lavoro](/cells/it/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Carica il libro di lavoro con il formato di carta della stampante specificato](/cells/it/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Apertura di file di diverse versioni di Microsoft Excel](/cells/it/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Apertura di file con formati diversi](/cells/it/javascript-cpp/opening-files-with-different-formats/)
- [Ottimizzazione dell'utilizzo della memoria durante il lavoro con file grandi che contengono grandi set di dati](/cells/it/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leggi i fogli di calcolo di Numbers sviluppati da Apple Inc. utilizzando Aspose.Cells](/cells/it/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo](/cells/it/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilizzo di API LightCells](/cells/it/javascript-cpp/using-lightcells-api/)
- [Convertire CSV in JSON](/cells/it/javascript-cpp/convert-csv-to-json/)
- [Converti Excel in JSON](/cells/it/javascript-cpp/convert-excel-to-json/)
- [Convertire JSON in CSV](/cells/it/javascript-cpp/convert-json-to-csv/)
- [Converti JSON in Excel](/cells/it/javascript-cpp/convert-json-to-excel/)
- [Converti Excel in Html](/cells/it/javascript-cpp/convert-excel-to-html/)
