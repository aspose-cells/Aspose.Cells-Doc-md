---
title: Hur man styr bladfliken med JavaScript via C++
linktitle: Hur man kontrollerar flikfält för arkhuvuden
type: docs
weight: 600
url: /sv/javascript-cpp/how-to-control-sheet-tab-bar/
description: Lär dig hur du styr bladfliken med Aspose.Cells for JavaScript via C++.
keywords: Hur man styr bladflikens JavaScript via C++, Operera bladflikens JavaScript via C++, Sätt bladflikens JavaScript via C++, Kontrollera bladflikens JavaScript via C++.  
---

## **Möjliga användningsscenario**  
När du behöver justera visningen av Excel-bladets list, måste du veta hur du styr bladfliken, till exempel att dölja eller visa bladfliken, ändra bladflikens bredd, ange det första synliga fliknamnet och så vidare. Aspose.Cells for JavaScript via C++ stöder dessa funktioner. Aspose.Cells tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.

- [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)
- [**WorkbookSettings.sheetTabBarWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#sheetTabBarWidth--)
- [**WorkbookSettings.firstVisibleTab**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#firstVisibleTab--)

## **Hur man styr bladfliken med Aspose.Cells for JavaScript via C++**  
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Visa flikfältet och ange bredden på flikfältet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value assignment)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            // Display the sheet tab and set the width of the tab bar (converted getters/setters -> properties)
            workbook.settings.showTabs = true;
            workbook.settings.sheetTabBarWidth = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Förhandsgranskning av resultatfil:  
<br>  
<image src="result.png" width="70%" />
