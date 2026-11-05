---
title: Добавить условное форматирование к сводной таблице
linktitle: Добавить условное форматирование к сводной таблице
description: Добавить условное форматирование к сводной таблице в Aspose.Cells for Java — привязать правило к области данных с помощью applyTo и области PivotConditionFormatScopeType, либо определить целевую область с помощью addCellArea и getPivotAreas, затем присоединить правила и стили через FormatConditions.addCondition.
keywords: Aspose.Cells for Java, Сводная таблица, условное форматирование, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /ru/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на основной странице и на соседней странице, статичны — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это правило‑ориентированный аналог — подсвечивает каждую сумму выше 200, затемняет средние пятьдесят процентов или отмечает элементы с наименьшим рейтингом — и подсветка следует за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводных таблиц находится в коллекции `PivotTable.getConditionalFormats()`. Каждая запись представляет собой `PivotConditionalFormat`, отвечающий независимо на два вопроса:
- **Где применяется правило?** Целевая область задаётся либо через `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, что соответствует выбору области в пользовательском интерфейсе Excel, либо через `addCellArea(CellArea)` и коллекцию `getPivotAreas()`, где область указывается явно.  
- **Что проверяется правилом?** Одна или несколько условий добавляются в `getFormatConditions()` с помощью `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, и каждое условие содержит свой `Style`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.addArea(CellArea)` в коллекции `getFormatConditions()` условного формата сводной таблицы. Эти два перегруженных метода наследуются из обычного API условного форматирования листа и не работают для сводных таблиц — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос тихо игнорируется. Всегда определяйте область непосредственно у `PivotConditionalFormat` (`applyTo`, `addCellArea` или `getPivotAreas()`) и добавляйте правило с помощью одного из перегруженных методов `addCondition`.
{{% /alert %}}

## **Применить правило с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как делает это пользовательский интерфейс Excel. Ячейка сводной таблицы задаётся её нулево‑базовыми координатами на листе, а область `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.DATA` — все ячейки‑значения, которые создаёт сводная таблица, включая итоговые значения.  
- `PivotConditionFormatScopeType.FIELD` — ячейки‑значения, принадлежащие полю, которое идентифицирует данная ячейка, без промежуточных итогов. Ячейка должна быть ячейкой‑полем, например меткой поля строки; передача ячейки‑значения вызывает исключение.  
- `PivotConditionFormatScopeType.SELECTION` — только те ячейки‑значения, которые находятся на пересечении, выбранном ячейкой, обычно одна ячейка‑значение.
Ниже пример создания сводной таблицы продаж фруктов с левым верхним углом в E3, привязки условного формата к ячейке F4 (строка 3, столбец 5) с областью `DATA` и подсветки каждой суммы, превышающей 200, жирным белым шрифтом на красном фоне. При значениях Apple 220, Banana 330, Cherry 200 и итоговом 750 правило раскрашивает F4, F5 и F7 — разрешённая область — весь столбец данных F4:F7, и подсвечиваются только те ячейки, чьё значение удовлетворяет правилу.

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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Привязка того же правила к метке поля строки E4 (строка 3, столбец 4) с областью `FIELD` приводит к области F4:F6 — тот же столбец данных без строки итогов — поскольку область теперь описывает поле `Fruit`, а не всю область значений. Область `SELECTION`, привязанная к F4, охватывает только ячейку F4.

## **Определить область вручную**
Второй способ пропускает выбор области и явно задаёт её у `PivotConditionalFormat`.

### **Прямоугольник листа с addCellArea**
`addCellArea(CellArea)` сохраняет заданный прямоугольник как цель правила. Координаты — нулево‑базовые координаты листа, и область точно соответствует переданному прямоугольнику — без расширения до столбца данных и без логики итогов. Используйте, когда интересующие ячейки образуют известный фиксированный прямоугольник текущего макета сводной таблицы.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Семантическая область сводной таблицы с getPivotAreas**
`getPivotAreas()` возвращает ту же модель семантической области, что используется на соседней странице для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `select` или `selectField`, и добавьте её через `getPivotAreas().addPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и смещении макета. Перегрузка `getPivotAreas().add(PivotArea)` всё ещё компилируется, но помечена устаревшей — предпочтительно использовать `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Где хранятся правила и как они сохраняются при перезагрузке**
Каждый вызов `getConditionalFormats().add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — повторное открытие файла в примере ниже показывает то же правило с его типом, оператором и формулой, а `getCellAreas()` возвращает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении книги, точно так же, как Excel удаляет условный формат без правила.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Связанные статьи**
- [Применение стиля к сводной таблице](/cells/ru/java/apply-style-to-pivot-table/)
- [Форматировать часть сводной таблицы](/cells/ru/java/format-part-of-pivot-table/)
- [Топ‑10 показывать или фильтровать в сводной таблице](/cells/ru/java/top-10-show-or-filter-in-pivot-table/)
- [Фильтрация сводных таблиц по метке или значению](/cells/ru/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}