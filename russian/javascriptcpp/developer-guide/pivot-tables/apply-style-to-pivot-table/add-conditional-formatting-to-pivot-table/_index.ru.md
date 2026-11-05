---
title: Добавление условного форматирования в сводную таблицу
linktitle: Добавление условного форматирования в сводную таблицу
description: Добавление условного форматирования к сводной таблице в Aspose.Cells for JavaScript via C++ — привязать правило к области данных с помощью applyTo и типа PivotConditionFormatScopeType, либо определить цель с помощью addCellArea и pivotAreas, затем присоединить правила и стили через formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, сводная таблица, условное форматирование, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /ru/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на соседней странице, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это управляемый правилами аналог — выделять каждый показатель выше 200, затенять средние пятьдесят процентов или отмечать элементы с наихудшим рейтингом, и выделение следует за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `pivotTable.conditionalFormats`. Каждый элемент — это `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область определяется либо через `applyTo(row, column, scope)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `addCellArea(cellArea)` и коллекцию `pivotAreas`, где область указывается явно.  
- **Что проверяет правило?** Один или несколько условий добавляются в `formatConditions` с помощью `addCondition(type, operatorType, formula1, formula2)`, и каждое условие имеет собственный `style`.

{{% alert color="primary" %}}
Не вызывайте `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` или `formatConditions.addArea(cellArea)` у объекта `formatConditions` условного формата сводной таблицы. Эти два перегруженных метода унаследованы от обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос беззвучно игнорируется. Всегда определяйте область непосредственно в `PivotConditionalFormat` (`applyTo`, `addCellArea` или `pivotAreas`) и добавляйте правило через один из перегруженных методов `addCondition`.  
{{% /alert %}}

## **Применить правило с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как делает это пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её нулевыми координатами листа, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.Data` — все ячейки‑значения, генерируемые сводной таблицей, включая общие итоги.  
- `PivotConditionFormatScopeType.Field` — ячейки‑значения, принадлежащие полю, которое идентифицирует данная ячейка, без общих итогов. Ячейка должна быть ячейкой‑полем, например меткой строки‑поля; попытка передать ячейку‑значение приводит к исключению.  
- `PivotConditionFormatScopeType.Selection` — только те ячейки‑значения, которые пересекаются с выбранной ячейкой, обычно одна ячейка‑значение.
Ниже приведён пример построения сводной таблицы продаж фруктов, левый верхний угол которой находится в E3, привязывает условный формат к ячейке F4 (строка 3, столбец 5) с областью `Data` и выделяет каждый показатель больше 200 полужирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и общем итоге 750 правило закрасит F4, F5 и F7 — разрешённая область охватывает весь столбец данных F4:F7, и подсвечиваются только ячейки, прошедшие проверку.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anchor the conditional format at F4 (row 3, column 5) with the Data scope
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Rule - highlight amounts greater than 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returns the file as bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Привязав то же правило к метке поля‑строки E4 (строка 3, столбец 4) с областью `Field`, оно будет разрешено к F4:F6 — тот же столбец данных без строки общего итога, поскольку область теперь описывает поле `Fruit`, а не всю область значений. Область `Selection`, привязанная к F4, ограничивается только ячейкой F4.

## **Определить область вручную**
Второй способ пропускает выбор области и задаёт её явно в `PivotConditionalFormat`.

### **Прямоугольник листа с addCellArea**
`addCellArea(cellArea)` фиксирует указанный прямоугольник как цель правила. Координаты — нулевые координаты листа, а область точно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики итоговых строк. Используйте этот метод, когда интересующие ячейки образуют известный фиксированный прямоугольник текущего макета сводной таблицы.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Target the rectangle F4:F6 (the value cells without the grand total)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Rule - italic on light yellow for amounts between 150 and 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Семантическая область сводной таблицы с pivotAreas**
`pivotAreas` представляет ту же модель семантической области, которую использует соседняя страница для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `select` или `selectField` и добавьте её через `pivotAreas.addPivotArea(pivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и изменении макета. Перегрузка `pivotAreas.add(pivotArea)` всё ещё работает, но помечена устаревшей — предпочтительно использовать `addPivotArea`.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attach the rule to the Amount data field as a semantic region
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Rule - grey text for amounts below 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `conditionalFormats.add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — при повторном открытии файла, сохранённого в первом примере в Node, отображается то же правило с неизменёнными типом, оператором и формулой, а `getCellAreas()` возвращает ту же область. На этой платформе свойства `type` и `operator` условия представлены числовыми значениями перечислений. Записи, которые никогда не получили условие, отбрасываются при сохранении рабочей книги, так же как Excel удаляет условный формат без правила.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Reload the file written by the first example
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // This prints:
    // Conditional formats: 1
    // Format 0: 1 2 formula1==200   (type 1 = CellValue, operator 2 = GreaterThan)
    //     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
    process.exit(0);
});
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/javascript-cpp/format-part-of-pivot-table/)
- [Отображение или фильтрация топ‑10 в сводной таблице](/cells/ru/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}