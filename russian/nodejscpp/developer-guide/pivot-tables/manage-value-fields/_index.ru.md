---
title: Управление полями значений сводной таблицы в Aspose.Cells для .NET
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Node.js via C++.
linktitle: Поля значений
keywords: Aspose.Cells, Node.js via C++, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ru/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет метод `PivotTable.addFieldToArea(PivotFieldType, string)`, перегрузку, которая принимает константу `PivotFieldType.Data` и имя исходного столбца. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.getDataFields()` в порядке добавления полей. По умолчанию числовой исходный столбец агрегируется функцией `ConsolidationFunction.Sum`, а нечисловой — `Count`.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField());
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

## Изменение функции итогов
Каждое поле, помещённое в область данных, внутренне оборачивается как экземпляр `PivotField`, а его свойство `getFunction()` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `setFunction()` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.

{{% alert color="primary" %}}
Изменение функции итогов влияет только на агрегат, исходный столбец не изменяется.
{{% /alert %}}

Таким образом, вы можете оставить одно поле данных как `Sum`, добавив второе поле данных, ссылающееся на тот же исходный столбец, но использующее `Count` или `Average`, — всё это в одной сводной таблице.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Размещение полей значений на оси строк или столбцов
Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле, называемое `PivotTable.getValuesField`. Это виртуальное поле представляет собой агрегат каждого поля данных, находящегося в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что удобно для расположения нескольких мер рядом.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` не работает, если поле значений отсутствует или является единственным.
{{% /alert %}}

Приведённые ниже сценарии демонстрируют три полных примера, которые показывают каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}