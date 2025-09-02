---
title: Convert CSV, TSV and TXT to Excel with JavaScript via C++
linktitle: Convert CSV, TSV and TXT to Excel
type: docs
weight: 30
url: /javascript-cpp/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}
Using Aspose.Cells, you can convert CSV files to Excel, OpenOffice, PDF, JSON, and many other formats.
{{% /alert %}}

## **Opening CSV Files**

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

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

## **Opening CSV files and replacing invalid characters**

In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API which is demonstrated in the code example given below.

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


### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

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

### **Opening Tab Delimited Files**

Tab delimited (Text) files contain spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

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

### **Opening Tab-Separated Values (TSV) Files**

Tab-separated values (TSV) files contain spreadsheet data but without any formatting. It is the same as a Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

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

## **Advance topics**
- [Load or Import CSV file with Formulas](/cells/javascript-cpp/load-or-import-csv-file-with-formulas/)
- [Reading CSV File with Multiple Encodings](/cells/javascript-cpp/reading-csv-file-with-multiple-encodings/)