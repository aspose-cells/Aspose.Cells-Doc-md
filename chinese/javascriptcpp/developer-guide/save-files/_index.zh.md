---
title: 用JavaScript通过C++保存文件的不同方式
linktitle: 保存文件
type: docs
weight: 40
url: /zh/javascript-cpp/different-ways-to-save-files/
description: Aspose.Cells for Java脚本通过C++可以将文件保存为不同格式，包括PDF、HTML、DOCX、PPTX、JSON和MHTML。
keywords: Aspose.Cells通过JavaScript与C++可以将Excel保存为PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML等格式。
---

{{% alert color="primary" %}}

Aspose.Cells 可以创建和保存文件。本文介绍了可保存文件的各种方式。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表Microsoft Excel文件，具有操作Excel文件所需的属性和方法。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类提供用于保存Excel文件的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)方法。[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)方法有多种重载，可以以不同方式保存文件。

保存文件的文件格式由[**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)枚举决定

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示 CSV 文件|
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007 XLSX文件|
|Xlsm|表示Excel 2007 XLSM文件|
|Xltx|表示Excel 2007模板XLTX文件|
|Xltm|表示Excel 2007启用宏的XLTM文件|
|Xlsb|表示Excel 2007二进制XLSB文件|
|SpreadsheetML|表示一种Spreadsheet XML文件|
|TSV|表示制表符分隔数值文件|
|TabDelimited|代表分隔符文本文件|
|ODS|表示 ODS 文件|
|Html|表示HTML文件|
|MHtml|表示一个MHTML文件|
|Pdf|表示一个PDF文件|
|XPS|表示一个XPS文档|
|TIFF|表示Tagged Image File Format (TIFF)|

## **如何将文件保存为不同的格式**

要将文件保存到存储位置，在调用[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)对象的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)方法时，指定文件名（包括存储路径）和所需的文件格式（来自[**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)枚举）。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Save Formats Example</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLinks a { display: block; margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Save Formats Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.ods" />
        <button id="runExample">Save in Multiple Formats</button>
        <div id="result"></div>
        <div id="downloadLinks"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions } = AsposeCells;

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
            const downloadLinks = document.getElementById('downloadLinks');
            downloadLinks.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare format list to save
            const formats = [
                { format: SaveFormat.Excel97To2003, name: 'output.xls', options: new XlsSaveOptions() },
                { format: SaveFormat.Xlsx, name: 'output.xlsx' },
                { format: SaveFormat.Xlsb, name: 'output.xlsb' },
                { format: SaveFormat.Ods, name: 'output.ods' },
                { format: SaveFormat.Pdf, name: 'output.pdf' },
                { format: SaveFormat.Html, name: 'output.html' },
                { format: SaveFormat.SpreadsheetML, name: 'output.xml' }
            ];

            // Save in each format and create download link
            for (let i = 0; i < formats.length; i++) {
                const f = formats[i];
                let outputData;
                if (f.options) {
                    outputData = workbook.save(f.format, f.options);
                } else {
                    outputData = workbook.save(f.format);
                }
                const blob = new Blob([outputData]);
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = f.name;
                link.textContent = 'Download ' + f.name;
                downloadLinks.appendChild(link);
            }

            result.innerHTML = '<p style="color: green;">Files saved in memory. Click the download links below to download each format.</p>';
        });
    </script>
</html>
```

## **如何将工作簿保存为PDF**
便携式文档格式（PDF）是由Adobe在1990年代创建的一种文档。该文件格式的目的是引入一种标准，用于以与应用软件、硬件及操作系统无关的格式表示文档和其他参考资料。PDF文件格式具有完整能力，包括文本、图像、超链接、表单字段、丰富媒体、数字签名、附件、元数据、地理空间特征和3D对象，且可以成为源文档的一部分。

以下代码展示了如何用Aspose.Cells将工作簿保存为PDF文件：
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Save to PDF and PDF/A-1a</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none;"></a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and set value to A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "Hello World!";

            // Save as PDF (first file)
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1], { type: 'application/pdf' });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'pdf1.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download pdf1.pdf';

            // Save as PDF with PDF/A-1a compliance
            const saveOptions = new PdfSaveOptions();
            saveOptions.compliance = PdfCompliance.PdfA1a;

            const outputData2 = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'pdfa1a.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download pdfa1a.pdf';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF files generated successfully. Use the download links above.</p>';
        });
    </script>
</html>
```

## **如何将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells都仅保存活动工作表的内容。

以下示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等），含有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例，将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--)为逗号，因此在保存为CSV格式时无需指定分隔符。请注意：如果你使用评估版，即使设置了[**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#exportAllSheets--)属性为true，程序仍只导出一个工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Workbook to Txt</title>
    </head>
    <body>
        <h1>Export Workbook to Txt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Export to TXT</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (Tab delimited)
            const outputData = workbook.save(SaveFormat.TabDelimited, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook exported to TXT successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to CSV (with custom separator)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions } = AsposeCells;

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

            // Create a Workbook object and open the file from the uploaded data
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Save the file with the options (returns file data)
            const outputData = wb.save(options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```

## **如何将文件保存到流中**

要将文件保存到流中，创建一个*MemoryStream*或*FileStream*对象，并通过调用[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)对象的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)方法，将文件保存到该流对象中。在调用时，使用[**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)枚举指定所需的文件格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a binary (xlsx) and provide it as a download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **如何将Excel文件保存为Html和Mht文件**
Aspose.Cells可以轻松保存Excel文件、JSON、CSV或其他可以作为.html和.mht文件加载的文件。
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells MHTML Save Example</title>
    </head>
    <body>
        <h1>Save Workbook to MHTML Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to MHTML format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to MHTML format successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **如何将Excel文件保存为OpenOffice（ODS，SXC，FODS，OTS）**
我们可以将文件保存为OpenOffice格式：ODS、SXC、FODS、OTS等。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Convert to ODS/SXC/FODS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Save</button>
        <div>
            <a id="downloadOds" style="display: none; margin-right: 10px;">Download ODS File</a>
            <a id="downloadSxc" style="display: none; margin-right: 10px;">Download SXC File</a>
            <a id="downloadFods" style="display: none;">Download FODS File</a>
        </div>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ODS
            const odsData = workbook.save(SaveFormat.Ods);
            const odsBlob = new Blob([odsData]);
            const downloadOds = document.getElementById('downloadOds');
            downloadOds.href = URL.createObjectURL(odsBlob);
            downloadOds.download = 'Out.ods';
            downloadOds.style.display = 'inline-block';
            downloadOds.textContent = 'Download ODS File';

            // Save as SXC
            const sxcData = workbook.save(SaveFormat.Sxc);
            const sxcBlob = new Blob([sxcData]);
            const downloadSxc = document.getElementById('downloadSxc');
            downloadSxc.href = URL.createObjectURL(sxcBlob);
            downloadSxc.download = 'Out.sxc';
            downloadSxc.style.display = 'inline-block';
            downloadSxc.textContent = 'Download SXC File';

            // Save as FODS
            const fodsData = workbook.save(SaveFormat.Fods);
            const fodsBlob = new Blob([fodsData]);
            const downloadFods = document.getElementById('downloadFods');
            downloadFods.href = URL.createObjectURL(fodsBlob);
            downloadFods.download = 'Out.fods';
            downloadFods.style.display = 'inline-block';
            downloadFods.textContent = 'Download FODS File';

            resultDiv.innerHTML = '<p style="color: green;">Files ready. Click the download links to save the converted files.</p>';
        });
    </script>
</html>
```

## **如何将Excel文件保存为JSON或XML**

JSON（JavaScript对象表示）是一种用于存储和传输数据的开放标准文件格式，它使用人类可读的文本。JSON文件存储为.json扩展名。JSON需要更少的格式化，是XML的一个很好的替代品。JSON源自JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持JSON的生成和解析。application/json是用于JSON的媒体类型。

Aspose.Cells支持将文件保存为JSON或XML。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON Export Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```


## **高级主题**
- [调整工作簿压缩级别](/cells/zh/javascript-cpp/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/javascript-cpp/saving-file-to-response-object/)
