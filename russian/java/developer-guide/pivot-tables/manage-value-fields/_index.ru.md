---
title: Поля значений в Aspose.Cells for Java
linktitle: Поля значений в Aspose.Cells for Java
description: Узнайте, как добавлять базовые поля в область данных сводной таблицы, изменять функцию итогов с помощью PivotField.Function и размещать поле значений на оси строк или столбцов в Aspose.Cells for Java.
keywords: Aspose.Cells, Java, сводная таблица, поле значений, PivotField, PivotField.Function, поле данных, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ru/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Добавление поля в область данных
Добавление базового поля в область данных (значений) — это первый шаг в формировании того, как сводная таблица агрегирует исходные данные. Aspose.Cells предоставляет метод `PivotTable.addFieldToArea(PivotFieldType, String)`, перегрузку, которая принимает константу `PivotFieldType.DATA` и имя столбца источника. После добавления поля в область данных API предоставляет к нему доступ через коллекцию `PivotTable.getDataFields()` в порядке добавления полей. По умолчанию числовой столбец источника обобщается с помощью `ConsolidationFunction.SUM`, а для нечислового столбца по умолчанию используется `COUNT`.
## Изменение функции итогов
Каждое поле, помещённое в область данных, внутренне оборачивается как экземпляр `PivotField`, и его свойство `getFunction()` возвращает значение из перечисления `ConsolidationFunction`. Тот же сеттер `setFunction(...)` позволяет переключаться между доступными агрегатами, включая `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` и `VARP`.
{{% alert color="primary" %}}
Изменение `Function` влияет только на агрегат, исходный столбец не изменяется.
{{% /alert %}}
Таким образом, можно оставить одно поле данных как `SUM`, добавив второе поле данных, ссылающееся на тот же исходный столбец, но использующее `COUNT` или `AVERAGE`, всё в одной сводной таблице.
## Размещение полей значений на оси строк или столбцов
Если сводная таблица содержит два или более полей данных, Aspose.Cells предоставляет дополнительное виртуальное поле `PivotTable.getValuesField()`. Это виртуальное поле представляет агрегат всех полей данных, находящихся в области данных. Его можно перетащить в область строк или столбцов как базовое поле сводной таблицы, что удобно для расположения нескольких мер рядом.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` не работает, если поле значений отсутствует или оно единственное.
{{% /alert %}}
Приведённые ниже сценарии пошагово рассматривают три законченных примера, демонстрирующих каждую из описанных выше возможностей на одной и той же структуре сводной таблицы.
## Сценарий 1 — перетаскивание базового поля в область значений
Этот сценарий показывает, как поместить одно базовое поле (`Amount`) в область данных существующей сводной таблицы. Общая структура сводной таблицы размещает `Category` и `Item` на оси строк, а `Year` — на оси столбцов. После операции `Amount` появляется в области данных и по умолчанию вычисляется как `Sum` поля `Amount`.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Заголовки в A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Строки данных A2:D9 с использованием вложенных циклов с ветвлением по j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
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
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Структура сводной таблицы: Категория и Элемент в строках, Год в столбцах, Сумма как поле данных
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Сценарий 2 — изменение функции итогов
Этот сценарий начинается с той же структуры сводной таблицы, что и в сценарии 1, но добавляет поле `Amount` в область данных дважды. Оба поля данных ссылаются на один и тот же исходный столбец, однако второе поле переопределяется с помощью сеттера `PivotField.setFunction(...)` так, что оно становится `COUNT` вместо `SUM` по умолчанию.
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");

pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField countField = pivotTable.getDataFields().get(1);
countField.setFunction(ConsolidationFunction.COUNT);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```
## Сценарий 3 — размещение полей значений на оси строк или столбцов
Когда в наличии два поля данных, `PivotTable.getValuesField()` становится доступным для использования. Этот сценарий перетаскивает агрегатное виртуальное поле в область столбцов так, чтобы каждая мера из области данных отображалась как отдельный блок столбцов рядом с `Year`.
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```
В совокупности эти три сценария охватывают все аспекты работы с полями значений в Aspose.Cells for Java — от единственного поля данных с `SUM` по умолчанию до сводной таблицы с несколькими мерами, в которой виртуальное поле `ValuesField` управляет расположением на оси строк или столбцов.

{{< app/cells/assistant language="java" >}}
