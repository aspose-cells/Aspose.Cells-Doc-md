---
title: Specifikation av signifikanta siffror som ska lagras i Excel fil med JavaScript via C++
linktitle: Ange signifikanta siffror som ska lagras i Excel fil
type: docs
weight: 30
url: /sv/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Lär dig hur du specificerar signifikanta siffror som ska lagras i en Excel fil med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Som standard lagrar Aspose.Cells for JavaScript via C++ 17 signifikanta siffror av dubbelvärden inuti Excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra Aspose.Cells standardbeteende från 17 till 15 signifikanta siffror med hjälp av [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--)-egenskapen.  

## **Ange signifikanta siffror som ska lagras i Excel-fil**  

Följande exempel kod tvingar Aspose.Cells att använda 15 signifikanta siffror när du lagrar dubbla värden i Excel-filen. Kontrollera [utdata Excel-fil](22774105.xlsx). Byt ut dess extension till .zip och packa upp den, du kommer att se att endast 15 signifikanta siffror lagras i Excel-filin. Följande skärmbild förklarar effekten av [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--)-egenskapen på utdata Excel-filen.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
