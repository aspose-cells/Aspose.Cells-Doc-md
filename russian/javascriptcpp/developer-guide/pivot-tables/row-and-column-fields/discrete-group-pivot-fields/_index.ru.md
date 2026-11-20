---
title: Дискретная группировка элементов поля сводной таблицы
linktitle: Дискретная группировка
description: Узнайте, как группировать элементы поля сводной таблицы в пользовательские группы с заданными именами, например «фрукты» и «овощи», с помощью DiscreteGroupItem и PivotFieldGroupOptions.discreteGroupItems в Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, сводная таблица, дискретная группировка, DiscreteGroupItem, PivotFieldGroupOptions, группировка элементов сводной таблицы, пользовательские группы, PivotField.group, Aspose.Cells for JavaScript via C++, сводная таблица Excel
type: docs
weight: 90
url: /ru/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Автоматическая группировка объединяет элементы по типу данных: например, даты группируются по месяцам и кварталам, а числа — по диапазонам. Дискретная группировка решает противоположную задачу, объединяя конкретные несвязанные элементы в пользовательские группы с заданными именами: например, продукты — в группы «фрукты» и «овощи», магазины — по регионам, а счета — по зонам. Aspose.Cells предоставляет дискретную группировку с помощью класса `DiscreteGroupItem` и свойства `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` представляет собой имя группы и входящие в нее элементы. Элементы можно идентифицировать двумя способами: по именам (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) или по их позициям в исходных данных с нулевой нумерацией (`new DiscreteGroupItem("fruit", [0, 3])`). Обе формы дают одинаковый результат.
- Дискретная группировка применяется к полю в области строк или столбцов сводной таблицы: для этого параметры группировки передаются в `PivotField.group(PivotFieldGroupOptions)`.

## **Группировка элементов поля сводной таблицы по именам элементов**
В следующем примере создается небольшой список продаж (продукт, дата и сумма), а затем на его основе создается сводная таблица с полем `product` в области строк, `date` — в области столбцов и `amount` — в области данных. Затем по именам элементов формируются две пользовательские группы: `fruit` (`grape`, `cherry`) и `vegetable` (`carrot`, `potato`). В результате создается двухуровневая компоновка строк: имя группы отображается на внешнем уровне, а исходные элементы располагаются внутри соответствующей группы. Благодаря этому тенденции можно анализировать отдельно по каждой пользовательской группе и каждому элементу.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

После вызова `calculateData()` в области строк сводной таблицы отображаются `fruit` (`grape` 50, `cherry` 80) и `vegetable` (`carrot` 60, `potato` 70), общий итог составляет 260, а подписи столбцов по-прежнему содержат четыре даты (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Группировка элементов поля сводной таблицы по индексам элементов**
Если имена элементов длинные или локализованы, второй конструктор `DiscreteGroupItem` позволяет определить элементы по индексу. Индекс элемента — это его позиция в порядке появления в исходных данных, а не в алфавитном порядке. Нумерация начинается с нуля. В приведенных выше тестовых данных `grape` имеет индекс 0, `carrot` — индекс 1, `potato` — индекс 2, а `cherry` — индекс 3; следовательно, для `fruit` используются индексы `{ 0, 3 }`, а для `vegetable` — `{ 1, 2 }`. Результат совпадает с результатом группировки по именам.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Примечание**

{{% alert color="primary" %}}
- Элементы, не включенные ни в одну пользовательскую группу, не теряются. Каждый из них остается в сводной таблице на том же уровне, что и пользовательские группы, в виде отдельной одноэлементной записи. В приведенном выше примере определение только группы `fruit` оставляет `carrot` и `potato` в области строк как отдельные записи рядом с группой `fruit`.
- Свойство `PivotFieldGroupOptions.newPivotField` управляет компоновкой дискретной группировки. По умолчанию оно имеет значение `true`, при котором группируемое поле добавляется в качестве нового внешнего поля рядом с исходным. В результате создается показанная выше двухуровневая компоновка (`rowFields` увеличивается до 2). Установите значение `false`, чтобы заменить исходное поле. Тогда в области строк отображается только один уровень с именами групп и их агрегированными значениями: `fruit` — 130 (50 + 80) и `vegetable` — 130 (60 + 70).
- Формы конструктора `DiscreteGroupItem`, основанные на именах и индексах, можно комбинировать в одном массиве `discreteGroupItems`.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей в сводной таблице](/cells/ru/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Применение стиля к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}