---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматировать часть сводной таблицы в Aspose.Cells for Node.js via C++ посредством применения стилей к семантическим регионам PivotArea или прямоугольникам CellArea через PivotTable.format, при этом форматы сохраняются в PivotTable.getPivotFormats() и сохраняются при обновлении сводной таблицы.
keywords: Aspose.Cells, Node.js via C++, сводная таблица, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /ru/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.formatAll` применяет один стиль ко всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные регионы отчёта.  
На практике обычно необходимо выделить лишь часть сводной таблицы. Типичные цели включают метки, принадлежащие одному полю строк, ячейки‑значения, созданные одним полем, строку итогов или произвольный прямоугольник, например первые две строки элементов.  
Прямое применение стиля к ячейкам рабочего листа, содержащим сводную таблицу, не эквивалентно. Excel хранит форматирование сводных таблиц как семантические регионы `PivotArea`, а не как обычные записи стилей ячеек. Формат, привязанный к области `PivotArea`, остаётся связанным с регионом, таким как метки поля или данные, и переопределяется при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный непосредственно в ячейку, принадлежит только этой позиции и не отслеживается моделью сводной таблицы.  
`Aspose.Cells` предоставляет полную семью перегрузок `PivotTable.format`, чтобы поддержать оба типа форматирования:
- `format(PivotArea, Style)` привязывает стиль к семантическому региону, построенному с помощью `PivotArea.select` или `PivotArea.selectField`.
- `format(CellArea, Style)` привязывает стиль к прямоугольнику рабочего листа внутри сводной таблицы.
- `format(number row, number column, Style)` нацеливает одну ячейку.
- `formatAll(Style)` формирует всю сводную таблицу.

## **Форматировать область PivotArea**
Рабочий процесс с семантической областью рекомендуется, когда выделение должно следовать за полем или регионом отчёта.
1. Создайте `PivotArea` с `new PivotArea(pivotTable)`. Объект описывает семантический регион, принадлежащий данной сводной таблице.
2. Выберите поле по его нулевому индексу на заданной оси с помощью `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` выбирает как метки, так и данные поля.
   - `PivotTableSelectionType.LabelOnly` выбирает только метки поля.
   - `PivotTableSelectionType.DataOnly` выбирает только ячейки‑данные поля.
3. Выберите поле по имени с помощью `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. При выборе поля строк по имени регион разрешается к ячейкам‑значениям, созданным элементами этого поля.
4. Создайте `Style` через `workbook.createStyle()`, настройте шрифт, цвет переднего плана и сплошной фоновый узор, затем передайте стиль в `pivotTable.format(area, style)`.
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `pivotTable.getPivotFormats()`.
6. Форматы, привязанные к полям, применяются при расчёте данных сводной таблицы. Поэтому после применения форматов вызовите `pivotTable.calculateData()`, чтобы стили стали видимыми.  
Следующий пример создаёт небольшую сводную таблицу продаж фруктов, задаёт стиль меткам строк `Fruit` через `PivotArea.select` и `PivotTableSelectionType.LabelOnly`, задаёт стиль ячейкам‑значениям того же поля через `PivotArea.selectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля были отрисованы.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Форматировать область CellArea сводной таблицы**
Используйте `PivotTable.format(CellArea, Style)`, когда интересующий регион представляет собой обычный прямоугольник рабочего листа, а не семантическую область сводной таблицы.  
`CellArea` описывается свойствами `startRow`, `startColumn`, `endRow` и `endColumn`. Значения — нулевые координаты листа, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область охватывает ячейки от начального до конечного положения включительно.  
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Повторный вызов `pivotTable.calculateData()` не требуется для отображения стиля.  
Прямоугольник `CellArea` может одновременно содержать метки и значения. Следующий раздел описывает, как `Aspose.Cells` и Excel представляют такой прямоугольник внутри.  
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы курсивным светло‑синим стилем и сохраняет рабочую книгу без дополнительного пересчёта.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Как сопоставляются PivotArea и CellArea**
Excel хранит форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек листа. Та же модель используется `Aspose.Cells`, поэтому запрос форматирования преобразуется в области pivot при записи.  
Взаимосвязь между пользовательским `CellArea` и внутренними областями pivot многократна в обеих направлениях.
- Один `CellArea` может породить несколько областей pivot. Если прямоугольник охватывает и метки, и данные, он разбивается на отдельные правила для меток и данных, поскольку модель pivot обрабатывает форматирование меток и данных независимо.
- Одна область pivot может разрешаться в несколько разрозненных экземпляров `CellArea`. Семантический регион, например строка итогов или поле с несмежными элементами, может покрывать несколько прямоугольников. Поэтому `PivotArea.getCellAreas()` возвращает коллекцию, а не один прямоугольник.
Каждая операция форматирования через `pivotTable.format()` фиксируется в `pivotTable.getPivotFormats()`. Каждая запись `PivotTableFormat` раскрывает соответствующий `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за каждый вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей.  
Чтобы различать сохранённые регионы, каждый `PivotArea` предоставляет флаги `getOnlyLabel()` и `getOnlyData()`. Пример ниже форматирует один прямоугольник, охватывающий и метки, и значения, исследует `pivotTable.getPivotFormats()` и выводит координаты `CellArea`, к которым разрешается каждый сохранённый регион pivot.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
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
Поскольку форматы сохраняются как области pivot, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется с помощью `pivotTable.refreshData()`, пересчитывается с помощью `pivotTable.calculateData()` или сохраняется и заново загружается, каждый сохранённый регион pivot переопределяется к текущему положению своей области, и стиль применяется вновь.
{{% /alert %}}

Используйте `PivotArea`, построенный через `select` или `selectField`, когда выделение должно оставаться привязанным к полю или семантическому региону при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник в текущем макете сводной таблицы. Перегрузка `format(number row, number column, Style)` нацелена на отдельную ячейку. Применяйте `formatAll`, описанный на родительской странице, когда необходимо переоформить всю сводную таблицу сразу.

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)
- [Добавление полей строк и столбцов сводной таблицы](/cells/ru/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Управление полями значений в сводной таблице](/cells/ru/nodejs-cpp/manage-value-fields/)
- [Обновление сводной таблицы](/cells/ru/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}