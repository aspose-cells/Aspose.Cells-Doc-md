---
title: Specificera dokumentversionen av Excel filen med inbyggda dokumentegenskaper med JavaScript via C++
linktitle: Ange dokumentversionen för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 20
url: /sv/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Lär dig hur man specificerar versionsnummer på en Excel fil programmatiskt med inbyggda dokumentegenskaper med JavaScript via C++.
---

## **Möjliga användningsscenario**  

Du kan ändra **Version number** på en Excel-fil genom att högerklicka på filen och välja Egenskaper > Detaljer och sedan redigera fältet **Version number**. Använd [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) egenskapen för att ändra det programmässigt med Aspose.Cells API:er.  

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**  

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper som inkluderar Titel, Författare och Versionnummer. Se [utdata Excel-fil](64716811.xlsx) genererad av koden och skärmdumpen som visar den modifierade Versionen med [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) egenskapen.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
