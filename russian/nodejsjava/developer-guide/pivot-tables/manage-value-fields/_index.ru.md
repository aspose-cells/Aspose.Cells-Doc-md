---
title: Управление полями значений сводной таблицы в Aspose.Cells для .NET
linktitle: Поля значений
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять итоговую функцию с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Сумма, Среднее
type: docs
weight: 230
url: /ru/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Добавление поля в область данных

Добавление базового поля в область данных (значений) — это первый шаг в формировании способа, которым сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет перегрузку `PivotTable.addFieldToArea(PivotFieldType, string)`, которая принимает константу `PivotFieldType.DATA` и имя исходного столбца. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.getDataFields()` в порядке добавления полей. По умолчанию числовой исходный столбец обобщается функцией `ConsolidationFunction.SUM`, а для нечислового столбца по умолчанию используется `COUNT`.

## Изменение итоговой функции

Каждое поле, размещённое в области данных, внутри оборачивается в экземпляр `PivotField`, и его свойство `getFunction()` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `setFunction()` позволяет переключаться между доступными агрегатами, включая `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` и `VARP`.

{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, исходный столбец при этом не меняется.
{{% /alert %}}

Таким образом, можно оставить одно поле данных как `SUM`, одновременно добавив второе поле данных, которое ссылается на тот же исходный столбец, но использует `COUNT` или `AVERAGE`, — всё в одной сводной таблице.

## Размещение полей значений на оси строк или столбцов

Когда сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле, называемое `PivotTable.getValuesField()`. Это виртуальное поле представляет агрегат каждого поля данных, находящегося в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что удобно для расположения нескольких мер бок о бок.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` не работает, если полей значений нет или существует только одно поле значений.
{{% /alert %}}

Приведённые ниже сценарии последовательно рассматривают три законченных примера, демонстрирующих каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.

## Сценарий 1 — перетаскивание базового поля в область значений

Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После выполнения операции `Amount` появляется в области данных и по умолчанию вычисляется как `Sum` поля `Amount`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Заголовки в A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Строки данных A2:D9 с использованием вложенных циклов с ветвлением по j
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

// Добавить сводную таблицу в F3 с именем PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Структура сводной таблицы: Категория и Элемент в строках, Год в столбцах, Сумма как поле данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Сценарий 2 — изменение итоговой функции

Этот сценарий начинается с той же структуры сводной таблицы, что и в сценарии 1, но добавляет поле `Amount` в область данных дважды. Оба поля данных ссылаются на один и тот же исходный столбец, однако для второго поля с помощью сеттера `PivotField.setFunction()` переопределяется итоговая функция, так что оно становится `COUNT` вместо `SUM` по умолчанию.

## Сценарий 3 — размещение полей значений на оси строк или столбцов

При наличии двух полей данных `PivotTable.getValuesField()` становится доступным для использования. Этот сценарий перетаскивает данное агрегатное виртуальное поле в область столбцов так, чтобы каждая мера в области данных отображалась как отдельный блок столбцов рядом с `Year`.

Все три сценария в совокупности охватывают все аспекты работы с полями значений в Aspose.Cells for Node.js via Java — от единственного поля данных с функцией `SUM` по умолчанию до сводной таблицы с несколькими мерами, в которой виртуальное поле `ValuesField` управляет расположением по оси строк или столбцов.

{{< app/cells/assistant language="nodejs-java" >}}
