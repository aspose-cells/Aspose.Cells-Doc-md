---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавьте условное форматирование к сводной таблице в Aspose.Cells for Node.js via C++ — привяжите правило к области данных с помощью applyTo и PivotConditionFormatScopeType, либо определите целевую область с помощью addCellArea и pivotAreas, затем прикрепите правила и стили через formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, сводная таблица, условное форматирование, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /ru/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это правило‑ориентированный аналог: выделить каждый показатель выше 200, затемнить средние пятьдесят процентов или пометить элементы с наименьшими рейтингами — и подсветка будет следовать за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `pivotTable.getConditionalFormats()`. Каждая запись — это `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область задаётся либо через `applyTo(row, column, scope)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `addCellArea(cellArea)` и коллекцию `pivotConditionalFormat.getPivotAreas()`, где область указывается явно.
- **Что проверяется правилом?** Один или несколько условий добавляются в `formatConditions`, получаемый через `pivotConditionalFormat.getFormatConditions()`, с помощью `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, и каждое условие имеет собственный стиль, получаемый через `getStyle()`.

{{% alert color="primary" %}}
Не вызывайте `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` или `formatConditions.addArea(cellArea)` у объекта `formatConditions` условного формата сводной таблицы. Эти две перегрузки унаследованы от обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос будет тихо проигнорирован. Всегда задавайте область непосредственно у объекта `pivotConditionalFormat` (`applyTo`, `addCellArea` или `getPivotAreas()`) и добавляйте правило одной из перегрузок `addCondition`.
{{% /alert %}}

## **Применить правило с областью (способ, аналогичный пользовательскому интерфейсу Excel)**
Первый способ позиционирует правило так же, как делает это пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко должно распространяться правило от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки‑значения, которые создает сводная таблица, включая общие итоги.
- `PivotConditionFormatScopeType.FIELD` — ячейки‑значения, принадлежащие полю, которое идентифицирует ячейка, за исключением общих итогов. Ячейка должна быть ячейкой‑полем, например меткой строкового поля; передача ячейки‑значения вызывает исключение.
- `PivotConditionFormatScopeType.SELECTION` — только те ячейки‑значения, которые находятся на пересечении, выбранном ячейкой, обычно одна ячейка‑значение.
Ниже приводится пример создания сводной таблицы продаж фруктов, левый‑верхний угол которой находится в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `DATA` и выделяет каждый показатель более 200 жирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило закрашивает F4, F5 и F7 — разрешённая область охватывает весь столбец данных F4:F7, и только ячейки, чьи значения удовлетворяют правилу, подсвечиваются.

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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Привязка того же правила к метке поля строки E4 (строка 3, столбец 4) с областью `FIELD` приводит к диапазону F4:F6 — тот же столбец данных без строки общего итога, потому что область теперь описывает поле `Fruit`, а не всю область значений. Область `SELECTION`, привязанная к F4, ограничивается только F4.

## **Определить область вручную**
Второй способ обходит выбор области и задаёт её явно у `PivotConditionalFormat`.

### **Прямоугольник рабочего листа с addCellArea**
`addCellArea(cellArea)` фиксирует указанный прямоугольник как цель правила. Координаты — это нулевые координаты листа, и область точно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики общих итогов. Используйте этот метод, когда интересующие ячейки известны как фиксированный прямоугольник текущего макета сводной таблицы.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Семантическая область сводной таблицы с getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` представляет ту же семантическую модель области, что и на соседней странице для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `select` или `selectField`, и добавьте её через `pivotAreas.addPivotArea(pivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и изменении макета. Перегрузка `pivotAreas.add(pivotArea)` всё ещё компилируется, но помечена как устаревшая — предпочтительно использовать `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `conditionalFormats.add()` добавляет один `PivotConditionalFormat` к сводной таблице. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило с его типом, оператором и формулой, а `getCellAreas()` возвращает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, как Excel удаляет условный формат без правила.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/nodejs-cpp/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/nodejs-cpp/format-part-of-pivot-table/)
- [Топ‑10 отображения или фильтрации в сводной таблице](/cells/ru/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}