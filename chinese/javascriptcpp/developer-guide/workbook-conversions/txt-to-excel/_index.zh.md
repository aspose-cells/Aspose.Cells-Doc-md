---
title: 使用JavaScript通过C++将CSV、TSV和Txt转换为Excel
linktitle: 将 CSV、TSV 和 TXT 转换为 Excel
type: docs
weight: 30
url: /zh/javascript-cpp/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}
 使用 Aspose.Cells，可以将 CSV 文件转换为 Excel、OpenOffice、PDF、JSON 等多种格式。
{{% /alert %}}

## **打开 CSV 文件**

逗号分隔值（CSV）文件包含记录，其中值由逗号分隔。 数据存储为表格，其中每列由逗号字符分隔并由双引号字符引用。 如果字段值包含双引号字符，则用一对双引号字符进行转义。 您还可以使用 Microsoft Excel 将电子表格数据导出到 CSV。

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

## **打开 CSV 文件并替换无效字符**

在Excel中，打开带有特殊字符的CSV文件时，字符会自动被替换。Aspose.Cells API也会执行相同操作，以下代码示例演示了这一点。

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


### **使用自定义分隔符打开文本文件**

文本文件用于在不格式化的情况下保存电子表格数据。 文件是一种可以具有一些自定义分隔符的纯文本文件。

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

### **打开制表符分隔文件**

选项卡分隔（文本）文件包含电子表格数据，但没有任何格式。数据以类似表格和电子表格的行和列进行排列。基本上，选项卡分隔文件是一种特殊的纯文本文件，每列之间用制表符分隔。

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

### **打开制表符分隔数值（TSV）文件**

Tab分隔值（TSV）文件包含电子表格数据，但没有任何格式。它与Tab分隔文件相同，数据以行和列的形式排列。

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

## **高级主题**
- [加载或导入带公式的CSV文件](/cells/zh/javascript-cpp/load-or-import-csv-file-with-formulas/)
- [读取带有多种编码的CSV文件](/cells/zh/javascript-cpp/reading-csv-file-with-multiple-encodings/)
