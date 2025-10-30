---
title: Konvertera Excel till CSV, TSV och Txt med JavaScript via C++
linktitle: Spara som CSV, TSV och Txt
type: docs
weight: 40
url: /sv/javascript-cpp/convert-excel-to-csv-tsv-and-txt/
description: Lär dig hur man konverterar Excel filer till CSV, TSV och TXT format med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att konvertera Excel, ODS, JSON och andra formatfiler till CSV, TSV och TXT.

{{% /alert %}}

## **Spara arbetsbok till text eller CSV-format**

Ibland vill du konvertera eller spara ett arbetsbok med flera flikar till textformat. För textformat (t.ex. TXT, TabDelim, CSV, etc.), sparar både Microsoft Excel och Aspose.Cells som standard endast innehållet i det aktiva kalkylbladet.

Följande kodexempel förklarar hur man sparar en hel arbetsbok till textformat. Ladda den källa arbetsboken, som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylbladsfil som helst (såsom XLS, XLSX, XLSM, XLSB, ODS osv.) med valfritt antal kalkylblad.

När koden körs konverterar den datan i alla arbetsblad i arbetsboken till TXT-format.

Du kan ändra samma exempel för att spara din fil till CSV. Som standard är [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) ett kommatecken, så ange inte en avskiljare om du sparar till CSV-format.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Txt Save Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Txt Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (as text)
            const outputData = workbook.save(SaveFormat.Txt, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as text. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Spara textfiler med anpassad separator**

Textfiler innehåller kalkyleringsdata utan formatering. Filen är en typ av ren textfil som kan ha anpassade avgränsare mellan sina data.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Workbook to TXT/CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions, SaveFormat } = AsposeCells;

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

            // Create a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Optionally specify CSV save format if required by the API
            options.saveFormat = SaveFormat.CSV;

            // Save the workbook to CSV/TXT using the options
            const outputData = wb.save(SaveFormat.CSV, options);
            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```


## **Fortsatta ämnen**
- [Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format](/cells/sv/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format](/cells/sv/javascript-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
