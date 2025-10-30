---
title: Ladda eller importera CSV fil med formler via JavaScript
linktitle: Ladda eller importera CSV fil med formler
type: docs
weight: 350
url: /sv/javascript-cpp/load-or-import-csv-file-with-formulas/
description: Lär dig att ladda och importera CSV filer som innehåller formler med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

CSV-fil innehåller oftast textdata och innehåller inga formler. Men ibland kan CSV-filer också innehålla formler. Sådana CSV-filer bör laddas genom att ställa in [TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--) till **true**. När denna egenskap är satt till **true** kommer Aspose.Cells inte att behandla formler som enkel text. Detta kommer att behandlas som formler, och Aspose.Cells formelberäkningsmotor kommer att bearbeta dem som vanligt.

{{% /alert %}}

 Följande kod illustrerar hur du kan ladda samt importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. För att illustrera använder vi [enkel CSV-fil](5115034.csv) som innehåller denna data. Som du ser innehåller den en formel.

{{< highlight javascript >}}
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with Formulas and Save as XLSX</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="convertToXlsx">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download XLSX</a>
        <div id="result"></div>

        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, TxtLoadOptions, SaveFormat } = AsposeCells;

            AsposeCells.onReady().then(() => {
                console.log("Aspose.Cells initialized");
            });

            document.getElementById('convertToXlsx').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.hasFormula = true;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = file.name.replace(/\.csv$/i, '.xlsx');
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download XLSX File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the XLSX file.</p>';
            });
        </script>
    </body>
</html>
{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Load Example</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);

            // TxtLoadOptions configuration
            const opts = new TxtLoadOptions();
            opts.separator = ',';
            opts.hasFormula = true;

            // Load your CSV file with formulas in a Workbook object
            const workbook = new Workbook(bytes, opts);

            // You can also import your CSV file like this
            // The code below is importing CSV file starting from cell D4 (rowIndex=3, colIndex=3)
            const worksheet = workbook.worksheets.get(0);
            worksheet.cells.importCSV(bytes, opts, 3, 3);

            // Save your workbook in Xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

Koden laddar först CSV-filen, importer den sedan igen till cell D4. Slutligen sparar den arbetsbokobjektet i XLSX-format. [utdata XLSX-fil](5115052.xlsx) ser ut så här. Som du ser, innehåller cell C3 och F4 formler och deras resultat är 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |
