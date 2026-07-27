---
title: Добавить поля строк и столбцов сводной таблицы в Aspose.Cells для .NET
linktitle: Поля строк и столбцов
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ru/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**

Метод `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.

- `Row` — поля, размещённые вертикально слева
- `Column` — поля, размещённые горизонтально сверху
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые как фильтры отчёта

После добавления полей вы можете получить к ним доступ через свойства `PivotTable.RowFields` и `PivotTable.ColumnFields`. Каждое свойство возвращает коллекцию `PivotFieldCollection`. Поле с индексом 0 в `RowFields` является внешним полем строки, а последующие индексы представляют поля, вложенные в него. То же соглашение об индексации применяется к `ColumnFields`.

Порядок вложенности полей имеет значение. Добавление `Category` в область строк первым, а затем `Item` приводит к созданию сводной таблицы, в которой внешняя группировка — `Category`, а внутренняя — `Item`. Изменение порядка на обратный меняет иерархию.

## **Промежуточные итоги полей сводной таблицы**

Метод `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводной таблицы. Каждый вызов переключает отдельный тип промежуточного итога независимо. Передача `shown = true` отображает промежуточный итог, а `shown = false` скрывает его. Поскольку каждый вызов затрагивает только один тип, многократный вызов метода с разными значениями `subtotalType` формирует пользовательское подмножество промежуточных итогов.

Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.

- `Automatic` — Aspose.Cells выбирает значение по умолчанию (как правило, `Sum` для числовых полей)
- `None` — подавить все строки промежуточных итогов
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Промежуточные итоги отображаются только при наличии двух или более полей сводной таблицы в области строк (или в области столбцов). У единственного поля нет ничего осмысленного для подведения промежуточного итога между группами, поэтому в этом случае вызовы `SetSubtotals` не имеют видимого эффекта. Поэтому в этой статье во всех примерах размещаются два поля строк (`Category` внешнее, `Item` внутреннее), чтобы граница промежуточного итога между каждой группой `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — автоматические (по умолчанию) промежуточные итоги**

Если `SetSubtotals` вообще не вызывается, Aspose.Cells применяет выбор `Automatic` для числовых полей. Следующий пример явно подтверждает это поведение, вызывая `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` для внешнего поля строки `Category`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Сценарий 2 — подавление всех промежуточных итогов (None)**

Вызов `SetSubtotals(PivotFieldSubtotalType.None, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда требуются необработанные сгруппированные данные без каких-либо строк итогов.

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Сценарий 3 — пользовательское подмножество промежуточных итогов (Sum + Average)**

Вы не ограничены единственным типом промежуточного итога. Каждый вызов `SetSubtotals` действует независимо для одного типа, поэтому двойной вызов метода — один раз с `Sum` и один раз с `Average` — формирует пользовательское подмножество из двух строк промежуточных итогов для каждой группы `Category`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```
## **Резюме**

Все три приведённых выше сценария используют один и тот же набор данных и структуру сводной таблицы. Единственное различие между ними — вызов `SetSubtotals`, применяемый к внешнему полю строки `Category`. Помните правило двух полей: у единственного поля в области нет ничего, между чем можно подвести промежуточный итог, поэтому всегда размещайте как минимум два поля в области строк или столбцов, если хотите, чтобы `SetSubtotals` имел видимый эффект.

## **Связанные статьи**

- [Поля страниц в сводных таблицах](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
