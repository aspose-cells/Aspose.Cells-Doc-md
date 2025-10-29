---
title: Очистить фильтр в сводной таблице
type: docs
weight: 130
url: /ru/javascript-cpp/clear-filter-in-pivot-table/
description: Как очистить фильтр PivotFilter в конкретном поле сводной таблицы с помощью Aspose.Cells for JavaScript на C++.
keywords: Aspose.Cells for JavaScript для Excel на C++, библиотека Excel JavaScript, очистка фильтра PivotFilter в сводной таблице с помощью Aspose.Cells for JavaScript на C++ Excel.
---

## **Возможные сценарии использования**
При создании сводной таблицы с известными данными и необходимости фильтрации сводной таблицы, необходимо изучить и использовать фильтр. Он поможет эффективно отфильтровать нужные данные. Используя API Aspose.Cells for JavaScript на C++, вы можете управлять фильтрами по значениям поля в сводных таблицах. 

## **Как очистить фильтр в сводной таблице в Excel**
Очистить фильтр в сводной таблице Excel, следуйте этим шагам:

1. Выберите сводную таблицу, которую вы хотите очистить от фильтра. 
2. Нажмите на стрелку-раскрывающееся меню для фильтра, который вы хотите очистить в сводной таблице.
3. Выберите "Очистить фильтр" в выпадающем меню.
<img src="1.png" width=80% />
4. Если вы хотите очистить все фильтры из сводной таблицы, вы также можете щелкнуть кнопку "Очистить фильтры" на вкладке Анализ сводной таблицы на ленте в Excel.
<img src="2.png" width=80% />

## **Как очистить фильтр в сводной таблице с помощью Aspose.Cells for JavaScript на C++**
Очистка фильтра в сводной таблице с помощью Aspose.Cells for JavaScript на C++. См. следующий пример кода. 
1. Задайте данные и создайте сводную таблицу на их основе. 
2. Добавьте фильтр на строковое поле сводной таблицы. 
3. Сохраните книгу в формате [output XLSX](out_add.xlsx). После выполнения примера кода, в рабочую книгу будет добавлена сводная таблица с фильтром top10. 
4. Очистите фильтр в конкретном поле сводной таблицы. После выполнения кода для очистки фильтра, фильтр в конкретном поле сводной таблицы будет очищен. Пожалуйста, проверьте [output XLSX](out_delete.xlsx).

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
