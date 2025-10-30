---
title: Aprire file con formati diversi con JavaScript tramite C++
linktitle: Apertura dei file con formati diversi
type: docs
weight: 30
url: /it/javascript-cpp/opening-files-with-different-formats/
description: L API Aspose.Cells for JavaScript tramite C++ permette di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: Aprire file xlsx, aprire file html, leggere file fods, leggere file ods, leggere file sxc, aprire file csv, Separato da tabulazione, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells, puoi aprire file con formati diversi. **Aspose.Cells** può aprire una vasta gamma di formati di file come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), file delimitati da tabulazione o valori separati da tab (TSV), ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/javascript-cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con formati diversi come SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazione o valori separati da tabulazione (TSV), file ODS. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per l'apertura di file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo che includono tutte le informazioni, come formattazione, formule, ecc. Dalla versione Microsoft Excel XP, viene aggiunta un'opzione di esportazione XML che consente di esportare i fogli di calcolo in file SpreadsheetML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open SpreadsheetML (Book3.xml)</h1>
        <input type="file" id="fileInput" accept=".xml,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an SpreadsheetML (.xml) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.SpreadsheetML);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">SpreadSheetML file opened successfully!</p>';
            console.log("SpreadSheetML file opened successfully!");
        });
    </script>
</html>
```

### **Apertura dei file HTML**

Aspose.Cells consente di aprire un file HTML in un oggetto Workbook. Il file HTML dovrebbe essere orientato a Microsoft Excel, cioè, MS-Excel dovrebbe essere in grado di aprirlo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert HTML to XLSX Example</h1>
        <input type="file" id="fileInput" accept=".html,.htm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an HTML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);

            // Create a Workbook object and opening the file from the uploaded file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the XLSX file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSX File';

            resultEl.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

### **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record dove i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ogni colonna è separata dal carattere virgola e quotata con il carattere virgolette doppie. Se un valore di campo contiene un carattere virgolette doppie, viene escapato con una coppia di caratteri virgolette doppie. Puoi anche usare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Open Example</title>
    </head>
    <body>
        <h1>Aspose.Cells CSV Open Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Open CSV</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions4 = new LoadOptions(LoadFormat.Csv);

            // Create a Workbook object and open the file from the uploaded data
            const wbCSV = new Workbook(new Uint8Array(arrayBuffer), loadOptions4);

            document.getElementById('result').innerHTML = '<p style="color: green;">CSV file opened successfully!</p>';
        });
    </script>
</html>
```

#### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto dall'API Aspose.Cells che è mostrata nell'esempio di codice qui sotto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with TxtLoadOptions Example</title>
    </head>
    <body>
        <h1>Load CSV with TxtLoadOptions Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtLoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.separator = ';';
                loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.CellData);
                loadOptions.checkExcelRestriction = false;
                loadOptions.convertNumericData = false;
                loadOptions.convertDateTimeData = false;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const worksheet = workbook.worksheets.get(0);
                const sheetName = worksheet.name;
                const nameLength = sheetName.length;

                console.log(sheetName);
                console.log(nameLength);
                console.log("CSV file opened successfully!");

                document.getElementById('result').innerHTML = `<p>Worksheet Name: ${sheetName}</p><p>Name Length: ${nameLength}</p><p style="color: green;">CSV file opened successfully!</p>`;
            });
        });
    </script>
</html>
```

### **Apertura dei file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV to Text Example</title>
    </head>
    <body>
        <h1>Convert CSV to Text Example</h1>
        <input type="file" id="fileInput" accept=".csv,.txt" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Text File's LoadOptions
            const txtLoadOptions = new TxtLoadOptions();

            // Specify the separator
            txtLoadOptions.separator = ",";

            // Specify the encoding type
            txtLoadOptions.encoding = AsposeCells.EncodingType.UTF8;

            // Create a Workbook object and open the file from the uploaded data
            const wb = new Workbook(new Uint8Array(arrayBuffer), txtLoadOptions);

            // Save file as text and provide download link
            const outputData = wb.save(SaveFormat.Text);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

### **Apertura dei file delimitati da tabulazione**

I file delimitati da tabulazione (Testo) contengono dati di fogli di calcolo senza alcuna formattazione. I dati sono disposti in righe e colonne come in tabelle e fogli di calcolo. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Open Tab Delimited</title>
    </head>
    <body>
        <h1>Open Tab Delimited Example</h1>
        <input type="file" id="fileInput" accept=".txt,.csv,.tsv" />
        <button id="runExample">Open File</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a tab-delimited (.txt/.tsv) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.TabDelimited);

            // Create a Workbook object and open the file from the uploaded file buffer
            const wbTabDelimited = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Tab delimited file opened successfully!</p>';
        });
    </script>
</html>
```

### **Apertura dei file di valori separati da tabulazione (TSV)**

Il file di valori separati da tabulazione (TSV) contiene dati di fogli di calcolo ma senza alcuna formattazione. È uguale a un file delimitato da tabulazioni dove i dati sono disposti in righe e colonne come in tabelle e fogli di calcolo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TSV Load Example</title>
    </head>
    <body>
        <h1>TSV Load Example</h1>
        <input type="file" id="fileInput" accept=".tsv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a TSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Tsv);

            // Create a Workbook object and opening the file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("C3");

            // Display cell name and value
            document.getElementById('result').innerHTML = `<p>Cell Name: ${cell.name} Value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con estensione SXC. Il file SXC è anche usato per i file di fogli di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere file SXC come dimostrato dal seguente esempio di codice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read SXC Cell Example</h1>
        <input type="file" id="fileInput" accept=".sxc" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an SXC file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Sxc);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Using the first worksheet in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("C3");

            // Display cell name and string value
            resultDiv.innerHTML = `<p>Cell Name: ${cell.name} Value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Apertura dei file FODS**

Il file FODS è un foglio di calcolo salvato in XML OpenDocument senza compressione. Aspose.Cells può leggere file FODS come dimostrato dal seguente esempio di codice.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Open FODS</title>
    </head>
    <body>
        <h1>Open FODS Example</h1>
        <input type="file" id="fileInput" accept=".fods" />
        <button id="runExample">Open FODS File</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select a FODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Fods);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">FODS file opened successfully!</p>';
        });
    </script>
</html>
```
