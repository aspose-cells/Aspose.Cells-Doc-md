---
title: Läsa CSV fil med flera kodningar med JavaScript via C++
linktitle: Läsning av CSV fil med flera kodningar
type: docs
weight: 200
url: /sv/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Lär dig hur du läser CSV filer med flera kodningar med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Ibland innehåller din CSV-fil flera teckenkodningar (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells låter dig ladda sådana CSV-filer och konvertera dem till andra format, till exempel PDF eller XLSX.

{{% /alert %}}

Aspose.Cells ger egenskapen [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--), som du behöver ställa in på **true** för att ladda din CSV-fil med flera kodningar korrekt.

Följande skärmbild visar en prov-CSV-fil som innehåller två rader. Den första raden är kodad med **ANSI** och den andra raden är kodad med **Unicode**

|**Ingående fil**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Följande skärmbild visar XLSX-filen konverterad från ovanstående CSV-fil utan att ställa in [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--)-egenskapen till **true**. Som du ser, tolkades Unicode-texten inte korrekt.

|**Utgående fil 1: ingen anpassning gjord för flera krypteringar**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Följande skärmbild visar XSLX-filen konverterad från ovan nämnda CSV-fil efter att egenskapen [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) har ställts in till **true**. Som du kan se är Unicode-texten nu konverterad korrekt.

|**Utgående fil 2: IsMultiEncoded är satt till true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Nedan är det exempelkod som konverterar ovanstående CSV-fil till XLSX-format korrekt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
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

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Relaterade artiklar

- [Öppning av CSV-filer](/cells/sv/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
