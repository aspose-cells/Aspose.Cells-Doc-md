---
title: Row and Column Fields in Aspose.Cells for Node.js via Java
linktitle: Поля строк и столбцов
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ru/nodejs-java/row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Поля строк и столбцов являются строительными блоками сводной таблицы. Поле, помещённое в область строк, отображается вертикально слева в сводной таблице, тогда как поле, помещённое в область столбцов, отображается горизонтально в верхней части. В этой статье показано, как программно добавлять базовые поля в эти области и как управлять промежуточными итогами, которые отображаются между группами полей, с помощью метода `PivotField.setSubtotals`.

## **Добавление поля в область строк или столбцов**

Метод `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.

- `ROW` — поля, размещаемые вертикально слева
- `COLUMN` — поля, размещаемые горизонтально в верхней части
- `DATA` — поля, значения которых агрегируются
- `PAGE` — поля, используемые в качестве фильтров отчёта

После добавления полей вы можете получить к ним доступ через свойства `PivotTable.getRowFields()` и `PivotTable.getColumnFields()`. Каждое свойство возвращает `PivotFieldCollection`. Поле с индексом 0 в `RowFields` является самым внешним полем строки, а последующие индексы представляют поля, вложенные в него. Та же самая индексация применяется и к `ColumnFields`.

Порядок вложенности полей имеет значение. Добавление `Category` в область строк первым, а затем `Item` создаёт сводную таблицу, в которой внешняя группировка — `Category`, а внутренняя — `Item`. Изменение порядка на противоположный меняет иерархию.

## **Промежуточные итоги поля сводной таблицы**

Метод `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводной таблицы. Каждый вызов независимо переключает отдельный тип промежуточного итога. Передача `shown = true` отображает промежуточный итог, а `shown = false` скрывает его. Поскольку каждый вызов влияет только на один тип, многократный вызов метода с разными значениями `subtotalType` формирует пользовательское подмножество промежуточных итогов.

Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.

- `AUTOMATIC` — Aspose.Cells выбирает вариант по умолчанию (обычно `SUM` для числовых полей)
- `NONE` — подавить все строки промежуточных итогов
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
Промежуточные итоги отображаются только при наличии двух или более полей сводной таблицы в области строк (или в области столбцов). Для одного поля нет ничего значимого для подведения промежуточных итогов между ними, поэтому в этом случае вызовы `setSubtotals` не имеют видимого эффекта. Поэтому в данной статье во всех примерах размещены два поля строк (`Category` — внешнее, `Item` — внутреннее), чтобы граница промежуточных итогов между каждой группой `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — Автоматические (по умолчанию) промежуточные итоги**

Если вы вообще не вызываете `setSubtotals`, Aspose.Cells применяет выбор `AUTOMATIC` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` на внешнем поле строки `Category`.

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Сценарий 2 — Подавление всех промежуточных итогов (None)**

Вызов `setSubtotals(PivotFieldSubtotalType.NONE, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда нужны необработанные сгруппированные данные без каких-либо строк итогов.

```javascript
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

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Сценарий 3 — Пользовательское подмножество промежуточных итогов (Sum + Average)**

Вы не ограничены одним типом промежуточного итога. Каждый вызов `setSubtotals` работает независимо над одним типом, поэтому двукратный вызов метода — один раз с `SUM` и один раз с `AVERAGE` — создаёт пользовательское подмножество из двух строк промежуточных итогов для каждой группы `Category`.

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
## **Резюме**

Три приведённых выше сценария используют один и тот же набор данных и структуру сводной таблицы. Единственное различие между ними — вызов `setSubtotals`, применяемый к внешнему полю строки `Category`. Помните правило двух полей: одно поле в области не имеет ничего для подведения промежуточных итогов между ними, поэтому всегда размещайте как минимум два поля в области строк или столбцов, если вы хотите, чтобы `setSubtotals` имел видимый эффект.

## **Связанные статьи**

- [Поля страниц в сводных таблицах](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
