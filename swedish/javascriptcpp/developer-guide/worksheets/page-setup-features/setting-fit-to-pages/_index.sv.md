---
title: Hur man skriver ut Excel som anpassade sidor breda och höga med JavaScript via C++
linktitle: Hur man skriver ut Excel som anpassade sidor breda och höga
type: docs
weight: 200
url: /sv/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Denna artikel visar kod som förklarar hur man ställer in FitToPagesWide och FitToPagesTall med Aspose.Cells for JavaScript via C++.
keywords: JavaScript via C++ Hur man ställer in FitToPagesWide och FitToPagesTall, Hur man lägger till FitToPagesWide och FitToPagesTall i JavaScript, Hur man ställer in FitToPagesWide och FitToPagesTall i Excel, Hur man tar bort FitToPagesWide och FitToPagesTall i Excel, Hur man skriver ut Excel som anpassade sidor breda och höga, Hur man skriver ut kalkylblad som en sida, Hur man skriver ut alla kolumner i kalkylbladet på en sida.
---

## **Introduktion**

FitToPagesWide och FitToPagesTall-inställningarna används i kalkylprogram (som Microsoft Excel) för att styra hur ett kalkylblad skalas när det skrivs ut. Dessa inställningar hjälper till att säkerställa att ditt utskrivna utskriftsresultat passar inom ett specificerat antal sidor, både horisontellt och vertikalt. Här är en översikt av varje inställning:

1. FitToPagesWide: Denna inställning specificerar antalet sidor brett som utskriften ska passa in i. Till exempel, att ställa in FitToPagesWide till 1 innebär att innehållet skalas för att passa inom en enkel sidbredde, oavsett hur brett kalkylbladet är.
2. FitToPagesTall: Denna inställning anger antalet sidor högt som den utskrivna versionen ska passa in i. Till exempel, att sätta FitToPagesTall till 1 innebär att innehållet skalas för att passa inom en sidhöjd, oavsett antalet rader.

## **Varför använda FitToPagesWide och FitToPagesTall**
Här är några skäl att ställa in FitToPagesWide och FitToPagesTall:
1. Kontroll över utskriftslayout: Genom att specificera antalet sidor brett och högt kan du säkerställa att din utskrivna dokument är lätt att läsa och välorganiserad, utan att kolumner eller rader delas på ett oönskat sätt över sidor.
2. Konsistens: Om du skriver ut flera blad eller rapporter hjälper användningen av dessa inställningar att bibehålla ett konsekvent format, vilket gör det lättare att jämföra och analysera utskrivna dokument.
3. Professionell presentation: Att korrekt skalas och anpassa innehåll till ett specificerat antal sidor kan leda till en mer professionell och polerad presentation av dina data.

## **Hur man skriver ut filen som anpassade sidor breda och höga i Excel**

För att ställa in FitToPagesWide och FitToPagesTall i Microsoft Excel, följ dessa steg:

1. Öppna ditt Excel-arbetsbok och gå till det blad du vill skriva ut.
2. Gå till fliken Sidlayout i menyfliksområdet.
3. I gruppen Sidformat klickar du på den lilla pilen i nedre högra hörnet för att öppna dialogrutan Sidformat.
4. I dialogrutan Sidformat går du till fliken Utsida.
5. Under Skalning väljer du alternativet "Anpassa till" och anger sedan antalet sidor brett och högt du vill: Skriv in antalet sidor brett du vill i den första rutan (Anpassa till x sidor brett). Skriv in det antal sidor högt du vill i den andra rutan (Anpassa till y sidor högt).
<br>
<img src="2.png" width=60% />

6. Klicka på OK för att tillämpa inställningarna.

## **Hur man skriver ut Excel som anpassade sidor breda och höga med Aspose.Cells for JavaScript via C++**

För att ställa in FitToPagesWide och FitToPagesTall i ett specificerat kalkylblad: Först, ladda [exempelfilen](input.xlsx), och sedan behöver du ändra egenskaperna [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) och [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) för [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-objektet för önskat kalkylblad. Här är ett exempel i JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man skriver ut kalkylblad som en sida med Aspose.Cells for JavaScript via C++**

För att skriva ut kalkylblad som en sida: Först, ladda [exempelfilen](sample.xlsx), och sedan behöver du ställa in egenskapen [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) för [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/)-objektet. Här är ett exempel i JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Utmatningsresultat:
<br>
<img src="3.png" width=60% />

## **Hur skriver man ut alla kolumner i kalkylbladet på en sida med hjälp av Aspose.Cells for JavaScript via C++**

För att skriva ut alla kolumner i kalkylbladet på en sida: Först laddar du [exempelfilen](sample.xlsx), och sedan måste du ställa in [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/)-objektet. Här är ett exempel i JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Utmatningsresultat:
<br>
<img src="4.png" width=60% />
