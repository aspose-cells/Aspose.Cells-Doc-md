---
title: Laddning och hantering av Excel , OpenOffice , Json , Csv och Html filer
linktitle: Öppna filer
type: docs
weight: 20
url: /sv/javascript-cpp/loading-saving-and-managing/
description: Med Aspose.Cells är det enkelt att skapa, öppna och hantera Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , Pdf , Jpg , Tiff , Bild , Mht och XPS filer med JavaScript via C++.
---

{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att skapa, öppna och hantera Excel-filer, till exempel för att hämta data eller använda en designer mall för att snabba upp utvecklingsprocessen.

{{% /alert %}}

## **Skapa en ny arbetsbok**
Följande exempel skapar en ny arbetsbok från grunden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Öppna och spara en fil**
Med Aspose.Cells är det enkelt att öppna, spara och hantera Excel-filer.

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
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Avancerade ämnen**
- [Olika sätt att öppna filer](/cells/sv/javascript-cpp/different-ways-to-open-files/)
- [Filtrera Definierade namn vid inläsning av arbetsbok](/cells/sv/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrera objekt vid inläsning av arbetsbok eller arbetsblad](/cells/sv/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrering av datatyp vid inläsning av arbetsboken från mallfil](/cells/sv/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Få varningar vid inläsning av Excel-fil](/cells/sv/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Ladda käll-Excel-fil utan diagram](/cells/sv/javascript-cpp/load-source-excel-file-without-charts/)
- [Ladda specifika arbetsblad i en arbetsbok](/cells/sv/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Ladda arbetsbok med specificerad pappersstorlek](/cells/sv/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Öppna filer från olika Microsoft Excel-versioner](/cells/sv/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Öppna filer med olika format](/cells/sv/javascript-cpp/opening-files-with-different-formats/)
- [Optimera minnesanvändningen vid arbete med stora filer med stora dataset](/cells/sv/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Läsa Numbers-kalkylblad utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid](/cells/sv/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Använda LightCells API](/cells/sv/javascript-cpp/using-lightcells-api/)
- [Konvertera CSV till JSON](/cells/sv/javascript-cpp/convert-csv-to-json/)
- [Konvertera Excel till JSON](/cells/sv/javascript-cpp/convert-excel-to-json/)
- [Konvertera JSON till CSV](/cells/sv/javascript-cpp/convert-json-to-csv/)
- [Konvertera JSON till Excel](/cells/sv/javascript-cpp/convert-json-to-excel/)
- [Konvertera Excel till Html](/cells/sv/javascript-cpp/convert-excel-to-html/)
