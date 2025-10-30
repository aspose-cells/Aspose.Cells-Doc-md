---
title: Inställning av marginaler med JavaScript via C++
linktitle: Inställning av marginaler
type: docs
weight: 20
url: /sv/javascript-cpp/setting-margins/
description: I denna artikel lär du dig hur du ställer in marginalerna för ett Excel kalkylblad med hjälp av exempel på kod. Lär dig också hur du programmässigt ställer in marginaler för sidcentrering, sidhuvud och sidfot med JavaScript API via C++.
keywords: Ställ in marginaler för excelkalkylblad till centrum med JavaScript via C++, ställ in marginalsidor för kalkylblad med JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells stödjer helt Microsoft Excels siduppställningsalternativ. Utvecklare kan behöva konfigurera siduppställningsinställningarna för kalkylblad för att kontrollera utskriftsprocessen. Det här avsnittet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

{{% /alert %}}

## **Ställa in marginaler**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samlingen som ger tillgång till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen.

Egenskapen [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) används för att ställa in sidinställningsalternativ för ett kalkylblad. Attributet [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) är ett objekt av klassen [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) som gör det möjligt för utvecklare att ställa in olika sidlayoutalternativ för ett utskrivet kalkylblad. Klassen [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) erbjuder olika egenskaper och metoder för att ställa in sidinställningar.

### **Sidmarginaler**

Ställ in sidmarginaler (vänster, höger, topp, botten) med hjälp av [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)-medlemmar. Några av medlemmarna är listade nedan och används för att specificera sidmarginaler:

- [**PageSetup.leftMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#leftMargin--)
- [**PageSetup.rightMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#rightMargin--)
- [**PageSetup.topMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#topMargin--)
- [**PageSetup.bottomMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#bottomMargin--)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Page Margins Example</title>
    </head>
    <body>
        <h1>Set Page Margins Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                // Proceed with a new empty workbook if no file selected
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            pageSetup.bottomMargin = 2;
            pageSetup.leftMargin = 1;
            pageSetup.rightMargin = 1;
            pageSetup.topMargin = 3;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetMargins_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page margins set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Centrera på sidan**

Det är möjligt att centrera något på en sida horisontellt och vertikalt. För detta finns några användbara medlemmar i [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)-klassen, [**PageSetup.centerHorizontally**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerHorizontally--) och [**PageSetup.centerVertically**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerVertically--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Center On Page</title>
    </head>
    <body>
        <h1>Center On Page Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // Create a workbook object (blank workbook)
            const workbook = new Workbook();

            // Get the worksheets in the workbook
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pagesetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Center on page Horizontally and Vertically
            pageSetup.centerHorizontally = true;
            pageSetup.centerVertically = true;

            // Save the Workbook in Excel 97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Sid- och fotmarginaler**

Ställ in sidhuvud- och sidfotsmarginaler med hjälp av [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)-klassens medlemmar som [**PageSetup.headerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerMargin--) och [**PageSetup.footerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerMargin--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Header/Footer Margins</title>
    </head>
    <body>
        <h1>Set Header/Footer Margins Example</h1>
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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Get the worksheets collection
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pageSetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Header / Footer margins (converted from setHeaderMargin/setFooterMargin)
            pageSetup.headerMargin = 2;
            pageSetup.footerMargin = 2;

            // Save the Workbook as Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
