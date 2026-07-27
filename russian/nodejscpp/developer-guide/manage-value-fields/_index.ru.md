---
title: Поля значений в Aspose.Cells for Node.js via C++
linktitle: Поля значений в Aspose.Cells for Node.js via C++
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять итоговую функцию с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ru/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Поля значений являются основой каждой сводной таблицы — это числовые агрегаты, которые обобщают исходные данные. В Aspose.Cells for Node.js via C++ область данных сводной таблицы заполняется путём добавления в неё базовых полей через `PivotTable.addFieldToArea`, и каждое поле, помещённое в эту область, может иметь собственную итоговую функцию. Когда существуют два или более полей данных, Aspose.Cells предоставляет специальное агрегатное поле `PivotTable.ValuesField`, которое может быть размещено на оси строк или столбцов в качестве базового поля, что даёт более точный контроль над тем, как поля значений отображаются в макете.

## Добавление поля в область данных

Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет метод `PivotTable.addFieldToArea(PivotFieldType, string)`, перегрузку, которая принимает константу `PivotFieldType.Data` и имя столбца-источника. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.DataFields` в порядке добавления полей. По умолчанию числовой столбец-источник обобщается функцией `ConsolidationFunction.Sum`, а для нечислового столбца по умолчанию используется `Count`.

## Изменение итоговой функции

Каждое поле, помещённое в область данных, внутренне оборачивается в экземпляр `PivotField`, и его свойство `Function` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `Function` позволяет переключаться между доступными агрегатами, включая `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` и `Varp`.

{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, столбец-источник не изменяется.
{{% /alert %}}

Таким образом, можно оставить одно поле данных как `Sum`, добавив второе поле данных, которое ссылается на тот же столбец-источник, но использует `Count` или `Average`, всё в одной сводной таблице.

## Размещение полей значений на оси строк или столбцов

Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле под названием `PivotTable.ValuesField`. Это виртуальное поле представляет агрегат каждого поля данных, находящегося в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что полезно для расположения нескольких мер рядом.

{{% alert color="primary" %}}
`PivotTable.ValuesField` не работает, если полей значений нет или существует только одно такое поле.
{{% /alert %}}

Приведённые ниже сценарии демонстрируют три законченных примера, которые показывают каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.

## Сценарий 1 — Перетаскивание базового поля в область значений

Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После операции `Amount` появляется в области данных и по умолчанию вычисляется как `Sum` поля `Amount`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Заголовки в A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Строки данных A2:D9 с использованием вложенных циклов с разветвлением по j
for (let i = 1; i <= 8; i++) {
  for (let j = 0; j < 4; j++) {
    switch (j) {
      case 0:
        worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
        break;
      case 1:
        if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
        else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
        else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
        else worksheet.getCells().get(i, j).putValue("Daikon");
        break;
      case 2:
        worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
        break;
      case 3:
        if (i == 1) worksheet.getCells().get(i, j).putValue(100);
        else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
        else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
        else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
        else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
        else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
        else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
        else worksheet.getCells().get(i, j).putValue(45);
        break;
    }
  }
}

// Добавление сводной таблицы в F3 с именем PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Макет сводной таблицы: Category и Item по строкам, Year по столбцам, Amount как поле данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Сценарий 2 — Изменение итоговой функции

Этот сценарий начинается с той же структуры сводной таблицы, что и Сценарий 1, но добавляет поле `Amount` в область данных дважды. Оба поля данных ссылаются на один и тот же столбец-источник, однако второе поле переопределяется с помощью сеттера `PivotField.Function`, так что оно становится `Count` вместо значения по умолчанию `Sum`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Сценарий 3 — Размещение полей значений на оси строк или столбцов

При наличии двух полей данных `PivotTable.ValuesField` становится доступным для использования. Этот сценарий перетаскивает данное агрегатное виртуальное поле в область столбцов так, что каждая мера в области данных отображается как отдельный блок столбцов рядом с `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

В совокупности эти три сценария охватывают все аспекты работы с полями значений в Aspose.Cells for Node.js via C++ — от единственного поля данных со значением по умолчанию `Sum` до сводной таблицы с несколькими мерами, в которой виртуальное поле `ValuesField` управляет расположением на оси строк или столбцов.

## Связанные статьи

- [Поля строк и столбцов сводной таблицы в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/row-and-column-fields/)
- [Поля страниц в сводных таблицах](/cells/ru/nodejs-cpp/add-page-field-in-pivot-table/)
- [Обновление сводных таблиц в Aspose.Cells for Node.js via C++](/cells/ru/nodejs-cpp/refresh-pivot-table/)
- [Применение стилей к сводным таблицам](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}