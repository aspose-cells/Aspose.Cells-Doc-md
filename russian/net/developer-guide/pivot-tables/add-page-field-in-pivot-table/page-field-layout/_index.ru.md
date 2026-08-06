---
title: Изменение макета поля страницы в сводной таблице
linktitle: Изменение макета поля страницы в сводной таблице
description: Узнайте, как управлять макетом области полей страницы в сводной таблице с помощью Aspose.Cells for .NET, включая настройку порядка отображения, количества полей в строке и порядка полей страницы в верхней части сводной таблицы.
keywords: Aspose.Cells, библиотека NET, электронные таблицы, сводная таблица, поле страницы, порядок полей страницы, количество полей страницы в строке, перемещение поля страницы
type: docs
weight: 191
url: /ru/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Эта статья является продолжением темы **Добавление поля страницы в сводной таблице**. В ней показано, как управлять макетом области полей страницы — полосы элементов управления фильтрами в верхней части сводной таблицы — включая порядок отображения, количество полей в строке и изменение порядка полей.

{{% /alert %}}

## **Введение**

В Microsoft Excel сводная таблица имеет выделенную **область полей страницы**, которая располагается над телом таблицы со строками, столбцами и данными. Эта область отображается в виде полосы выпадающих элементов управления фильтрами (по одному на каждое поле страницы), и именно на них пользователь нажимает, чтобы выполнить срезку сводной таблицы по таким критериям, как год или регион. Aspose.Cells моделирует эту область через коллекцию `PivotTable.PageFields` и предоставляет три свойства, управляющих визуальным расположением полосы:

- `PivotTable.PageFieldOrder` (значение `Aspose.Cells.PrintOrderType`) определяет, будут ли дополнительные поля страницы размещены *рядом* с существующими или *под* ними.
- `PivotTable.PageFieldWrapCount` задаёт, сколько полей страницы размещается в одной строке или столбце до переноса.
- `PivotTable.PageFields.Move(currIndex, destIndex)` изменяет порядок полей страницы без изменения режима порядка.

В этой статье рассматриваются три примера кода, демонстрирующие каждую из этих операций на общем наборе данных, чтобы можно было сравнить получившиеся макеты рядом.

## **Исходные данные**

Во всех трёх примерах ниже эти восемь строк данных о продажах загружаются на рабочий лист с именем `PivotData`. Данные содержат два кандидата в поля страницы (`Year`, `Region`), один кандидат в поле строки (`Fruit`) и один показатель (`Amount`), что делает полосу полей страницы информативной для изучения.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Все восемь строк заполняются в каждом примере кода в одинаковом порядке, поэтому исходные данные никогда не различаются между сценариями — различаются только свойства макета полей страницы.

## **Пример 1: Сначала по горизонтали, затем по вертикали**

В первом сценарии мы настраиваем два поля страницы (`Year`, `Region`) так, чтобы они отображались **бок о бок в одной строке** в верхней части сводной таблицы. Мы назначаем `Fruit` на ось строк, размещаем `Year` первым, а `Region` вторым на оси страницы (порядок вызовов `AddFieldToArea` определяет начальный индекс), добавляем `Amount` (Sum) как поле данных, а затем устанавливаем `PageFieldOrder` равным `PrintOrderType.OverThenDown` с `PageFieldWrapCount = 2`. При `OverThenDown` и количестве полей в строке равном 2, два поля страницы располагаются горизонтально бок о бок в одной строке в верхней части сводной таблицы, поэтому полоса занимает одну строку шириной в два элемента.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// Заголовки (строка 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Строка 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Строка 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Строка 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Строка 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Строка 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Строка 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Строка 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Строка 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Добавить лист PivotTableReport
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Создать сводную таблицу из диапазона PivotData!A1:D9, размещённую в A1 на листе PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Добавить поля
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Фрукт
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Год
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Регион
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Количество
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Настроить компоновку области полей страниц: размещать поля страниц по горизонтали сначала, переносить после каждых 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Обновить и вычислить
pivotTable.CalculateData();

// Сохранить
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Пример 2: Сначала по вертикали, затем по горизонтали**

В этом примере мы размещаем `Fruit` на оси строк, `Year` и `Region` на оси страницы (первым идёт `Year`), а `Amount` (Sum) как поле данных — точно так же, как в примере 1. Затем мы устанавливаем `PageFieldOrder` равным `PrintOrderType.DownThenOver` и `PageFieldWrapCount` равным `2`. При `DownThenOver` и количестве полей в строке равном 2, два поля страницы располагаются вертикально — `Year` сверху, `Region` непосредственно под ним — образуя один столбец в верхней части сводной таблицы. Таким образом, полоса занимает две строки шириной в один элемент, в отличие от примера 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Пример 3: Перемещение поля страницы**

В третьем сценарии мы сохраняем этот набор данных и распределение полей, устанавливаем нейтральный макет (`OverThenDown` с количеством полей в строке `2`), а затем демонстрируем операцию `PageFields.Move`. Вызов `Move(0, 1)` перемещает поле страницы с индексом 0 (`Year`) на позицию 1, а поле страницы, которое было на позиции 1 (`Region`), сдвигается на позицию 0. После этого вызова `Region` становится первым полем страницы, а `Year` — вторым. Режим переноса и порядка остаётся без изменений, поэтому полоса по-прежнему отображается горизонтально бок о бок — изменён только порядок двух выпадающих элементов.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Связанные статьи**

- [Добавление поля страницы в сводной таблице](/cells/ru/net/add-page-field-in-pivot-table/) — родительская страница, на которой рассказывается, как добавлять поля страницы в сводную таблицу.
- [Поля строк и столбцов в сводной таблице](/cells/ru/net/pivot-table-add-row-and-column-fields/) — охватывает распределение полей по осям строк и столбцов, дополняя работу с осью страницы, показанную здесь.
- [Управление полями значений в сводной таблице](/cells/ru/net/manage-value-fields/) — описывает, как настроить область данных (значений), включая агрегацию `Sum`, используемую в этой статье.
- [Обновление сводной таблицы](/cells/ru/net/refresh-pivot-table/) — объясняет `RefreshData` и `CalculateData`, которые необходимы после изменения порядка полей страницы.
- [Применение стиля к сводной таблице](/cells/ru/net/apply-style-to-pivot-table/) — показывает, как форматировать отображаемую сводную таблицу после размещения полосы полей страницы.

{{< app/cells/assistant language="csharp" >}}