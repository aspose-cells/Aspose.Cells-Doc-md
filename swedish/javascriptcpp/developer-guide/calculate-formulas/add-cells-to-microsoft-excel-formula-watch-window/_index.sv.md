---
title: Lägg till Cells i Microsoft Excel Formelbevakar Fönstret med JavaScript via C++
linktitle: Lägg till celler i Microsoft Excel Formelövervakningsfönstret
description: Hur man använder Aspose.Cells biblioteket för att lägga till celler i formelbevakarens fönster i Excel med JavaScript via C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi manipulera cellerna i den och ställa in formler. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, Formelbevakar Fönster, Celler, Lägg till, JavaScript via C++
type: docs
weight: 60
url: /sv/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Möjliga användningsscenario**

Microsoft Excel Watch Window är ett användbart verktyg för att enkelt övervaka cellvärden och dess formler i ett fönster. Du kan öppna *Watch Window* med Microsoft Excel genom att klicka på *Formulas > Watch* *Window*. Det har knappen *Add Watch* som kan användas för att lägga till celler för inspektion. På liknande sätt kan du använda [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-)-metoden för att lägga till celler i *Watch Window* med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande exempel kod ställer in formeln för cellerna C1 och E1 och lägger till båda till Watch Window. Den sparar sedan arbetsboken som [utdata Excel-fil](67338481.xlsx). Om du öppnar den utdata Excel-filen och tittar i *Watch Window* kommer du att se båda cellerna som visas i denna skärmdump.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            const fileInput = document.getElementById('fileInput');
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
