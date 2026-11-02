---
title: Отображение или фильтрация Топ-10 в сводной таблице
linktitle: Отображение или фильтрация Топ-10 в сводной таблице
description: Узнайте, как отображать только элементы с наиболее высоким или наиболее низким рейтингом в поле сводной таблицы с помощью Aspose.Cells for Java. В этой статье рассматриваются метод Top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings и фильтр Топ-10 для Excel 2007-365 с помощью FilterTop10.
keywords: Aspose.Cells, Java, сводная таблица, топ-10, автопоказ, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ru/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, перечисляющая все элементы поля строки, может быть сложной для восприятия, если поле содержит десятки элементов. Отчет «Топ-10» оставляет только элементы с наиболее высоким или наиболее низким рейтингом, что необходимо для отчетов с ранжированием, например «5 продуктов с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Автопоказ Excel 97-2003** — метод `PivotField.top10AutoShow()`. Это классическая настройка «Показывать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она поддерживается всеми версиями Excel, как старыми, так и новыми, поскольку входит в исходный формат сводной таблицы.
- **Фильтр Топ-10 Excel 2007-365** — метод `PivotField.filterTop10()`. Это современный фильтр значений «Топ-10», доступный в разделе «Фильтры значений» меню поля. Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование по количеству элементов и по проценту.

## **Отображение Топ-10 в Excel 97-2003 (top10AutoShow)**
Классический автопоказ настраивается одним вызовом `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — включает или отключает автопоказ для поля.
- `isTop` — значение `true` сохраняет элементы с наиболее высоким рейтингом («Верхние»), а `false` — с наиболее низким («Нижние»).
- `count` — количество сохраняемых элементов, например 10 для классического отчета «Топ-10».
- `rankBy` — нулевой индекс **поля данных**, значения которого используются для ранжирования элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю данных или по самому полю. Ниже показаны два варианта.

### **Ранжирование по полю данных**
Элементы поля строки можно ранжировать по обычному полю данных, например «Сумма продаж». В следующем примере создается сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объемом продаж. Значение `rankBy` равно 0, поскольку «Сумма продаж» является полем данных с индексом 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Показать 2 лучших элемента, отсортированных по «Сумма продаж» (индекс поля данных 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Ранжирование по самому полю**
Для ранжирования по самому полю передайте -1 в `rankBy`. Для этого варианта дополнительное поле данных не требуется; достаточно поместить поле в область строк или столбцов. В следующем примере показаны 3 вида спорта, занимающие нижние позиции рейтинга. При сохранении этих настроек атрибут `rankBy` исключается из XML сводной таблицы, поскольку -1 является значением по умолчанию для данного формата, а `Top10AutoShowSettings.getRankBy()` считывает значение -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Чтение текущих параметров (Top10AutoShowSettings)**
Метод `PivotField.getTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий текущие параметры автопоказа, сохраненные в поле. Используйте его, чтобы проверить, как будут отображены элементы существующей рабочей книги или только что настроенной сводной таблицы, в том числе при загрузке рабочих книг из файла.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Четыре свойства этого объекта соответствуют классическим атрибутам автопоказа, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому при чтении возвращаются именно те значения, которые учитываются всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- Прямые свойства `PivotField`, доступные через `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` и `getAutoShowField()`, помечены как устаревшие. Вместо них используйте объект `Top10AutoShowSettings`: `Top10AutoShowSettings.isAutoShow()` заменяет `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` заменяет `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` заменяет `PivotField.getAutoShowCount()`, а `Top10AutoShowSettings.getRankBy()` заменяет `PivotField.getAutoShowField()`. Метод `PivotField.top10AutoShow()` является поддерживаемым способом изменения этих параметров.
- `top10AutoShow` работает с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не размещены в теле сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр Топ-10 (filterTop10)**
Современные версии Excel предоставляют «Топ-10» как фильтр значений в меню поля («Фильтры значений», «Топ-10...»). В Aspose.Cells этот фильтр реализован методом `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, возвращающим созданный объект `PivotFilter`:
- `valueFieldIndex` — нулевой индекс поля данных, агрегированные значения которого определяют рейтинг элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.COUNT` сохраняет фиксированное количество элементов (элемент «Элементы» в диалоговом окне). `PivotFilterType.PERCENT` сохраняет заданный процент элементов, поэтому `itemCount` является самим процентом — значение 30 сохраняет верхние 30 процентов. `PivotFilterType.SUM` ранжирует элементы по накопленному объему значений.
- `isTop` — значение `true` для верхних элементов, `false` для нижних.
- `itemCount` — число N в выражении «Топ-N»; его единица измерения зависит от `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Фильтр Top 10 — сохранить 2 верхних элемента по «Sum of Sales» (индекс поля данных 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Для фильтра на основе процентов вместо этого сохранить верхние 30 процентов элементов:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` и `filterTop10` — две отдельные возможности. Механизм автопоказа записывает классический атрибут `autoShow`, заданный для поля сводной таблицы, и поддерживается всеми версиями Excel, начиная с Excel 97. `filterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица с современным фильтром начинает отображать все элементы. Для документов, которые необходимо открывать и сохранять с помощью устаревших инструментов, предпочтительнее `top10AutoShow`; для современных рабочих книг предпочтительнее `filterTop10`, поскольку его можно использовать вместе с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/java/filter-by-label-or-value-of-pivot-table/)
- [Добавление полей строки и столбца в сводную таблицу](/cells/ru/java/pivot-table-add-row-and-column-fields/)
- [Группировка полей сводной таблицы](/cells/ru/java/group-pivot-fields-in-the-pivot-table/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)
- [Добавление поля страницы в сводную таблицу](/cells/ru/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}