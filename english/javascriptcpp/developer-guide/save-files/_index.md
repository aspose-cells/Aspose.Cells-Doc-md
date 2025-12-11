---
title: Different Ways to Save Files with JavaScript via C++
linktitle: Save Files
type: docs
weight: 40
url: /javascript-cpp/different-ways-to-save-files/
description: Aspose.Cells for JavaScript via C++ can save files to different formats including PDF, HTML, DOCX, PPTX, JSON, and MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and more using JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to create and save files. This article explains the various ways in which files can be saved.

{{% /alert %}}

## **Different Ways to Save Files**

Aspose.Cells provides the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) which represents a Microsoft Excel file and provides the properties and methods necessary to work with Excel files. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class provides the [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method used to save Excel files. The [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method has many overloads that are used to save files in different ways.

The file format that the file is saved to is decided by the [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumeration

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|Excel97To2003|Represents an Excel 97‑2003 file|
|Xlsx|Represents an Excel 2007 XLSX file|
|Xlsm|Represents an Excel 2007 XLSM file|
|Xltx|Represents an Excel 2007 template XLTX file|
|Xltm|Represents an Excel 2007 macro‑enabled XLTM file|
|Xlsb|Represents an Excel 2007 binary XLSB file|
|SpreadsheetML|Represents a Spreadsheet XML file|
|TSV|Represents a Tab‑separated values file|
|TabDelimited|Represents a Tab‑delimited text file|
|ODS|Represents an ODS file|
|Html|Represents HTML file(s)|
|MHtml|Represents an MHTML file(s)|
|Pdf|Represents a PDF file|
|XPS|Represents an XPS document|
|TIFF|Represents Tagged Image File Format (TIFF)|

## **How to Save File to Different Formats**

To save files to a storage location, specify the file name (complete with storage path) and the desired file format (from the [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumeration) when calling the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) object's [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method.

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

## **How to Save Workbook to PDF**
Portable Document Format (PDF) is a type of document created by Adobe back in the 1990s. The purpose of this file format was to introduce a standard for representation of documents and other reference material in a format that is independent of application software, hardware, as well as operating systems. The PDF file format has the full capability to contain information such as text, images, hyperlinks, form fields, rich media, digital signatures, attachments, metadata, geospatial features, and 3D objects that can become part of the source document.

The following code shows how to save a workbook as a PDF file with Aspose.Cells:

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

## **How to Save Workbook to Text or CSV Format**

Sometimes you want to convert or save a workbook with multiple worksheets into a text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into a text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (e.g., XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) is a comma, so do not specify a separator if saving to CSV format. Please note: If you are using the evaluation version and even if the [**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#exportAllSheets--) property is set to true, the program will still only export one worksheet.

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

## **How to Save File to Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain‑text file that can have customized delimiters between its data.

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

## **How to Save File to a Stream**

To save files to a stream, create a *MemoryStream* or *FileStream* object and save the file to that stream object by calling the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) object's [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method. Specify the desired file format using the [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumeration when calling the method.

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

## **How to Save Excel File to HTML and MHT Files**

Aspose.Cells can simply save an Excel file, JSON, CSV, or other files that can be loaded by Aspose.Cells as .html and .mht files.

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

## **How to Save Excel File to OpenOffice (ODS, SXC, FODS, OTS)**

We can save the files in OpenOffice formats: ODS, SXC, FODS, OTS, etc.

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

## **How to Save Excel File to JSON or XML**

JSON (JavaScript Object Notation) is an open‑standard file format for sharing data that uses human‑readable text to store and transmit data. JSON files are stored with the .json extension. JSON requires less formatting and is a good alternative to XML. JSON is derived from JavaScript but is a language‑independent data format. The generation and parsing of JSON is supported by many modern programming languages. `application/json` is the media type used for JSON.

Aspose.Cells supports saving files to JSON or XML.

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

## **Advanced Topics**
- [Adjust workbook compression level](/cells/javascript-cpp/adjust-workbook-compression-level/)
- [Save Workbook to Strict Open XML Spreadsheet Format](/cells/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Saving File to Response Object](/cells/javascript-cpp/saving-file-to-response-object/)