---
title: Rensa filter i pivot tabell
type: docs
weight: 130
url: /sv/javascript-cpp/clear-filter-in-pivot-table/
description: Hur man rensar PivotFilter från det specifika PivotField i pivottabellen med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript bibliotek, Rensar PivotFilter i pivottabell med Aspose.Cells for JavaScript via C++ Excel bibliotek.
---

## **Möjliga användningsscenario**
När du skapar en pivottabell med kända data och vill filtrera pivottabellen måste du lära dig och använda filter. Det kan hjälpa dig att filtrera ut data på ett effektivt sätt. Genom att använda API:et Aspose.Cells for JavaScript via C++ kan du manipulera filter på fältvärden i pivottabeller. 

## **Hur man rensar filter i pivot-tabell i Excel**
Rensa filter i pivot-tabell i Excel, följ dessa steg:

1. Välj den pivot-tabell du vill rensa filtret på. 
2. Klicka på nedåtpilen för filtret som du vill rensa i pivot-tabellen.
3. Välj "Rensa filter" från rullgardinsmenyn.
<img src="1.png" width=80% />
4. Om du vill rensa alla filter från pivottabellen kan du också klicka på knappen "Rensa filter" på fliken PivotTable Analyze i Excel-ribbon.
<img src="2.png" width=80% />

## **Hur man rensar filter i pivottabell med Aspose.Cells for JavaScript via C++**
Rensa filter i pivottabell med Aspose.Cells for JavaScript via C++. Se följande exempel. 
1. Ställ in datan och skapa en pivottabell baserad på det. 
2. Lägg till ett filter på radfältet i pivottabellen. 
3. Spara arbetsboken i [utdata XLSX](ut_add.xlsx) -format. Efter att exemplet har körts läggs en pivottabell med top10-filter till i arket. 
4. Rensa filtret på ett specifikt pivotfält. Efter att koden har körts för att rensa filtret kommer filtret på det specifika pivotfältet att rensas. Vänligen kontrollera [utdata XLSX](ut_delete.xlsx).

## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkAdd" style="display: none; margin-right: 10px;">Download Pivot Added File</a>
            <a id="downloadLinkDelete" style="display: none;">Download Pivot Filter Cleared File</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            document.getElementById('result').innerHTML = '<p>Running example...</p>';

            // Create a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("A6");
            cell.value = "Guava";
            cell = cells.get("A7");
            cell.value = "Carambola";
            cell = cells.get("A8");
            cell.value = "Banana";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("B6");
            cell.value = 5;
            cell = cells.get("B7");
            cell.value = 2;
            cell = cells.get("B8");
            cell.value = 20;

            // Adding a PivotTable to the worksheet
            const i = ws.pivotTables.add("=A1:B8", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Count");
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;

            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;

            // Add top10 filter
            const index = pivotTable.pivotFilters.add(field.baseIndex, AsposeCells.PivotFilterType.Count);
            const filter = pivotTable.pivotFilters.get(index);
            filter.autoFilter.filterTop10(0, true, false, 5);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after adding pivot/filter
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLinkAdd = document.getElementById('downloadLinkAdd');
            downloadLinkAdd.href = URL.createObjectURL(blob);
            downloadLinkAdd.download = 'out_add.xlsx';
            downloadLinkAdd.style.display = 'inline-block';
            downloadLinkAdd.textContent = 'Download out_add.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created and top10 filter applied. Download the file with pivot added.</p>';

            // Clear PivotFilter from the specific PivotField
            pivotTable.pivotFilters.clearFilter(field.baseIndex);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save workbook after clearing filter
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLinkDelete = document.getElementById('downloadLinkDelete');
            downloadLinkDelete.href = URL.createObjectURL(blob2);
            downloadLinkDelete.download = 'out_delete.xlsx';
            downloadLinkDelete.style.display = 'inline-block';
            downloadLinkDelete.textContent = 'Download out_delete.xlsx';

            document.getElementById('result').innerHTML += '<p style="color: green;">Pivot filter cleared and data recalculated. Download the file with filter removed.</p>';
        });
    </script>
</html>
```
