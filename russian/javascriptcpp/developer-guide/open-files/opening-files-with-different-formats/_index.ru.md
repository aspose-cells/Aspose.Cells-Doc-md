---
title: Открытие файлов различных форматов с помощью JavaScript через C++
linktitle: Открытие файлов с различными форматами
type: docs
weight: 30
url: /ru/javascript-cpp/opening-files-with-different-formats/
description: API Aspose.Cells for JavaScript через C++ позволяет открывать/читать различные форматы, такие как XLSX, HTML, CSV, ODS, TSV, SXC, FODS и другие.
keywords: открыть файлы xlsx, открыть файлы html, прочитать файлы fods, прочитать файлы ods, прочитать файлы sxc, открыть файлы csv, Табличный разделитель, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

С помощью Aspose.Cells вы можете открывать файлы разных форматов. **Aspose.Cells** поддерживает широкий спектр форматов, таких как таблицы Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, значения через запятую (CSV), файлы с разделителями табуляции или TSV и другие.

Если вам нужно знать все поддерживаемые форматы файлов, обратитесь к следующим страницам:
[Поддерживаемые форматы файлов](https://docs.aspose.com/cells/javascript-cpp/supported-file-formats/)

{{% /alert %}}

## **Открытие файлов с различными форматами**

Aspose.Cells позволяет разработчикам открывать файлы электронных таблиц различных форматов, такие как SpreadsheetML, файлы, разделенные запятыми (CSV), файлы с разделителями табуляции или табулированные значения (TSV), файлы ODS. Для открытия таких файлов разработчики могут использовать тот же метод, который они используют для открытия файлов различных версий Microsoft Excel.

### **Открытие файлов SpreadsheetML**

Файлы SpreadsheetML — это XML-представление таблиц с полной информацией о форматировании, формулах и др. Начиная с Microsoft Excel XP, добавлена возможность экспорта в XML, которая сохраняет таблицы в виде файлов SpreadsheetML.

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

### **Открытие файлов HTML**

Aspose.Cells позволяет открыть HTML-файл в объекте Workbook. HTML-файл должен быть предназначен для Microsoft Excel, то есть его сможет открыть MS-Excel.

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

### **Открытие файлов CSV**

Файлы Значения, разделённые запятыми (CSV), содержат записи, где значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделён запятой и заключён в двойные кавычки. Если значение поля содержит двойную кавычку, она экранируется парой двойных кавычек. Также можно экспортировать данные таблицы в CSV с помощью Microsoft Excel.

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

#### **Открытие файлов CSV и замена недопустимых символов**

При открытии файла CSV с особыми символами в Excel символы автоматически заменяются. То же самое выполняет API Aspose.Cells, демонстрированный в приведённом ниже коде.

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

### **Открытие текстовых файлов с пользовательским разделителем**

Текстовые файлы используются для хранения данных электронных таблиц без форматирования. Файл является своего рода обычным текстовым файлом, в котором могут быть использованы некоторые настраиваемые разделители.

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

### **Открытие файлов с разделителями табуляции**

Файлы с разделением табуляцией (Text) содержат данные таблицы без форматирования. Данные расположены по строкам и столбцам, как в таблицах и электронных таблицах. По сути, файл с разделителем табуляции — это особый вид обычного текстового файла с табулятором между столбцами.

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

### **Открытие файлов со значениями, разделенными табуляцией (TSV)**

Файл с разделёнными табуляцией (TSV) содержит таблицу данных без форматирования. Аналогичен файлу с разделителем табуляции, где данные расположены по строкам и столбцам, как в таблицах и рабочих листах.

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

### **Открытие файлов SXC**

StarOffice Calc похож на Microsoft Excel и поддерживает формулы, диаграммы, функции и макросы. Таблицы, созданные этим программным обеспечением, сохраняются с расширением SXC. Такой же формат используется для файлов таблиц OpenOffice.org Calc. Aspose.Cells может читать файлы SXC, что демонстрируется в следующем примере кода.

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

### **Открытие файлов FODS**

Файл FODS — это таблица, сохранённая в формате OpenDocument XML без сжатия. Aspose.Cells может читать файлы FODS, что показано в следующем примере кода.

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
