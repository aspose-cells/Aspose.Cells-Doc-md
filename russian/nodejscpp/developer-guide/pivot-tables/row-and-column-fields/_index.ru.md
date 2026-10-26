---
title: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for Node.js с помощью C++
linktitle: Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for Node.js с помощью C++
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять подытогами полей сводной таблицы с помощью PivotField.setSubtotals в Aspose.Cells for Node.js с помощью C++
keywords: Aspose.Cells, Node.js, C++, сводная таблица, поле строки, поле столбца, PivotField, SetSubtotals, PivotFieldSubtotalType, подытоги
type: docs
weight: 220
url: /ru/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Добавление поля в область строк или столбцов**
Метод `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` перемещает базовое поле из исходных данных в одну из четырех областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.
- `Row` — поля, размещенные вертикально слева
- `Column` — поля, размещенные горизонтально в верхней части
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые в качестве фильтров отчета
Порядок вложения полей важен. Если сначала добавить `Category` в область строк, а затем `Item`, получится сводная таблица, в которой `Category` образует внешнюю группировку, а `Item` — внутреннюю. Изменение порядка добавит reverses иерархию.

## **Подытоги полей сводной таблицы**
Метод `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` определяет, какие строки подытогов отображаются для поля сводной таблицы. Каждый вызов независимо включает или отключает один тип подытога. Передача `shown = true` отображает подытог, а `shown = false` скрывает его. Поскольку каждый вызов затрагивает только один тип, повторные вызовы с различными значениями `subtotalType` позволяют сформировать настраиваемое подмножество подытогов.
Перечисление `PivotFieldSubtotalType` определяет доступные типы подытогов.
- `Automatic` — Aspose.Cells выбирает вариант по умолчанию (обычно `Sum` для числовых полей)
- `None` — отключает отображение всех строк подытогов
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
Подытоги отображаются, только если в области строк (или столбцов) размещено два или более полей сводной таблицы. При наличии только одного поля нет промежуточного уровня, на котором можно рассчитать подытоги, поэтому вызовы `setSubtotals` в этом случае не имеют видимого эффекта. Поэтому в каждом примере этой статьи в область строк добавляются два поля (`Category` — внешнее, `Item` — внутреннее), чтобы для каждой группы `Category` была видна граница, на которой рассчитываются подытоги.
{{% /alert %}}

## **Сценарий 1 — Автоматические подытоги (по умолчанию)**
Если метод `setSubtotals` не вызывается, Aspose.Cells применяет к числовым полям вариант `Automatic`. Следующий пример явно подтверждает это поведение: для внешнего поля строки `Category` вызывается `setSubtotals(PivotFieldSubtotalType.Automatic, true)`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Сценарий 2 — Отключение всех подытогов (None)**
Вызов `setSubtotals(PivotFieldSubtotalType.None, true)` удаляет из сводной таблицы все строки подытогов, оставляя только строки полей и общий итог в нижней части. Это полезно, если требуется отображать исходные сгруппированные данные без каких-либо строк сводки.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Сценарий 3 — Настраиваемое подмножество подытогов (Sum + Average)**
Использовать один тип подытога необязательно. Каждый вызов `setSubtotals` действует только на один тип, поэтому два вызова метода — один с `Sum`, другой с `Average` — формируют настраиваемое подмножество из двух строк подытогов для каждой группы `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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

## **Краткие итоги**
Три сценария отличаются только вызовами метода `setSubtotals`. Всё остальное — набор данных, поля и области, которым они назначены, — идентично, что делает макеты непосредственно сопоставимыми.
- **Размещение полей.** Метод `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` перемещает исходный столбец в определённую область. Внутри одной области порядок вызовов определяет порядок отображения, поэтому первый вызов создаёт самую внешнюю группу. Для вычисления промежуточных итогов необходимо наличие двух или более полей в одной и той же области: при наличии одного поля между группами просто отсутствует место для вставки промежуточных итогов.
- **Сценарий 1 — автоматические промежуточные итоги.** Если метод `setSubtotals` не вызывается, выбор по умолчанию остаётся за Excel, который применяет свой собственный промежуточный итог к числовым полям. Вызов `setSubtotals` с параметром `AsposeCells.PivotFieldSubtotalType.Automatic` явным образом фиксирует этот выбор, а не оставляет его неявным.
- **Сценарий 2 — отсутствие промежуточных итогов.** Вызов `setSubtotals` с параметром `AsposeCells.PivotFieldSubtotalType.None` отключает промежуточный итог по умолчанию, поэтому сводная таблица сохраняет строки полей и общий итог, но исключает строки промежуточных итогов, которые Excel в противном случае вставлял бы между ними.
- **Сценарий 3 — выбранный поднабор.** Каждый вызов переключает ровно один тип промежуточного итога, при этом вызовы накапливаются, а не сбрасывают друг друга. Следовательно, двукратный вызов — первый с параметром `AsposeCells.PivotFieldSubtotalType.Sum`, второй с `AsposeCells.PivotFieldSubtotalType.Average` — оставляет оба типа включёнными, и сводная таблица отображает как промежуточный итог по сумме, так и промежуточный итог по среднему значению, а также общий итог.

{{% alert color="primary" %}}
Ничего в работе с промежуточными итогами не связано строго с областью строк. Те же самые вызовы `setSubtotals`, применённые к полю, полученному из `PivotTable.ColumnFields`, создают такие же три макета по оси столбцов, поскольку настройка принадлежит сводному полю, а не оси, на которой оно расположено.
{{% /alert %}}

## **Связанные статьи**
- [Поля страницы в сводных таблицах](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Node.js с помощью C++](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}