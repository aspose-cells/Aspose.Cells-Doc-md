---
title: Форматирование части сводной таблицы
description: Форматирование части сводной таблицы в Aspose.Cells for Java путем применения стилей к семантическим областям PivotArea или прямоугольникам CellArea через PivotTable.format, форматы сохраняются в PivotTable.getPivotFormats и сохраняются при обновлении сводной таблицы.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, сводная таблица, формат, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /ru/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.formatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные области отчёта.
На практике обычно требуется выделить лишь часть сводной таблицы. Частыми целями являются метки, принадлежащие одному полю строки, ячейки со значениями, полученные от одного поля, строка общей суммы, или произвольный прямоугольник, например первые две строки элементов.
Применение стиля непосредственно к ячейкам листа сводной таблицы не эквивалентно. Excel сохраняет форматирование сводных таблиц как семантические области `PivotArea`, а не как обычные записи стилей ячеек. Формат области PivotArea привязан к региону, например к меткам поля или значениям данных, и переопределяется при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный напрямую в ячейку, относится к конкретному положению ячейки и не отслеживается моделью сводной таблицы.
Aspose.Cells предоставляет полный набор перегрузок `PivotTable.format`, позволяя использовать оба типа форматирования:
- `format(PivotArea, Style)` привязывает стиль к семантической области, построенной с помощью `PivotArea.select` или `PivotArea.selectField`.
- `format(CellArea, Style)` привязывает стиль к прямоугольнику листа внутри сводной таблицы.
- `format(int row, int column, Style)` нацеливается на одну ячейку.
- `formatAll(Style)` форматирует всю сводную таблицу.

## **Форматировать область PivotArea**
Рабочий процесс с семантической областью рекомендуется, когда выделение должно следовать за полем или областью отчёта.
1. Создайте `PivotArea` с помощью `new PivotArea(pivotTable)`. Объект описывает семантическую область, принадлежащую этой конкретной сводной таблице.
2. Выберите поле по его нулевой позиции на заданной оси с помощью `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` выбирает как метки, так и данные поля.
   - `PivotTableSelectionType.LABEL_ONLY` выбирает только метки поля.
   - `PivotTableSelectionType.DATA_ONLY` выбирает только ячейки данных поля.
3. Выберите поле по имени с помощью `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Когда поле строки выбирается по имени, область разрешается в ячейки значений, полученные от элементов этого поля.
4. Создайте `Style` через `Workbook.createStyle()`, настройте его шрифт, цвет переднего плана и сплошной фоновый узор, затем передайте стиль в `PivotTable.format(area, style)`.
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.getPivotFormats()`.
6. Форматы, связанные с полем, применяются при расчёте данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.calculateData()`, чтобы стили стали видимыми.
Следующий пример создаёт небольшую сводную таблицу продаж фруктов, стилизует метки строк `Fruit` с помощью `PivotArea.select` и `PivotTableSelectionType.LABEL_ONLY`, стилизует ячейки значений, полученные тем же полем строки, с помощью `PivotArea.selectField`, затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Форматировать область CellArea в сводной таблице**
Используйте `PivotTable.format(CellArea, Style)`, когда интересующая область представляет собой обычный прямоугольник листа, а не семантическую область сводной таблицы.
`CellArea` описывается свойствами `getStartRow()`, `getStartColumn()`, `getEndRow()` и `getEndColumn()`. Значения — координаты листа с нулевой основы, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область покрывает ячейки от начальной позиции до конечной включительно.
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `calculateData()` не требуется для отображения стиля.
Прямоугольник `CellArea` может одновременно содержать ячейки меток и ячейки значений. В следующем разделе описывается, как Aspose.Cells и Excel представляют этот прямоугольник внутри.
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы с помощью курсивного светло‑голубого стиля и сохраняет рабочую книгу без дополнительного пересчёта.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Как сопоставляются PivotArea и CellArea**
Excel сохраняет форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Та же модель используется в Aspose.Cells, поэтому запрос на форматирование преобразуется в области pivot при записи.
Взаимосвязь между `CellArea`, предоставляемой пользователем, и внутренними областями pivot является многими‑ко‑многим в обеих направлениях.
- Один `CellArea` может порождать несколько областей pivot. Если прямоугольник охватывает как ячейки меток, так и ячейки значений, он разбивается на отдельные правила для меток и данных, поскольку модель pivot обрабатывает форматирование меток и данных независимо.
- Одна область pivot может разрешаться в несколько раздельных экземпляров `CellArea`. Семантическая область, например строка общей суммы, или поле, чьи элементы не соприкасаются, может охватывать несколько прямоугольников. Поэтому `PivotArea.getCellAreas()` возвращает коллекцию, а не один прямоугольник.
Каждая операция форматирования, выполненная через `PivotTable.format`, фиксируется в `PivotTable.getPivotFormats()`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий различные семантические регионы, может добавить несколько записей.
Чтобы различать сохранённые регионы, каждый `PivotArea` предоставляет флаги `getOnlyLabel()` и `getOnlyData()`. Пример ниже форматирует один прямоугольник, охватывающий и метки, и значения, проверяет `PivotTable.getPivotFormats()` и выводит координаты `CellArea`, к которым разрешается каждая сохранённая область pivot.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Поскольку форматы хранятся как области pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.refreshData`, пересчитывается через `calculateData` или сохраняется и загружается заново, каждая сохранённая область pivot переопределяется к текущему положению своей области, и её стиль повторно применяется.
{{% /alert %}}

Используйте `PivotArea`, построенный с помощью `select` или `selectField`, когда выделение должно оставаться привязанным к полю или семантической области при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник в текущем макете сводной таблицы. Перегрузка `format(int row, int column, Style)` для одной ячейки нацелена на отдельную ячейку. Используйте `formatAll`, описанный на родительской странице, когда необходимо одновременно изменить стиль всей сводной таблицы.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/java/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}