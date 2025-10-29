---
title: Добавить фильтр в сводной таблице
type: docs
weight: 130
url: /ru/javascript-cpp/add-filter-in-pivot-table/
description: Узнайте, как добавлять фильтр в сводную таблицу с помощью Aspose.Cells for JavaScript на C++.
keywords: Aspose.Cells for JavaScript для Excel на C++, библиотека Excel JavaScript, добавление фильтра в сводную таблицу с помощью библиотеки Aspose.Cells for JavaScript для Excel.
---

## **Возможные сценарии использования**
При создании сводной таблицы с известными данными и необходимости фильтрации сводной таблицы, необходимо изучить и использовать фильтр. Он поможет эффективно отфильтровать нужные данные. Используя API Aspose.Cells for JavaScript на C++, вы можете добавлять фильтр к значениям поля в сводных таблицах. 

## **Добавление фильтра в сводную таблицу с помощью Aspose.Cells for JavaScript на C++**
Пожалуйста, ознакомьтесь с следующим образцовым кодом. Он устанавливает данные и создает сводную таблицу на их основе. Затем добавьте фильтр на поля строк сводной таблицы. Наконец, сохраните книгу в формате [output XLSX](filterout.xlsx). После выполнения примера кода книга Excel с фильтром top10 добавляется в рабочий лист.

## **Образец кода**
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
            // Creating a new Workbook object
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;
            // Setting the value to the cells (converted putValue -> value)
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

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:B8", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Count");

            // Converted getDataFields().get(0).setFunction(...) -> dataFields.get(0).function = ...
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;

            // Converted getRowFields().get(0) -> rowFields.get(0)
            const field = pivotTable.rowFields.get(0);
            // Converted setIsAutoSort(true) -> isAutoSort = true
            field.isAutoSort = true;
            // Converted setIsAscendSort(false) -> isAscendSort = false
            field.isAscendSort = false;
            // Converted setAutoSortField(0) -> autoSortField = 0
            field.autoSortField = 0;

            // Add top10 filter (converted getPivotFilters -> pivotFilters and getAutoFilter -> autoFilter)
            const index = pivotTable.pivotFilters.add(0, AsposeCells.PivotFilterType.Count);
            const filter = pivotTable.pivotFilters.get(index);
            filter.autoFilter.filterTop10(0, true, false, 5);

            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
