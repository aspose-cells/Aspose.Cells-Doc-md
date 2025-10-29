---
title: Указание абсолютного положения элемента сводной таблицы
type: docs
weight: 50
url: /ru/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Иногда пользователю нужно указать абсолютную позицию элементов сводной таблицы, Aspose.Cells for JavaScript через C++ API предоставил новые свойства и метод для достижения этого требования.

- Добавлено свойство [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик - количество позиций для перемещения элемента сводной таблицы вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, элемент сводной таблицы переместится вниз, параметр типа Boolean isSameParent указывает на то, должна ли операция перемещения выполняться в одном и том же родительском узле или нет.
- Устарел метод *PivotItem.move(int count)*, поэтому рекомендуется использовать недавно добавленный метод [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

В следующем демонстрационном коде создается сводная таблица, после чего указываются позиции элементов сводной таблицы в том же родительском узле. Вы можете загрузить [исходный файл Excel](5112632.xlsx) и [выходной файл Excel](5112619.xlsx) для вашего справочника. Если вы откроете выходной файл Excel, вы увидите, что элемент сводной таблицы "4H12" находится в 0-й позиции в родителе "K11", а "DIF400" находится на 3-й позиции. Точно так же CA32 находится на позиции 1, а AAA3 на позиции 2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
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
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Обратите внимание, что необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData перед использованием свойств [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-), [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) и метода [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}
