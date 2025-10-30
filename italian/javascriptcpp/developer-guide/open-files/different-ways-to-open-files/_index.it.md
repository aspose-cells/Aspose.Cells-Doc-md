---
title: Modi diversi per aprire file con JavaScript tramite C++
linktitle: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/javascript-cpp/different-ways-to-open-files/
description: Questo articolo spiega come aprire un file Excel utilizzando Aspose.Cells for JavaScript tramite API C++.
keywords: JavaScript Aprire un file Excel senza Excel, Come aprire un file Excel usando JavaScript.
---

{{% alert color="primary" %}}

Con Aspose.Cells, è semplice aprire file, ad esempio, per recuperare dati, o usare un modello di progettazione per accelerare il processo di sviluppo.

{{% /alert %}}

## **Come aprire un file Excel tramite un percorso**

Gli sviluppatori possono aprire un file Microsoft Excel usando il percorso del file sul computer locale specificandolo nel costruttore della classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Basta passare il percorso come *stringa* nel costruttore. Aspose.Cells rileva automaticamente il tipo di formato del file.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Open Workbook</title>
    </head>
    <body>
        <h1>Open Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook1 = new Workbook(new Uint8Array(arrayBuffer));
            console.log("Workbook opened using file successfully!");

            // Display basic info about the opened workbook
            document.getElementById('result').innerHTML = `<p style="color: green;">Workbook opened successfully! Worksheets count: ${workbook1.worksheets.count}</p>`;
        });
    </script>
</html>
```

## **Come aprire un file Excel tramite uno stream**

È anche semplice aprire un file Excel come stream. Per farlo, usa una versione sovraccaricata del costruttore che prende l'oggetto *Stream* che contiene il file.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Stream to Workbook</title>
    </head>
    <body>
        <h1>Open Excel Stream Example (Browser)</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file as an ArrayBuffer (equivalent to reading a stream in JavaScript)
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Example modification: set A1 to indicate file was loaded (demonstrates cell value setter conversion)
            const cell = worksheet.cells.get(0, 0);
            cell.value = "Loaded from stream";

            // Save the modified workbook as Excel97-2003 (.xls) since original was .xls in JavaScript example
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Come aprire un file con solo dati**

Per aprire un file con solo dati, usa le classi [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) e [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) per impostare gli attributi e le opzioni correlate delle classi per il file modello da caricare.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells LoadOptions Example</title>
    </head>
    <body>
        <h1>LoadOptions with LoadFilter Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Set LoadFilter property to load only data & cell formatting
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.CellData);

            // Create a Workbook object and opening the file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Indicate success
            document.getElementById('result').innerHTML = '<p style="color: green;">File data imported successfully!</p>';

            // Prepare download of the loaded workbook (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Come caricare solo fogli visibili**

Mentre si carica un [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), a volte potrebbe essere sufficiente avere solo i dati nelle fogli visibili di un workbook. Aspose.Cells permette di saltare i dati nelle fogli invisibili durante il caricamento di un workbook. Per farlo, crea una funzione personalizzata che eredita dalla classe [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) e passa la sua istanza alla proprietà [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create if no file selected)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, Utils } = AsposeCells;

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
            let bytes;
            let createdOutputData;

            if (fileInput.files.length) {
                // Load from user-selected file
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                bytes = new Uint8Array(arrayBuffer);
            } else {
                // Create a sample workbook in memory
                const createWorkbook = new Workbook();

                // Put some data in first cell of all 3 sheets
                createWorkbook.worksheets.get("Sheet1").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet2").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet3").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.get("Sheet3").isVisible = false;

                // Save the created workbook to bytes
                createdOutputData = createWorkbook.save(SaveFormat.Xlsx);
                bytes = createdOutputData instanceof Uint8Array ? createdOutputData : new Uint8Array(createdOutputData);

                // Provide download link for the created workbook
                const blob = new Blob([bytes]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Created Excel File';
            }

            // Prepare load options and load filter
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter();

            // Load the workbook using the bytes and load options
            const loadWorkbook = new Workbook(bytes, loadOptions);

            // Read values from A1 of Sheet1, Sheet2, Sheet3
            const sheet1A1 = loadWorkbook.worksheets.get("Sheet1").cells.get("A1").value;
            const sheet2A1 = loadWorkbook.worksheets.get("Sheet2").cells.get("A1").value;
            const sheet3A1 = loadWorkbook.worksheets.get("Sheet3").cells.get("A1").value;

            // Log to console and show in the page
            console.log(`Sheet1: A1: ${sheet1A1}`);
            console.log(`Sheet2: A1: ${sheet2A1}`);
            console.log(`Sheet3: A1: ${sheet3A1}`);

            document.getElementById('result').innerHTML =
                `<p>Sheet1: A1: ${sheet1A1}</p>
                 <p>Sheet2: A1: ${sheet2A1}</p>
                 <p>Sheet3: A1: ${sheet3A1}</p>
                 <p style="color: green;">Operation completed successfully!</p>`;
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>CustomLoad Example</h1>
        <p>Select an Excel file to evaluate sheets with CustomLoad.startSheet()</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadDataFilterOptions } = AsposeCells;

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

        class CustomLoad {
            startSheet(sheet) {
                if (sheet.isVisible()) {
                    // Load everything from visible worksheet
                    this.loadDataFilterOptions = LoadDataFilterOptions.All;
                } else {
                    // Load nothing
                    this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const custom = new CustomLoad();

            let html = '<h2>CustomLoad Results</h2>';
            html += '<ul>';

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sheet = workbook.worksheets.get(i);
                custom.startSheet(sheet);
                html += `<li><strong>${sheet.name}</strong>: loadDataFilterOptions = ${custom.loadDataFilterOptions}</li>`;
            }

            html += '</ul>';
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file non nativi di Excel o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) usando Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Ci sono buone possibilità che il costruttore [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) possa generare *OutOfMemoryError* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile è insufficiente per caricare completamente il foglio di calcolo in memoria; pertanto, il foglio di calcolo deve essere caricato abilitando le Preferenze di Memoria.

{{% /alert %}}
