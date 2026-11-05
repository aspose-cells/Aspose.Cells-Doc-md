---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавьте условное форматирование к сводной таблице в Aspose.Cells for Node.js via Java — привяжите правило к области данных с помощью applyTo и области PivotConditionFormatScopeType, или определите цель с помощью addCellArea и getPivotAreas, затем присоедините правила и стили через getFormatConditions().addCondition.
keywords: Aspose.Cells, сводная таблица, условное форматирование, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /ru/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это управляемый правилами аналог: выделять каждое значение выше 200, затенять средние пятьдесят процентов или помечать элементы с наименьшим рейтингом — и выделение будет следовать за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells for Node.js via Java условное форматирование сводных таблиц находится в коллекции `pivotTable.getConditionalFormats()`. Каждый элемент представляет собой `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область задаётся либо через `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, что повторяет выбор области в пользовательском интерфейсе Excel, либо через `addCellArea(CellArea)` и коллекцию `getPivotAreas()`, которые явно указывают регион.
- **Что проверяет правило?** Один или несколько условий добавляются в `getFormatConditions()` с помощью `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, и каждое условие имеет собственный `getStyle()`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.addArea(CellArea)` у объекта `getFormatConditions()` условного формата сводной таблицы. Эти два перегруженных метода унаследованы из обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос тихо игнорируется. Всегда определяйте регион непосредственно у `PivotConditionalFormat` (`applyTo`, `addCellArea` или `getPivotAreas()`) и добавляйте правило через одну из перегрузок `addCondition`.
{{% /alert %}}

## **Применение правила с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как это делает пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её координатами на листе с нулевой базой, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки значений, которые создаёт сводная таблица, включая промежуточные итоги.  
- `PivotConditionFormatScopeType.FIELD` — ячейки значений, принадлежащие полю, к которому относится ячейка, исключая промежуточные итоги. Ячейка должна быть ячейкой поля, например меткой строкового поля; передача ячейки значения вызывает исключение.  
- `PivotConditionFormatScopeType.SELECTION` — только ячейки значений на пересечении, выбранные ячейкой, обычно одна ячейка значения.  
Ниже пример создаёт сводную таблицу продаж фруктов, где левый‑верхний угол располагается в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `DATA` и выделяет каждое значение больше 200 жирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общей сумме 750 правило закрасит F4, F5 и F7 — вычисленный регион — весь столбец данных F4:F7, и только ячейки, прошедшие проверку, подсветятся.

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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Привязка того же правила к метке строкового поля E4 (строка 3, столбец 4) с областью `FIELD` приводит к региону F4:F6 — тот же столбец данных без строки итогов, потому что область теперь относится к полю `Fruit`, а не ко всему диапазону значений. Область `SELECTION`, привязанная к F4, ограничивается только F4.

## **Определение региона вручную**
Второй способ обходит выбор области и явно задаёт регион на `PivotConditionalFormat`.

### **Прямоугольник листа с addCellArea**
`addCellArea(CellArea)` фиксирует заданный прямоугольник как цель правила. Координаты — это координаты листа с нулевой базой, и регион точно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики промежуточных итогов. Используйте этот метод, когда интересующие ячейки известны и фиксированы в текущем макете сводной таблицы.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Семантический регион сводной таблицы с PivotAreas**
`getPivotAreas()` предоставляет тот же семантический модельный регион, который используется на соседней странице для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `select` или `selectField` и добавьте её через `getPivotAreas().addPivotArea(PivotArea)`. Семантический регион остаётся привязанным к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и изменении макета. Перегрузка `getPivotAreas().add(PivotArea)` всё ещё компилируется, но помечена как устаревшая — предпочтительно использовать `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `add()` на `getConditionalFormats()` добавляет один `PivotConditionalFormat` к сводной таблице. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило со всеми типами, операциями и формулами, а `getCellAreas()` выдаёт те же регионы. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении книги, точно так же, как Excel удаляет условный формат без правила.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Сопутствующие статьи**
- [Применение стиля к сводной таблице](/cells/ru/nodejs-java/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/nodejs-java/format-part-of-pivot-table/)
- [Топ‑10 отображение или фильтрация в сводной таблице](/cells/ru/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}