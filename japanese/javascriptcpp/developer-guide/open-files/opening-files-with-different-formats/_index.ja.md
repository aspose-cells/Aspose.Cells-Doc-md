---
title: JavaScriptを使用してC++経由で異なるフォーマットのファイルを開く
linktitle: さまざまな形式のファイルを開く
type: docs
weight: 30
url: /ja/javascript-cpp/opening-files-with-different-formats/
description: Aspose.Cells for JavaScriptをC++ APIで使用すると、XLSX、HTML、CSV、ODS、TSV、SXC、FODSなどのさまざまなフォーマットを開いたり読んだりできます。
keywords: xlsx ファイルを開く、html ファイルを開く、fods ファイルを読む、ods ファイルを読む、sxc ファイルを読む、csv ファイルを開く、タブ区切り、SpreadsheetML、tsv、mhtml
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、さまざまなフォーマットのファイルを開くことができます。**Aspose.Cells**は、Microsoft Excelのスプレッドシート（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはTSVファイルなどを開くことが可能です。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイルフォーマット](https://docs.aspose.com/cells/javascript-cpp/supported-file-formats/)

{{% /alert %}}

## **異なるフォーマットのファイルを開く**

Aspose.Cells は、SpreadsheetML、コンマ区切り値（CSV）、タブ区切りまたはタブ区切り値（TSV）、ODS ファイルなどの異なる形式のスプレッドシートファイルを開くことができます。このようなファイルを開くには、開く異なる Microsoft Excel バージョンのファイルを開くときと同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetMLファイルは、書式設定や数式など、スプレッドシートに関するすべての情報を含むXMLによるスプレッドシートの表現です。Microsoft Excel XP以降に、ExcelにはスプレッドシートをSpreadsheetMLファイルにエクスポートするXMLエクスポートオプションが追加されました。

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

### **HTML ファイルを開く**

Aspose.Cellsは、HTMLファイルをWorkbookオブジェクトに開くことを可能にします。HTMLファイルはMicrosoft Excel向きである必要があります。つまり、MS-Excelが開くことができる必要があります。

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

### **CSV ファイルを開く**

カンマ区切り値（CSV）ファイルは、値がカンマで区切られたレコードを含みます。データは表として保存され、各列はカンマ文字で区切られ、二重引用符で囲まれています。フィールド値に二重引用符が含まれる場合、それは二重引用符のペアでエスケープされます。Microsoft Excelを使用してスプレッドシートデータをCSVにエクスポートすることもできます。

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

#### **CSV ファイルを開くと無効な文字を置換する**

Excelで、特殊文字を含むCSVファイルを開くと、文字が自動的に置き換えられます。Aspose.Cells APIも同様に動作し、以下のコード例で示します。

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

### **カスタム区切り記号を使用してテキストファイルを開く**

テキストファイルは、書式なしでスプレッドシートデータを保持するために使用されます。この種のファイルは、カスタマイズされた区切り記号を持つプレーンテキストファイルです。

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

### **タブ区切りファイルを開く**

タブ区切り（テキスト）ファイルはスプレッドシートのデータを含みますが、フォーマットはありません。データは表やスプレッドシートのように行と列に配置され、基本的には各列の間にタブが挿入されたプレーンテキストファイルです。

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

### **タブ区切り値（TSV）ファイルを開く**

TSV（タブ区切り値）ファイルは、書式設定なしのスプレッドシートデータを含みます。これは、タブ区切りファイルと同じで、データは表やスプレッドシートのように行と列に配置されます。

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

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、数式、チャート、関数、マクロをサポートします。このソフトウェアで作成されたスプレッドシートはSXC拡張子で保存されます。SXCファイルは、OpenOffice.org Calcのスプレッドシートファイルにも使用されます。Aspose.CellsはSXCファイルを読み取ることができます（以下のコード例による）。

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

### **FODSファイルを開く**

FODSファイルは、圧縮なしのOpenDocument XMLとして保存されたスプレッドシートです。Aspose.Cellsは、FODSファイルを読み取ることもできます（以下のコード例による）。

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
