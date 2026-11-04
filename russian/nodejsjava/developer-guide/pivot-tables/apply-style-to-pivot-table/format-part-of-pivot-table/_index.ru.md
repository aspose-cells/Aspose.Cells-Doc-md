---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматирование части сводной таблицы в Aspose.Cells for Node.js via Java путем применения стилей к семантическим областям PivotArea или прямоугольникам CellArea через PivotTable.format, при этом форматы сохраняются в PivotTable.getPivotFormats() и сохраняются при обновлении сводной таблицы.
keywords: Aspose.Cells for Node.js via Java, сводная таблица, формат, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /ru/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.formatAll` применяет один стиль ко всей сводной таблице и рассматривается на основной странице. Он не различает метки, значения, итоговые строки или отдельные области отчёта.  
На практике обычно требуется выделить только часть сводной таблицы. Частыми целями являются метки, принадлежащие одному полю строки, ячейки‑данные, созданные одним полем, строка общей суммы или произвольный прямоугольник, например первые две строки элементов.  
Применение стиля непосредственно к ячейкам рабочего листа сводной таблицы не эквивалентно. Excel сохраняет форматирование сводных таблиц в виде семантических областей `PivotArea`, а не обычных записей стилей ячеек. Формат, привязанный к области `PivotArea`, остаётся связанным с такой областью, как метки поля или данные, и переопределяется при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный непосредственно в ячейку, принадлежит только этой позиции ячейки и не отслеживается моделью сводной таблицы.  
Aspose.Cells предоставляет полный набор перегрузок `PivotTable.format`, чтобы обеспечить оба типа форматирования:
- `format(PivotArea, Style)` привязывает стиль к семантической области, создаваемой через `PivotArea.select` или `PivotArea.selectField`.
- `format(CellArea, Style)` привязывает стиль к прямоугольнику рабочего листа внутри сводной таблицы.
- `format(int row, int column, Style)` ориентирован на одну ячейку.
- `formatAll(Style)` форматирует всю сводную таблицу.

## **Форматировать область PivotArea**
Семантический подход рекомендуется, когда выделение должно следовать за полем или областью отчёта.
1. Создайте объект `PivotArea` с помощью `new PivotArea(pivotTable)`. Этот объект описывает семантическую область, принадлежащую конкретной сводной таблице.  
1. Выберите поле по его нулевой позиции на заданной оси с помощью `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DATA_AND_LABEL` выбирает как метки, так и данные поля.  
   - `PivotTableSelectionType.LABEL_ONLY` выбирает только метки поля.  
   - `PivotTableSelectionType.DATA_ONLY` выбирает только ячейки‑данные поля.  
1. Выберите поле по имени с помощью `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. При выборе строкового поля по имени область раскрывается в ячейки‑данные, созданные элементами этого поля.  
1. Создайте объект `Style` через `Workbook.createStyle()`, настройте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.format(area, style)`.  
1. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.getPivotFormats()`.  
1. Форматы, привязанные к полям, отрисовываются при вычислении данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.calculateData()`, чтобы стили стали видимыми.  
Следующий пример создаёт небольшую сводную таблицу продаж фруктов, стилизует метки строк `Fruit` с помощью `PivotArea.select` и `PivotTableSelectionType.LABEL_ONLY`, стилизует ячейки‑данные, полученные тем же полем строки, через `PivotArea.selectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Форматировать область CellArea сводной таблицы**
Используйте `PivotTable.format(CellArea, Style)`, когда интересующая область представляет собой простой прямоугольник рабочего листа, а не семантическую область сводной таблицы.  
`CellArea` описывается публичными полями `StartRow`, `StartColumn`, `EndRow` и `EndColumn`. Значения являются нулевыми координатами листа, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область охватывает ячейки от начальной позиции до конечной включительно.  
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `calculateData()` не требуется для отображения стиля.  
Прямоугольник `CellArea` может одновременно содержать метки и значения. В следующем разделе объясняется, как Aspose.Cells и Excel представляют такой прямоугольник внутренне.  
Пример ниже форматирует прямоугольник `E4:F5` сводной таблицы курсивом светло‑голубого цвета и сохраняет рабочую книгу без дополнительного пересчёта.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Как сопоставляются PivotArea и CellArea**
Excel сохраняет форматирование сводных таблиц в виде записей `pivotArea`, а не обычных записей стилей ячеек листа. Такая же модель используется в Aspose.Cells, поэтому запрос на форматирование преобразуется во внутренние области pivot при сохранении.  
Отношения между `CellArea`, указанным пользователем, и внутренними областями pivot являются многие‑ко‑многим в обоих направлениях.  
- Один `CellArea` может породить несколько областей pivot. Если прямоугольник охватывает как метки, так и значения, он разлагается на отдельные правила для меток и данных, поскольку модель pivot рассматривает их независимо.  
- Одна область pivot может преобразоваться в несколько разрозненных экземпляров `CellArea`. Семантическая область, например строка общей суммы или поле, элементы которого не идут подряд, может покрывать несколько прямоугольников. Поэтому `PivotArea.getCellAreas()` возвращает коллекцию, а не один прямоугольник.  
Каждая операция форматирования, выполненная через `PivotTable.format`, записывается в `PivotTable.getPivotFormats()`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические области, может добавить несколько записей.  
Для различения сохранённых областей каждый `PivotArea` предоставляет флаги `getOnlyLabel()` и `getOnlyData()`. Пример ниже форматирует один прямоугольник, охватывающий как метки, так и значения, проверяет `PivotTable.getPivotFormats()` и выводит координаты `CellArea`, к которым каждая сохранённая область pivot соответствует.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
        );
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
Поскольку форматы хранятся как области pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется методом `PivotTable.refreshData()`, пересчитывается с помощью `calculateData()` или сохраняется и загружается заново, каждая сохранённая область pivot перепривязывается к текущей позиции своей области, и стиль применяется повторно.
{{% /alert %}}

Используйте `PivotArea`, построенный с помощью `select` или `selectField`, когда выделение должно оставаться привязанным к полю или семантической области при обновлениях, и используйте `CellArea`, когда достаточно форматировать фиксированный прямоугольник в текущем макете сводной таблицы. Перегрузка `format(int row, int column, Style)` работает с отдельной ячейкой. Применяйте `formatAll`, описанный на родительской странице, когда нужно переоформить всю сводную таблицу единовременно.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов в сводную таблицу](/cells/ru/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-java/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}