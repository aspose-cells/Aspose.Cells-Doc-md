---
title: Konvertera CSV, TSV och TXT till Excel med JavaScript via C++
linktitle: Konvertera CSV, TSV och TXT till Excel
type: docs
weight: 30
url: /sv/javascript-cpp/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}
Med Aspose.Cells kan du konvertera CSV-filer till Excel, OpenOffice, PDF, JSON och många andra format.
{{% /alert %}}

## **Öppning av CSV-filer**

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open CSV with Aspose.Cells (Browser)</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Open CSV</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat (CSV)
            const loadOptions4 = new LoadOptions(LoadFormat.Csv);

            // Create a Workbook object and open the file from the uploaded file buffer
            const wbCSV = new Workbook(new Uint8Array(arrayBuffer), loadOptions4);

            document.getElementById('result').innerHTML = '<p style="color: green;">CSV file opened successfully!</p>';
            document.getElementById('result').innerHTML += `<p>Worksheets count: ${wbCSV.worksheets.count}</p>`;
        });
    </script>
</html>
```

## **Öppna CSV-filer och ersätt ogiltiga tecken**

När en CSV-fil med specialtecken öppnas i Excel, ersätts tecknen automatiskt. Samma gäller för Aspose.Cells API som demonstreras i kodexemplet nedan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Load Example</title>
    </head>
    <body>
        <h1>CSV Load Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Configure TxtLoadOptions
            const options = new AsposeCells.TxtLoadOptions();
            options.separator = ",";
            options.loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData);
            options.checkExcelRestriction = false;
            options.convertNumericData = false;
            options.convertDateTimeData = false;

            // Load CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet and its name
            const worksheet = workbook.worksheets.get(0);
            const sheetName = worksheet.name;
            const nameLength = sheetName.length;

            console.log(sheetName);
            console.log(nameLength);
            console.log("CSV file opened successfully!");

            document.getElementById('result').innerHTML =
                `<p>Worksheet name: ${sheetName}</p>` +
                `<p>Name length: ${nameLength}</p>` +
                `<p style="color: green;">CSV file opened successfully!</p>`;
        });
    </script>
</html>
```


### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV to Text Example</title>
    </head>
    <body>
        <h1>CSV to Text Conversion Example</h1>
        <input type="file" id="fileInput" accept=".csv,.txt" />
        <button id="runExample">Convert and Download</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, EncodingType } = AsposeCells;

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
            txtLoadOptions.encoding = EncodingType.UTF8;

            // Create a Workbook object and open the file from the uploaded file's bytes
            const wb = new Workbook(new Uint8Array(arrayBuffer), txtLoadOptions);

            // Save file as CSV (download as .txt)
            const outputData = wb.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

### **Öppning av tabbehållna filer**

Tab-separerade (Text) filer innehåller kalkylbladsdata men utan formatering. Data är arrangerad i rader och kolumner som i tabeller och kalkylblad. En fil med tab-separering är i princip en speciell typ av platt textfil med ett tab-tecken mellan varje kolumn.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Tab Delimited Example</title>
    </head>
    <body>
        <h1>Open Tab-Delimited File</h1>
        <input type="file" id="fileInput" accept=".txt,.csv,.tsv,.xls,.xlsx" />
        <button id="runExample">Open Tab Delimited</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a tab-delimited text file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat (TabDelimited)
            const loadOptions = new LoadOptions(LoadFormat.TabDelimited);

            // Create a Workbook object and open the file from the uploaded data using LoadOptions
            const wbTabDelimited = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Tab delimited file opened successfully!</p>';

            // Save the workbook to XLSX and provide a download link
            const outputData = wbTabDelimited.save(SaveFormat.Xlsx);
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

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Värden separerade med tabb (TSV) innehåller kalkylbladsdata men utan formatering. Det är samma sak som en Tab-separerad fil där data är arrangerad i rader och kolumner som i tabeller och kalkylblad.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TSV Read Example</title>
    </head>
    <body>
        <h1>Read TSV Cell Example</h1>
        <input type="file" id="fileInput" accept=".tsv,.txt" />
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

            // Instantiate LoadOptions with TSV format
            const loadOptions = new LoadOptions(LoadFormat.Tsv);

            // Create Workbook from uploaded file with loadOptions
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Using the first sheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("C3");

            const outputText = `Cell Name: ${cell.name} Value: ${cell.stringValue}`;
            console.log(outputText);
            document.getElementById('result').innerHTML = `<p style="color: green;">${outputText}</p>`;
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Läs in eller importera CSV-fil med formler](/cells/sv/javascript-cpp/load-or-import-csv-file-with-formulas/)
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/javascript-cpp/reading-csv-file-with-multiple-encodings/)
