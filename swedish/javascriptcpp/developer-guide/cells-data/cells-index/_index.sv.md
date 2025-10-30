---
title: Få cellerindex
type: docs
weight: 600
url: /sv/javascript-cpp/get-cells-index/
description: Lär dig hur du får rad eller kolumn genom att använda radnamn, kolumn eller celler. Konvertera cellens namn till rad och kolumnindex som är nollbaserat med Aspose.Cells for JavaScript via C++.
keywords: Få radindex och kolumnindex efter namnet på cellen, Få kolumnindex efter namnet på kolumnen, Få radindex efter namnet på raden, Få index efter namnet på cellen. 
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn är definierad som A, B, C ... och cellerna namnges som A1, B2, C3 ... och så vidare.
Du kan vilja veta vilken rad och kolumn är denna cell i.

{{% /alert %}}


## **Möjliga användningsscenario**
När du bara behöver manipulera en specifik data på arbetsbladet genom rad- och kolumnindex behöver du veta kolumn- och kolumnindex för den specifika cellen. 
Aspose.Cells for JavaScript via C++ erbjuder den här funktionen för att hämta rad- och kolumnindex efter namnet på rad, kolumn och cell. 
Aspose.Cells for JavaScript via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att nå dina mål.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#rowNameToIndex-string-)

Obs: Indexeringen är nollbaserad i Aspose.Cells for JavaScript via C++, men raden är ettbaserad i MS Excel.

## **Hämta cellsindex med Aspose.Cells for JavaScript via C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Access cells of the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Find the cell containing "Blackberry"
            const curr = cells.find("Blackberry", null);

            // Current cell name
            const currentCellName = curr.name;

            // get row and column index of current cell
            const rowCol = CellsHelper.cellNameToIndex(curr.name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];

            // get column name by column index
            const columnName = CellsHelper.columnIndexToName(currCol);

            // get row name by row index
            const rowName = CellsHelper.rowIndexToName(currRow);

            // get column index by column name
            const columnIndex = CellsHelper.columnNameToIndex(columnName);

            // get row index by row name
            const rowIndex = CellsHelper.rowNameToIndex(rowName);

            const outputs = [];
            outputs.push("Current Cell Name: " + currentCellName);
            outputs.push("Row Index: " + currRow + "  Column Index: " + currCol);
            outputs.push("Column Name: " + columnName + " Row Name: " + rowName);
            outputs.push("Column Index: " + columnIndex + " Row Index: " + rowIndex);
            outputs.push("columnIndex == currCol: " + (columnIndex == currCol));
            outputs.push("rowIndex == currRow: " + (rowIndex == currRow));

            document.getElementById('result').innerHTML = '<pre>' + outputs.join('\n') + '</pre>';

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
