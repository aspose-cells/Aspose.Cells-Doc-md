---
title: Вставка сводной таблицы
linktitle: Сводные таблицы
type: docs
weight: 160
url: /ru/javascript-cpp/create-pivot-table/
description: Создание и форматирование сводных таблиц файла электронной таблицы Excel.
---

## **Создать сводную таблицу**

Можно использовать Aspose.Cells for JavaScript через C++ для программного добавления сводных таблиц в электронные таблицы.

### **Модель объекта сводной таблицы**

Aspose.Cells for JavaScript через C++ предоставляет специальный набор классов, используемых для создания и управления сводными таблицами. Эти классы создают и устанавливают объекты [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable), являющиеся строительными блоками сводной таблицы. Объекты:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) в [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) представляет собой сводную таблицу на листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) представляет собой коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) на листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**

1. Добавьте данные на лист с использованием метода [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) объекта [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).
   Эти данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) коллекции [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection), который инкапсулирован в объекте Лист.
1. Получите доступ к новому объекту [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) из коллекции [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection), передав индекс сводной таблицы.
1. Используйте любые из объектов [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) (описанных выше), чтобы управлять сводной таблицей.

После выполнения примера кода сводная таблица добавляется на лист.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен проходить сверху вниз. Например, "A1:C3" допустим, но "C3:A1" - нет.

{{% /alert %}}
