---
title: Вставка сводной таблицы
linktitle: Вставка сводной таблицы
description: Создавайте и форматируйте сводные таблицы для файлов электронных таблиц Excel с помощью Aspose.Cells for Node.js via Java.
keywords: Создание сводной таблицы, Вставка сводной таблицы, Форматирование сводной таблицы, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /ru/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Что такое сводная таблица?**
Сводная таблица — это интерактивный сводный отчёт, который преобразует большой массив необработанных данных, представленных в виде строк, в компактную матрицу без единой формулы. Вы выбираете, какие столбцы станут метками строк, какие — метками столбцов, а какие будут агрегироваться как значения; сводная таблица выполняет группировку и вычисления:
- **Обобщение** — итоговые объёмы продаж по продуктам, регионам или кварталам вместо длинных цепочек формул.
- **Сравнение** — категории в строках и периоды в столбцах превращают плоский список в перекрёстный отчёт, в котором тенденции видны наглядно.
- **Детализация** — дважды щёлкните по любому итоговому значению, чтобы просмотреть соответствующие исходные строки.
- **Обновление** — если исходные данные изменились, одно обновление пересчитывает весь отчёт.
Типичные сценарии — дашборды продаж, разбиение расходов и анализ запасов, а также любые вопросы вида «как разбиваются эти числа по категориям и времени?». Aspose.Cells for Node.js via Java программно создаёт аналогичные сводные таблицы, поэтому рабочие книги, создаваемые вашим приложением, могут содержать готовые отчёты, а не только необработанные данные.

### **Модель объектов сводной таблицы**
Aspose.Cells предоставляет набор классов, используемых для создания сводных таблиц и управления ими. Основные элементы:
- `PivotField` представляет поле в `PivotTable`.
- `PivotFieldCollection` представляет коллекцию всех объектов `PivotField` в `PivotTable`.
- `PivotTable` представляет сводную таблицу на рабочем листе.
- `PivotTableCollection` представляет коллекцию всех объектов `PivotTable` на рабочем листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
Создание сводной таблицы выполняется в три этапа: запись исходных данных в ячейки рабочего листа, добавление сводной таблицы в указанное место и размещение полей сводной таблицы в областях строк, столбцов и данных.
1. Добавьте данные в рабочий лист с помощью метода `putValue` ячейки. Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу в рабочий лист с помощью метода `add` коллекции `PivotTables`: `add(sourceData, row, column)`. `sourceData` — исходный диапазон (например, "A1:C8"); `row` и `column` — координаты целевой ячейки в левом верхнем углу сводной таблицы (нумерация начинается с нуля; ячейка E3 соответствует строке 2 и столбцу 4). Метод непосредственно возвращает новый объект `PivotTable`.
3. Разместите поля сводной таблицы с помощью метода `addFieldToArea` объекта `PivotTable`: имя поля передаётся в область строк (`PivotFieldType.ROW`), в область столбцов (`PivotFieldType.COLUMN`) или в область данных (`PivotFieldType.DATA`).
4. Сохраните рабочую книгу — сводная таблица будет записана в сохранённый файл.
После выполнения примера кода в рабочий лист добавляется сводная таблица.

```javascript
const AsposeCells = require("aspose.cells");

// Создайте новую книгу и получите первый рабочий лист
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Запишите исходные данные: продажи по видам спорта и кварталам
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

// Добавьте сводную таблицу в ячейку назначения E3 с источником данных A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Назначьте поля сводной таблицы: Sport для строк, Quarter для столбцов, Sales для данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Сохраните книгу
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен располагаться от верхней левой ячейки до нижней правой. Например, "A1:C3" допустим, а "C3:A1" — нет.
{{% /alert %}}

## Связанные статьи
- [Добавление полей фильтрации в сводную таблицу с помощью Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/add-page-field-in-pivot-table/)
- [Применение стилей к сводным таблицам с помощью Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Изменение макета поля страницы в сводной таблице](/cells/ru/nodejs-java/change-page-field-layout/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Управление полями значений сводной таблицы с помощью Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}