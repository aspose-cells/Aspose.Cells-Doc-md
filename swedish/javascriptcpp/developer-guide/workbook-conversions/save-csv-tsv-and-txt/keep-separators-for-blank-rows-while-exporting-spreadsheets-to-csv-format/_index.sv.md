---
title: Behåll separatorer för tomma rader vid export av kalkylblad till CSV format med JavaScript via C++
linktitle: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format
type: docs
weight: 160
url: /sv/javascript-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**  

Aspose.Cells ger möjlighet att behålla radseparatorer när man konverterar kalkylblad till CSV-format. För detta kan du använda [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--)-egenskapen av [**TxtSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/). [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) är en boolean-egenskap. För att behålla separatorerna för tomma rader vid konvertering av Excel-fil till CSV, ställ in [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--)-egenskapen till **true**.  

Följande kod laddar [käll-Excel-filen](84378743.xlsx). Den ställer in [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--)-egenskapen till **true** och sparar den som [utdata.csv](84378744.csv). Skärmbilden visar jämförelsen mellan käll-Excel-filen, standardutdata som genereras vid konvertering av kalkblad till CSV och den utdata som genereras när [**TxtSaveOptions.keepSeparatorsForBlankRow**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#keepSeparatorsForBlankRow--) ställs in på **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TxtSaveOptions Example</title>
    </head>
    <body>
        <h1>TxtSaveOptions to CSV Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to CSV</button>
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

            // Create a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate TxtSaveOptions
            const options = new TxtSaveOptions();

            // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
            options.keepSeparatorsForBlankRow = true;

            // Save the workbook to CSV using the options
            const outputData = workbook.save(SaveFormat.CSV, options);

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
