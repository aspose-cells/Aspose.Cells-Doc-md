---
title: Поля строк и столбцов в Aspose.Cells for .NET
linktitle: Поля строк и столбцов
description: Узнайте, как добавлять базовые поля в области строк и столбцов сводной таблицы и управлять промежуточными итогами полей сводной таблицы с помощью PivotField.SetSubtotals в Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, сводная таблица, поле строки, поле столбца, PivotField, SetSubtotals, PivotFieldSubtotalType, промежуточные итоги
type: docs
weight: 220
url: /ru/net/row-and-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Поля строк и столбцов являются основой сводной таблицы. Поле, размещённое в области строк, отображается вертикально слева в сводной таблице, а поле, размещённое в области столбцов, отображается горизонтально сверху. В этой статье показано, как программно добавлять базовые поля в эти области, и как управлять промежуточными итогами, которые отображаются между группами полей, с помощью метода `PivotField.SetSubtotals`.

## **Добавление поля в область строк или столбцов**

Метод `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` перемещает базовое поле из исходных данных в одну из четырёх областей сводной таблицы. Аргумент `fieldType` принимает одно из следующих значений `PivotFieldType`.

- `Row` — поля, размещаемые вертикально слева
- `Column` — поля, размещаемые горизонтально сверху
- `Data` — поля, значения которых агрегируются
- `Page` — поля, используемые в качестве фильтров отчёта

После добавления полей к ним можно получить доступ через свойства `PivotTable.RowFields` и `PivotTable.ColumnFields`. Каждое свойство возвращает коллекцию `PivotFieldCollection`. Поле с индексом 0 в `RowFields` является самым внешним полем строки, а последующие индексы представляют поля, вложенные в него. То же соглашение об индексации применяется к `ColumnFields`.

Порядок вложенности полей имеет значение. Добавление `Category` в область строк первым, а затем `Item` создаёт сводную таблицу, внешняя группировка которой — `Category`, а внутренняя — `Item`. Изменение порядка на противоположный меняет иерархию.

## **Промежуточные итоги поля сводной таблицы**

Метод `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` управляет тем, какие строки промежуточных итогов отображаются для поля сводной таблицы. Каждый вызов независимо переключает один тип промежуточного итога. Передача `shown = true` отображает промежуточный итог, а `shown = false` скрывает его. Поскольку каждый вызов влияет только на один тип, многократный вызов метода с разными значениями `subtotalType` формирует пользовательское подмножество промежуточных итогов.

Перечисление `PivotFieldSubtotalType` определяет доступные виды промежуточных итогов.

- `Automatic` — Aspose.Cells применяет выбор по умолчанию (обычно `Sum` для числовых полей)
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
Промежуточные итоги отображаются только при наличии двух или более полей сводной таблицы в области строк (или в области столбцов). Для одного поля нет ничего значимого для расчёта промежуточного итога, поэтому вызовы `SetSubtotals` в этом случае не имеют видимого эффекта. Поэтому в этой статье во всех примерах размещаются два поля строк (`Category` — внешнее, `Item` — внутреннее), чтобы граница промежуточных итогов между группами `Category` была видна.
{{% /alert %}}

## **Сценарий 1 — Автоматические (по умолчанию) промежуточные итоги**

Если `SetSubtotals` вообще не вызывается, Aspose.Cells применяет выбор `Automatic` к числовым полям. Следующий пример явно подтверждает это поведение, вызывая `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` на внешнем поле строки `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **Сценарий 2 — Подавление всех промежуточных итогов (None)**

Вызов `SetSubtotals(PivotFieldSubtotalType.None, true)` удаляет все строки промежуточных итогов из сводной таблицы, оставляя только строки полей и общий итог внизу. Это полезно, когда нужны исходные сгруппированные данные без каких-либо строк промежуточных итогов.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **Сценарий 3 — Пользовательское подмножество промежуточных итогов (Sum + Average)**

Вы не ограничены одним типом промежуточного итога. Каждый вызов `SetSubtotals` действует независимо на один тип, поэтому двукратный вызов метода — один раз с `Sum` и один раз с `Average` — создаёт пользовательское подмножество из двух строк промежуточных итогов для каждой группы `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **Резюме**

Три приведённых выше сценария используют один и тот же набор данных и структуру сводной таблицы. Единственное различие между ними — это вызов `SetSubtotals`, применяемый к внешнему полю строки `Category`. Помните о правиле двух полей: одно поле в области не имеет ничего для расчёта промежуточного итога, поэтому всегда размещайте как минимум два поля в области строк или столбцов, если хотите, чтобы `SetSubtotals` оказывал видимый эффект.

## **Связанные статьи**

- [Поля страниц в сводных таблицах](/cells/ru/net/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for .NET](/cells/ru/net/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
