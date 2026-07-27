---
title: Управление полями значений сводной таблицы в Aspose.Cells для .NET
linktitle: Поля значений
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ru/net/pivot-table-manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Поля значений — это ядро каждой сводной таблицы, числовые агрегаты, которые обобщают исходные данные. В Aspose.Cells for .NET область данных сводной таблицы заполняется путём добавления в неё базовых полей через `PivotTable.AddFieldToArea`, и каждое поле, помещённое в эту область, может иметь собственную функцию итогов. Когда существует два или более полей данных, Aspose.Cells предоставляет специальное агрегатное поле `PivotTable.ValuesField`, которое можно разместить на оси строк или столбцов в качестве базового поля, что даёт более точный контроль над тем, как поля значений отображаются в макете.
## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет перегрузку `PivotTable.AddFieldToArea(PivotFieldType, string)`, которая принимает константу `PivotFieldType.Data` и имя исходного столбца. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.DataFields`, в порядке добавления полей. По умолчанию числовой исходный столбец обобщается с помощью `ConsolidationFunction.Sum`, а нечисловой столбец по умолчанию получает `Count`.
## Изменение функции итогов
Каждое поле, помещённое в область данных, внутри оборачивается как экземпляр `PivotField`, и его свойство `Function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `Function` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.
{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, исходный столбец остаётся без изменений.
{{% /alert %}}
Таким образом, можно оставить одно поле данных как `Sum`, добавив при этом второе поле данных, которое ссылается на тот же исходный столбец, но использует `Count` или `Average`, всё в одной сводной таблице.
## Размещение полей значений на оси строк или столбцов
Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле под названием `PivotTable.ValuesField`. Это виртуальное поле представляет агрегат всех полей данных, находящихся в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводки, что удобно для размещения нескольких мер рядом.
{{% alert color="primary" %}}
`PivotTable.ValuesField` не работает, если полей значений нет или имеется только одно поле значений.
{{% /alert %}}
Приведённые ниже сценарии демонстрируют три комплексных примера, которые показывают каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.
## Сценарий 1 — Перетаскивание базового поля в область значений
Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После операции `Amount` появляется в области данных и по умолчанию вычисляется как `Sum` значений `Amount`.
```csharp
Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Заголовки в A1:D1
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// Строки данных A2:D9 с использованием вложенных циклов с ветвлением по j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// Добавить сводную таблицу в F3 с именем PivotTable1
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Структура сводной таблицы: Category и Item в строках, Year в столбцах, Amount как поле данных
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.RefreshData();
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## Сценарий 2 — Изменение функции итогов
Этот сценарий начинается с той же структуры сводной таблицы, что и Сценарий 1, но добавляет поле `Amount` в область данных дважды. Оба поля данных ссылаются на один и тот же исходный столбец, однако для второго поля с помощью сеттера `PivotField.Function` функция итогов переопределяется так, что оно становится `Count` вместо значения по умолчанию `Sum`.
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

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```
## Сценарий 3 — Размещение полей значений на оси строк или столбцов
Когда на месте есть два поля данных, `PivotTable.ValuesField` становится доступным для использования. Этот сценарий перетаскивает это агрегатное виртуальное поле в область столбцов так, что каждая мера в области данных появляется в виде отдельного блока столбцов рядом с `Year`.
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

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.RefreshData();
pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```
В совокупности эти три сценария охватывают все аспекты работы с полями значений в Aspose.Cells for .NET, от одного поля данных со значением по умолчанию `Sum` до сводной таблицы с несколькими мерами, в которой виртуальное `ValuesField` управляет макетом по оси строк или столбцов.
## Связанные статьи
- [Поля строк и столбцов сводной таблицы в Aspose.Cells for .NET](/cells/ru/net/row-and-column-fields/)
- [Поля страниц в сводных таблицах](/cells/ru/net/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for .NET](/cells/ru/net/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}