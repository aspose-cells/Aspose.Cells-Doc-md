---
title: Добавление полей строк и столбцов в сводную таблицу в Aspose.Cells for Node.js via Java
linktitle: Добавление полей строк и столбцов в сводную таблицу в Aspose.Cells for Node.js via Java
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять подытогами полей сводной таблицы с помощью PivotField.setSubtotals в Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, сводная таблица, поле строк, поле столбцов, PivotField, setSubtotals, PivotFieldSubtotalType, подытоги
type: docs
weight: 220
url: /ru/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**
Метод `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` перемещает базовое поле из исходных данных в одну из четырех областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.
- `ROW` — поля, размещенные вертикально слева
- `COLUMN` — поля, размещенные горизонтально сверху
- `DATA` — поля, значения которых агрегируются
- `PAGE` — поля, используемые в качестве фильтров отчета
Порядок вложения полей имеет значение. Если сначала добавить `Category` в область строк, а затем `Item`, внешняя группировка будет выполняться по `Category`, а внутренняя — по `Item`. Изменение порядка меняет иерархию.

## **Подытоги поля сводной таблицы**
Метод `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` управляет отображением строк подытогов для поля сводной таблицы. Каждый вызов независимо включает или отключает один тип подытога. При передаче `shown = true` подытог отображается, а при `shown = false` — скрывается. Поскольку каждый вызов затрагивает только один тип, несколько вызовов метода с различными значениями `subtotalType` позволяют сформировать пользовательский набор подытогов.
Перечисление `PivotFieldSubtotalType` определяет доступные типы подытогов.
- `AUTOMATIC` — Aspose.Cells выбирает вариант по умолчанию (обычно `SUM` для числовых полей)
- `NONE` — отключает отображение всех строк подытогов
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Подытоги отображаются только тогда, когда в области строк (или области столбцов) есть два или более полей сводной таблицы. Для одного поля нет внутренних групп, между которыми можно было бы вычислить подытог, поэтому вызовы `setSubtotals` в таком случае не имеют видимого эффекта. Поэтому в каждом примере этой статьи используются два поля строк (`Category` — внешнее, `Item` — внутреннее), чтобы была видна граница подытога для каждой группы `Category`.
{{% /alert %}}

## **Сценарий 1 — Автоматические подытоги (по умолчанию)**
Если метод `setSubtotals` вообще не вызывается, Aspose.Cells использует вариант `AUTOMATIC` для числовых полей. В следующем примере это поведение явно подтверждается вызовом `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` для внешнего поля строк `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Сценарий 2 — Подавление всех подытогов (NONE)**
Вызов `setSubtotals(PivotFieldSubtotalType.NONE, true)` удаляет все строки подытогов из сводной таблицы, оставляя только строки полей и общий итог в нижней части. Это полезно, когда требуются сгруппированные данные без каких-либо строк с итогами.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Сценарий 3 — Пользовательский набор подытогов (сумма + среднее)**
Можно использовать несколько типов подытогов. Каждый вызов `setSubtotals` независимо воздействует на один тип, поэтому два вызова метода — с `SUM` и `AVERAGE` — формируют пользовательский набор из двух строк подытогов для каждой группы `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Заключение**
Три сценария различаются только вызовами метода `setSubtotals`. Всё остальное — набор данных, поля и области, в которые они назначены, — одинаково, что и делает макеты прямо сравнимыми друг с другом.
- **Размещение полей.** Вызов `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` перемещает исходный столбец в указанную область. В пределах одной области порядок вызовов определяет порядок отображения: первый вызов формирует наиболее внешнюю группу. Для вычисления промежуточных итогов требуется два или более полей в одной области: при наличии только одного поля промежуточные итоги вычислять не между какими элементами.
- **Сценарий 1 — автоматические промежуточные итоги.** Отсутствие вызова `setSubtotals` оставляет выбор за Excel, который применяет собственный стандартный промежуточный итог к числовым полям. Явный вызов `setSubtotals` с параметром `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` фиксирует этот выбор, делая его явным, а не оставляя подразумеваемым.
- **Сценарий 2 — отсутствие промежуточных итогов.** Вызов `setSubtotals` с параметром `AsposeCells.PivotFieldSubtotalType.NONE` отключает стандартный промежуточный итог, в результате чего сводная таблица сохраняет строки полей и общий итог, но не вставляет между ними строки промежуточных итогов, которые иначе добавлял бы Excel.
- **Сценарий 3 — выбранный набор типов итогов.** Каждый вызов включает или отключает ровно один тип промежуточного итога, и вызовы накапливаются, не сбрасывая друг друга. Таким образом, один вызов с `AsposeCells.PivotFieldSubtotalType.SUM` и один вызов с `AsposeCells.PivotFieldSubtotalType.AVERAGE` одновременно включают оба типа итогов, и сводная таблица отображает промежуточный итог по сумме, промежуточный итог по среднему значению и общий итог.

{{% alert color="primary" %}}
Особенности работы с промежуточными итогами не относятся исключительно к строковой области. Те же самые вызовы `setSubtotals`, применённые к полю из `PivotTable.ColumnFields`, создают те же три макета на оси столбцов, поскольку параметр относится к самому полю сводной таблицы, а не к той оси, на которой оно размещено.
{{% /alert %}}

## **Связанные статьи**
- [Поля страницы в сводных таблицах](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}