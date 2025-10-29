---
title: 使用JavaScript通过C++将文件保存到响应对象
linktitle: 将文件保存到响应对象
type: docs
weight: 50
url: /zh/javascript-cpp/saving-file-to-response-object/
description: 学习如何使用Aspose.Cells for JavaScript通过C++动态生成文件并直接发送到客户端浏览器。
---

{{% alert color="primary" %}}  

Aspose.Cells可以操作文件。本文解释了可以将文件保存到响应对象的各种方法。  

{{% /alert %}}  

## **将文件保存到响应对象**  

也可以动态生成文件并直接发送到客户端浏览器。为此，请使用接受以下参数的 [**Save**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) 方法的特殊重载版本：  

- JavaScript响应对象。  
- 文件名。  
- [**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/)，输出文件的 content-disposition 类型。  
- [**SaveOptions**](https://reference.aspose.com/cells/javascript-cpp/saveoptions/)，文件格式类型  

[**ContentDisposition**](https://reference.aspose.com/cells/javascript-cpp/contentdisposition/) 枚举决定了传送到浏览器的文件是否提供直接在浏览器或与 .xls/.xlsx 或其他扩展名相关联的应用程序中打开的选项。  

该枚举包含以下预定义的保存类型：  

|**类型**|**描述**|  
| :- | :- |  
|附件|将电子表格发送到浏览器，并作为与.xls/.xlsx或其他扩展名相关联的附件在应用程序中打开|  
|内置|将文档发送到浏览器，并提供选项将电子表格保存到磁盘或在浏览器中打开|  

### **XLS文件**  

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

### **XLSX文件**  

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

### **PDF文件**  

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

### **注意**  

由于JavaScript中没有标准的响应对象，此功能在Aspose.Cells for JavaScript通过C++中不存在。你可以参考以下代码将文件保存到流中，然后对流进行操作。  

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
