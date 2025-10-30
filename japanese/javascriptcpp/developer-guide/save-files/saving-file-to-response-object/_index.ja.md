---
title: JavaScript経由でC++を使用してレスポンスオブジェクトにファイルを保存する
linktitle: レスポンスオブジェクトへのファイルの保存
type: docs
weight: 50
url: /ja/javascript-cpp/saving-file-to-response-object/
description: Aspose.Cells for JavaScriptを使用して、動的にファイルを生成し、クライアントブラウザに直接送信する方法を学びます。
---

{{% alert color="primary" %}}  

Aspose.Cellsを使用すると、ファイルを操作することができます。この記事では、ファイルをレスポンスオブジェクトに保存するさまざまな方法を説明します。  

{{% /alert %}}  

## **レスポンスオブジェクトへのファイルの保存**  

また、ファイルを動的に生成してクライアントブラウザに直接送信することも可能です。そのためには、次のパラメータを受け取る特別なオーバーロードされた[**Save**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-)メソッドを使用します。  

- JavaScriptレスポンスオブジェクト。  
- ファイル名。  
- [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/)、出力ファイルのcontent-dispositionタイプ。  
- [**SaveOptions**](https://reference.aspose.com/cells/javascript-cpp/saveoptions/)、ファイル形式の種類  

[**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/)列挙体は、ブラウザに送信されるファイルがブラウザ内で直接開くオプションを提供するか、.xls/.xlsxまたは他の拡張子に関連付けられたアプリケーションで開くかを決定します。  

列挙型には、以下の事前定義された保存タイプが含まれています:  

|**タイプ**|**説明**|  
| :- | :- |  
|アタッチメント|スプレッドシートをブラウザに送り、.xls/.xlsx や他の拡張子に関連付けられたアプリケーションで添付ファイルとして開きます|  
|インライン|ドキュメントをブラウザに送り、スプレッドシートをディスクに保存するかブラウザ内で開くオプションを表示します|  

### **XLS ファイル**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Save XLS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions, Utils } = AsposeCells;

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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Simulate the JavaScript "response" which is null in this example
            let response = null;

            if (response != null) {
                // Server-side streaming scenario (not used in browser example)
                // Save in Excel2003 XLS format to response stream with options
                const options = new XlsSaveOptions();
                workbook.save(response, "output.xls", AsposeCells.ContentDisposition.Inline, options);
                response.end();
                document.getElementById('result').innerHTML = '<p style="color: green;">File written to response stream.</p>';
            } else {
                // Browser: save workbook and provide download link
                const options = new XlsSaveOptions();
                const outputData = workbook.save(SaveFormat.Excel97To2003, options);
                const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';
                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved. Click the download link to get the file.</p>';
            }
        });
    </script>
</html>
```  

### **XLSX ファイル**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an Excel file to load or leave empty to create a new workbook. Click "Save as XLSX" to generate and download output.xlsx.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions, Utils } = AsposeCells;

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

            // Load workbook from selected file or create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Save the workbook in XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook generated successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```  

### **PDF ファイル**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Prepare PDF save options
            const pdfOptions = new PdfSaveOptions();

            // Save workbook as PDF and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, pdfOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **注**  

JavaScriptには標準のレスポンスオブジェクトが存在しないため、この機能はAspose.Cells for JavaScriptにはありません。以下のコードを参考にしてファイルをストリームに保存し、その後ストリーム上で操作を行うことができます。  

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a memory buffer in XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">File is ready. Click the download link to save the workbook.</p>';
        });
    </script>
</html>
```
