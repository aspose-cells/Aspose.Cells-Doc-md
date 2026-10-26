---
title: Вставка сводной таблицы
linktitle: Вставка сводной таблицы
description: Создание и форматирование сводных таблиц с помощью Aspose.Cells for Node.js через C++.
keywords: Создание сводной таблицы, вставка сводной таблицы, форматирование сводной таблицы.
type: docs
weight: 160
url: /ru/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный сводный отчет: она преобразует большой массив необработанных данных, представленных построчно, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут использоваться как агрегируемые значения: сводная таблица выполняет группировку и расчеты:
- **Обобщение** — суммарные продажи по каждому продукту, региону или кварталу вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрестный отчет, в котором тенденции видны с первого взгляда.
- **Детализация** — дважды щелкните по любому итоговому значению, чтобы просмотреть исходные строки, из которых оно получено.
- **Обновление** — при изменении исходных данных достаточно одного обновления, чтобы пересчитать весь отчет.
Типичные сценарии — панели продаж, детализация расходов и анализ запасов, то есть любые запросы вида «как эти числа распределяются по категориям и временным периодам?». Aspose.Cells for Node.js через C++ позволяет программно создавать такие же сводные таблицы, поэтому рабочие книги, создаваемые вашим приложением, могут содержать готовые отчеты, а не только необработанные данные.

### **Объектная модель сводной таблицы**
Aspose.Cells for Node.js через C++ предоставляет специальный набор классов, предназначенных для создания сводных таблиц и управления ими. Эти классы используются для создания и настройки объектов [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), являющихся строительными блоками сводной таблицы. Объекты модели:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) представляет поле сводной таблицы [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) представляет коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield), содержащихся в [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) представляет объект `PivotTable` на рабочем листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) представляет коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) на рабочем листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
Создание сводной таблицы выполняется в три шага: запись исходных данных в ячейки рабочего листа, добавление сводной таблицы в позицию назначения и размещение полей сводной таблицы в областях строк, столбцов и данных.
1. Добавьте данные в рабочий лист с помощью метода [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) объекта [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу в рабочий лист, вызвав метод [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) коллекции [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection): `add(sourceData, row, column)`. `sourceData` — исходный диапазон (например, «A1:C8»); `row` и `column` — нулевые индексы строки и столбца ячейки назначения, расположенной в левом верхнем углу сводной таблицы (ячейка E3 означает строку 2 и столбец 4). Метод напрямую возвращает новый объект [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
3. Разместите поля сводной таблицы с помощью метода `addFieldToArea` объекта [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): имя поля добавляется в область строк (`PivotFieldType.Row`), в область столбцов (`PivotFieldType.Column`) или в область данных (`PivotFieldType.Data`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохраненный файл.
После выполнения кода примера в рабочий лист добавляется сводная таблица.

```javascript
const AsposeCells = require("aspose.cells.node");

// Создать новую книгу и получить первый лист
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Записать исходные данные: продажи по видам спорта и кварталам
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Добавить сводную таблицу в ячейку назначения E3 на основе диапазона A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Назначить поля сводной таблицы: Sport — строки, Quarter — столбцы, Sales — данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Сохранить книгу
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных его начальная ячейка должна находиться в левом верхнем углу, а конечная — в правом нижнем. Например, «A1:C3» — допустимый диапазон, а «C3:A1» — недопустимый.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}