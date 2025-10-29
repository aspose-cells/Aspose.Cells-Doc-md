---
title: Добавление вычисляемого поля в сводной таблице
type: docs
weight: 130
url: /ru/javascript-cpp/add-calculated-field-in-pivot-table/
description: Как добавить вычисляемое поле в сводную таблицу с помощью Aspose.Cells for JavaScript через C++.
keywords: Aspose.Cells for JavaScript через C++ для Excel, библиотека JavaScript для Excel, добавление вычисляемого поля в сводную таблицу с помощью JavaScript Library для Excel.
---

## **Возможные сценарии использования**
Когда вы создаете сводную таблицу на основе известных данных, вы обнаруживаете, что данные в ней не соответствуют вашим требованиям. Вы хотите объединить эти исходные данные. Например, вам нужно сложить, вычесть, умножить и разделить исходные данные перед тем, как вы их захотите. В этом случае вам нужно создать вычисляемое поле и установить соответствующую формулу для вычислений. Затем выполнить некоторые статистические и другие операции с вычисляемым полем. 

## **Как добавить вычисляемое поле в сводную таблицу в Excel**
Чтобы добавить вычисляемое поле в сводную таблицу в Excel, выполните следующие шаги:

1. Выберите сводную таблицу, к которой вы хотите добавить вычисляемое поле. 
2. Перейдите на вкладку Analyze в контекстном меню сводной таблицы.
3. Нажмите на "Поля, элементы и наборы" и затем выберите "Вычисляемое поле" в выпадающем меню.
4. В поле "Имя" введите имя для вычисляемого поля.
5. В поле "Формула" введите формулу для выполнения расчета, используя соответствующие имена полей сводной таблицы и математические операторы. 
<br>
<img src="1.png" width=80% />
6. Нажмите "ОК", чтобы создать вычисляемое поле.
7. Новое вычисляемое поле появится в списке полей сводной таблицы в разделе 'Значения'.
8. Перетащите вычисляемое поле в раздел 'Значения' сводной таблицы, чтобы отобразить вычисленные значения.
<br>
<img src="2.png" width=80% />

## **Как добавить вычисляемое поле в сводную таблицу с помощью Aspose.Cells for JavaScript через C++**
Добавьте вычисляемое поле в Excel-файл с помощью Aspose.Cells for JavaScript на C++. См. следующий пример кода. После выполнения примерного кода к листу добавляется сводная таблица с вычисляемым полем.
1. Задайте исходные данные и создайте сводную таблицу. 
2. Создайте расчетное поле согласно существующему PivotField в сводной таблице.
3. Добавьте расчетное поле в область данных. 
4. Наконец, сохраните книгу в формате [output XLSX](out.xlsx). 

## **Образец кода**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
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
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
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
