---
title: Filter in Pivot Tabelle löschen
type: docs
weight: 130
url: /de/javascript-cpp/clear-filter-in-pivot-table/
description: Wie man den PivotFilter eines bestimmten PivotFields in der Pivot Tabelle mit Aspose.Cells for JavaScript via C++ löscht.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript Bibliothek, Löschen des PivotFilters in der Pivot Tabelle mit Aspose.Cells for JavaScript via C++ Excel Bibliothek.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie eine Pivot-Tabelle mit bekannten Daten erstellen und filtern möchten, müssen Sie lernen und den Filter verwenden. Es kann Ihnen helfen, die gewünschten Daten effektiv herauszufiltern. Durch Verwendung der Aspose.Cells for JavaScript API via C++ können Sie Operationen auf dem Filterfeld in Pivot-Tabellen durchführen. 

## **Wie Sie den Filter in der Pivot-Tabelle in Excel löschen**
Filter in Pivot-Tabelle in Excel löschen, befolgen Sie diese Schritte:

1. Wählen Sie die Pivot-Tabelle aus, aus der Sie den Filter löschen möchten. 
2. Klicken Sie auf den Dropdown-Pfeil für den Filter, den Sie in der Pivot-Tabelle löschen möchten.
3. Wählen Sie "Filter löschen" aus dem Dropdown-Menü aus.
<img src="1.png" width=80% />
4. Wenn Sie alle Filter aus der Pivot-Tabelle löschen möchten, können Sie auch auf die Schaltfläche "Filter löschen" im PivotTable-Analyse-Tab im Menüband in Excel klicken.
<img src="2.png" width=80% />

## **Wie man den Filter in Pivot-Tabellen mit Aspose.Cells for JavaScript via C++ löscht**
Den Filter in Pivot-Tabellen mit Aspose.Cells for JavaScript via C++ löschen. Bitte sehen Sie sich den folgenden Beispielcode an. 
1. Daten setzen und eine Pivot-Tabelle basierend darauf erstellen. 
2. Einen Filter auf das Zeilenfeld der Pivot-Tabelle hinzufügen. 
3. Die Arbeitsmappe im Format [output XLSX](out_add.xlsx) speichern. Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle mit einem Top10-Filter zum Arbeitsblatt hinzugefügt. 
4. Den Filter auf einem bestimmten Pivot-Feld löschen. Nach Ausführung des Codes zum Löschen des Filters wird der Filter auf dem spezifischen Pivot-Feld gelöscht. Bitte prüfen Sie das [output XLSX](out_delete.xlsx).

## **Beispielcode**
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
