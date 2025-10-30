---
title: Specificera språk på Excel filen med inbyggda dokumentegenskaper med JavaScript via C++
linktitle: Ange språket för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 30
url: /sv/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Möjliga användningsscenario**

Du kan ändra språk på en Excel-fil genom att högerklicka på filen och sedan välja Egenskaper > Detaljer och redigera fältet Språk. Använd [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--)-egenskapen för att ändra detta programmatiskt med Aspose.Cells for JavaScript via C++ API:er.

## **Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskap som heter language. Se [utdata Excel-fil](64716891.xlsx) genererad av koden och skärmdumpen som visar det modifierade språkvärdet med [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) egenskapen.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
