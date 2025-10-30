---
title: Laden und Verwalten von Excel , OpenOffice , Json , Csv und Html Dateien
linktitle: Dateien öffnen
type: docs
weight: 20
url: /de/javascript-cpp/loading-saving-and-managing/
description: Mit Aspose.Cells ist es einfach, Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , Pdf , Jpg , Tiff , Bild , Mht und XPS Dateien mit JavaScript via C++ zu erstellen, zu öffnen und zu verwalten.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Excel-Dateien zu erstellen, zu öffnen und zu verwalten, z.B. um Daten abzurufen oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Neue Arbeitsmappe erstellen**
Das folgende Beispiel erstellt ein neues Arbeitsbuch von Grund auf.

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

## **Eine Datei öffnen und speichern**
Mit Aspose.Cells ist es einfach, Excel-Dateien zu öffnen, zu speichern und zu verwalten.

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

## **Erweiterte Themen**
- [Verschiedene Möglichkeiten, Dateien zu öffnen](/cells/de/javascript-cpp/different-ways-to-open-files/)
- [Definierte Namen filtern beim Laden der Arbeitsmappe](/cells/de/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Objekte filtern beim Laden einer Arbeitsmappe oder eines Arbeitsblatts](/cells/de/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Die Art der Daten filtern, während die Arbeitsmappe aus einer Vorlagendatei geladen wird](/cells/de/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Warnungen beim Laden von Excel-Dateien erhalten](/cells/de/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Quell-Excel-Datei ohne Diagramme laden](/cells/de/javascript-cpp/load-source-excel-file-without-charts/)
- [Bestimmte Arbeitsblätter in einer Arbeitsmappe laden](/cells/de/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Arbeitsmappe mit angegebener Druckerpapiergröße laden](/cells/de/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Öffnen von verschiedenen Microsoft Excel-Versionen Dateien](/cells/de/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Öffnen von Dateien mit verschiedenen Formaten](/cells/de/javascript-cpp/opening-files-with-different-formats/)
- [Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und umfangreichen Datensätzen](/cells/de/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Zahlen-Tabellenkalkulation von Apple Inc. mit Aspose.Cells lesen](/cells/de/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [ Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert](/cells/de/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Verwendung der LightCells-API](/cells/de/javascript-cpp/using-lightcells-api/)
- [Konvertieren von CSV in JSON](/cells/de/javascript-cpp/convert-csv-to-json/)
- [Excel nach JSON konvertieren](/cells/de/javascript-cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/javascript-cpp/convert-json-to-csv/)
- [JSON in Excel konvertieren](/cells/de/javascript-cpp/convert-json-to-excel/)
- [Excel in Html umwandeln](/cells/de/javascript-cpp/convert-excel-to-html/)
