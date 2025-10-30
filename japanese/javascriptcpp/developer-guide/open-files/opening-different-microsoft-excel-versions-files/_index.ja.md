---
title: JavaScriptを使用してC++経由で異なるMicrosoft Excelバージョンのファイルを開く
linktitle: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: この記事は、C++経由でAspose.Cells for JavaScriptを使用して異なるExcelバージョンのファイルを開く方法について説明しています。
keywords: JavaScriptを使用してC++経由で異なるMicrosoft Excelファイルを開く方法、暗号化されたExcelファイルをJavaScript経由でC++で開くにはどうすればよいか
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く方法**

アプリケーションは通常、Microsoft Excel 95、97、またはMicrosoft Excel 2007/2010/2013/2016/2019やOffice 365で作成されたさまざまなバージョンのMicrosoft Excelファイルを開く必要があります。XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimitedまたはTSV、CSV、ODSなど、多くの形式のいずれかでロードする必要があります。コンストラクターを使用するか、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--)タイプ属性を指定して、[**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype)列挙体を使用してフォーマットを指定します。

[**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype)列挙体には多くの事前定義されたファイル形式が含まれており、その一部は以下に示します。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|Csv|はCSVファイルを表します
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します
|Xlsm|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します
|Xltx|はExcel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します
|Xltm|はExcel 2007/2010/2013/2016/2019およびOffice 365マクロ有効なXLTMファイルを表します
|Xlsb|はExcel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します
|SpreadsheetML|はSpreadsheetMLファイルを表します
|Tsv|はタブ区切りの値ファイルを表します
|TabDelimited|はタブ区切りのテキストファイルを表します
|Ods|はODSファイルを表します
|Html|はHTMLファイルを表します
|Mhtml|はMHTMLファイルを表します

### **Microsoft Excel 95/5.0ファイルを開く**

Microsoft Excel 95/5.0ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)クラスの関連属性を設定します。この機能のテスト用サンプルファイルは以下のリンクからダウンロードできます：

[Excel95 File](Excel95.xls)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel95_5.0.xls Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions1 = new LoadOptions(LoadFormat.Auto);

            // Create a Workbook object and opening the file from the stream
            const wbExcel95 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);
            console.log("Microsoft Excel 95/5.0 workbook opened successfully!");

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 95/5.0 workbook opened successfully!</p>';
        });
    </script>
</html>
```

### **Microsoft Excel 97-2003ファイルを開く**

Microsoft Excel 97 - 2003ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)クラスの関連属性を設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel 97-2003 Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel 97-2003 (.xls) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions1 = new LoadOptions(LoadFormat.Excel97To2003);
            const wbExcel97 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 97 - 2003 workbook opened successfully!</p>';

            const outputData = wbExcel97.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019、またはOffice 365のフォーマット（XLSXまたはXLSB）を開くには、ファイルパスを指定します。さらに、[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)クラスの関連属性/オプションを設定することもできます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Open Excel 2007 Xlsx Example</title>
    </head>
    <body>
        <h1>Open Excel 2007 Xlsx Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 2007 - Office365 workbook opened successfully!</p>';

            // Save the workbook back to a downloadable file (unchanged content)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book_Excel2007_output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';
        });
    </script>
</html>
```

### **暗号化されたExcelファイルを開く**

Microsoft Excelで暗号化されたExcelファイルを作成することが可能です。暗号化されたファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)を使用し、その属性とオプション（例：パスワードの設定）をテンプレートファイルに設定します。
この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[Encrypted Excel](EncryptedExcel.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Encrypted Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions
            const loadOptions = new LoadOptions();

            // Specify the password (converted from setPassword to property assignment)
            loadOptions.password = "1234";

            // Create a Workbook object opening the file from the uploaded bytes with loadOptions
            const wbEncrypted = new Workbook(new Uint8Array(arrayBuffer), loadOptions);
            console.log("Encrypted excel file opened successfully!");

            // Save the workbook so user can download it (using Excel97To2003 format for .xls)
            const outputData = wbEncrypted.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            // Use original name with a prefix to indicate it's been opened
            const originalName = file.name || 'output.xls';
            downloadLink.download = 'opened_' + originalName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Encrypted Excel file opened successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。
