---
title: Olika sätt att spara filer med JavaScript via C++
linktitle: Spara filer
type: docs
weight: 40
url: /sv/javascript-cpp/different-ways-to-save-files/
description: Aspose.Cells for JavaScript via C++ kan spara filer i olika format inklusive PDF, HTML, DOCX, PPTX, JSON och MHTML.
keywords: Aspose.Cells Spara Excel till PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML och mer med JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att skapa och spara filer. Den här artikeln förklarar de olika sätten på vilka filer kan sparas.

{{% /alert %}}

## **Olika sätt att spara filer**

Aspose.Cells tillhandahåller [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil och ger de egenskaper och metoder som krävs för att arbeta med Excel-filer. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen tillhandahåller [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metoden som används för att spara Excel-filer. [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metoden har många överlagringar som används för att spara filer på olika sätt.

Det filformat som filen sparas i bestäms av [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-enumerationen

|**Filtyp**|**Beskrivning**|
| :- | :- |
|CSV|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007 XLSX-fil|
|Xlsm|Representerar en Excel 2007 XLSM-fil|
|Xltx|Representerar en Excel 2007-mall XLTX-fil|
|Xltm|Representerar en Excel 2007 med makroaktiverad XLTM-fil|
|Xlsb|Representerar en Excel 2007 binär XLSB-fil|
|SpreadsheetML|Representerar en kalkyl XML-fil|
|TSV|Representerar en tab-separated values-fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|ODS|Representerar en ODS-fil|
|Html|Representerar HTML-fil(er)|
|MHtml|Representerar MHTML-fil(er)|
|Pdf|Representerar en PDF-fil|
|XPS|Representerar ett XPS-dokument|
|TIFF|Representerar Tagged Image File Format (TIFF)|

## **Så här sparar du filen i olika format**

 För att spara filer till en lagringsplats, ange filnamnet (fullständig lagringsväg) och önskat filformat (från [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)-enumerationen) när du anropar [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-objektets [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metod.

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

## **Så här sparar du arbetsbok till Pdf**
 Portable Document Format (PDF) är en typ av dokument som skapades av Adobe på 1990-talet. Syftet med detta filformat var att införa en standard för presentation av dokument och annat referensmaterial i ett format som är oberoende av applikationsprogramvara, hårdvara och operativsystem. PDF-filtet innehåller fulla kapaciteter för att innehålla information som text, bilder, hyperlänkar, formulärfält, rik media, digitala signaturer, bilagor, metadata, geospatiala funktioner och 3D-objekt som kan bli en del av källa dokumentet.

 Följande kod visar hur man sparar arbetsbok som PDF-fil med Aspose.Cells:
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

## **Så här sparar du arbetsboken till Text- eller CSV-format**

Ibland vill du konvertera eller spara en arbetsbok med flera arbetsblad till textformat. För textformat (till exempel TXT, TabDelim, CSV osv.) sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva arbetsbladet.

 Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda arbetsboken som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylbladsfil som helst (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med vilket antal arbetsblad som helst.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan modifiera samma exempel för att spara din fil till CSV. Som standardspecifikation är [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) komma, så ange inte en separator om du sparar till CSV-format. Observera: Om du använder utvärderingsversionen och även om egenskapen [**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#exportAllSheets--) är inställd på true, kommer programmet fortfarande endast att exportera ett kalkylblad.

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

## **Så här sparar du filen till textfiler med anpassad avskiljare**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

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

## **Så här sparar du filen till en ström**

För att spara filer till en ström, skapa ett *MemoryStream* eller *FileStream*-objekt och spara filen till den strömmen genom att anropa [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) objektets [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metod. Specificera önskat filformat med enumrationen [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) när du anropar [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metoden.

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

## **Så här sparar du Excel-filen till HTML- och MHT-filer**
Aspose.Cells kan enkelt spara en Excel-fil, JSON, CSV eller andra filer som kan laddas av Aspose.Cells som .html och .mht-filer.
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


## **Så här sparar du Excel-filen till OpenOffice (ODS, SXC, FODS, OTS)**
Vi kan spara filerna i OpenOffice-format: ODS, SXC, FODS, OTS, etc.

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

## **Så här sparar du Excel-filen till JSON eller XML**

JSON (JavaScript Object Notation) är ett öppet standardfilformat för att dela data som använder mänskligt läsbar text för att lagra och överföra data. JSON-filer lagras med filändelsen .json. JSON kräver mindre formatering och är ett bra alternativ till XML. JSON härstammar från JavaScript men är ett språkoberoende dataformat. Generering och tolkning av JSON stöds av många moderna programmeringsspråk. application/json är mediatypen som används för JSON.

Aspose.Cells stöder att spara filer i JSON eller XML.

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


## **Fortsatta ämnen**
- [Justera arbetsbokens kompressionsnivå](/cells/sv/javascript-cpp/adjust-workbook-compression-level/)
- [Spara arbetsbok i strikt öppet XML-kalkylbladsformat](/cells/sv/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Spara fil till responsobjekt](/cells/sv/javascript-cpp/saving-file-to-response-object/)
