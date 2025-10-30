---
title: Öppna olika Microsoft Excel versioner filer med JavaScript via C++
linktitle: Öppna olika Microsoft Excel versioners filer
type: docs
weight: 20
url: /sv/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: Denna artikel förklarar hur man öppnar filer i olika Excel versioner med Aspose.Cells for JavaScript via C++.
keywords: JavaScript Öppna olika Microsoft Excel filer via C++, Hur öppnar jag krypterade Excel filer JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Hur man öppnar filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95, 97 eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i någon av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS och så vidare. Använd konstruktorn, eller ange klassens [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) [**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--)-egenskaps attribut som anger formatet med hjälp av [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype)-uppräkningen.

Uppräkningen [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) innehåller många fördefinierade filformat, varav några är listade nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|SpreadsheetML|Representerar en SpreadsheetML fil|
|Tsv|Representerar en tabb-separerad värden fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|Ods|Representerar en ODS fil|
|Html|Representerar en HTML fil|
|Mhtml|Representerar en MHTML fil|

### **Öppna Microsoft Excel 95/5.0 filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) och ställ in den relaterade attributet för [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)-klassen för mallfilen som ska laddas. En exempel fil för att testa denna funktion kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

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

### **Öppna Microsoft Excel 97-2003 filer**

För att öppna en Microsoft Excel 97 - 2003-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) och ställ in det relaterade attributet för [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)-klassen för mallfilen som ska laddas.

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

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, ange filens sökväg. Du kan även använda [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) och ställa in de relaterade attributen/alternativen för [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)-klassen för mallfilen som ska laddas.

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

### **Öppna krypterade Excel-filer**

Det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna en krypterad fil, använd [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) och ställ in dess attribut och alternativ (till exempel, ge ett lösenord) för mallfilen som ska laddas.
En testfil för att testa den här funktionen kan laddas ner från följande länk:

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

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 filer.
