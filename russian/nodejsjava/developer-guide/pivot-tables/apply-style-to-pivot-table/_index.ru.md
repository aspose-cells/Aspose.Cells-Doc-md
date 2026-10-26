---
title: Применение стилей к сводным таблицам в Aspose.Cells for Node.js via Java
linktitle: Применение стилей к сводным таблицам в Aspose.Cells for Node.js via Java
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Node.js via Java, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц, а также shortcut formatAll.
keywords: Aspose.Cells Node.js via Java стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Вызываемый API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.
{{% /alert %}}

## **Введение**
Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочую книгу, а не форматом, из которого вы её читаете. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.
- `PivotTable.pivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.pivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Worksheets.getTableStyles().addPivotTableStyle(...)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.
Кроме того, `PivotTable.formatAll(Style)` — это shortcut, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из перечисленных выше API имён стилей. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**
`PivotTable.autoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: `Report1`–`Report10`, `Classic`, а также `Table1`–`Table10`.
Следующий пример загружает новую рабочую книгу, заполняет образец данных Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.Report5` и сохраняет результат как `.xls`.

{{% alert color="primary" %}}
**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** с полями строк и значениями — у них нет встроенного оформления для заголовков полей столбцов. Если в вашей сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из [Сценария 2](#apply-a-modern-named-preset-pivot-table-style), которые предназначены для двухмерной компоновки, используемой в современном Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Получить первый рабочий лист
let sheet = workbook.getWorksheets().get(0);
// Заполнить исходные данные строкой заголовка (Fruit, Year, Amount)
// и 9 строками данных с grape, blueberry, kiwi, cherry за 2020 и 2021 годы
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Добавить сводную таблицу в ячейку назначения E3, с именем, используя исходный диапазон A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Назначить поля: Fruit -> строки, Amount -> данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Применить предустановленный автоформат устаревшего XLS "Report5"
// Примечание: это свойство имеет значение только при сохранении в формате .xls.
// При сохранении в формате .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
// и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// Сохранить книгу в устаревшем формате .xls
workbook.save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**
`PivotTable.setPivotTableStyleType(int)` выбирает один из встроенных именованных стилей, которые Excel 2007 представил для сводных таблиц. Перечисление `PivotTableStyleType` предоставляет три семейства тем: светлое семейство от `PIVOT_TABLE_STYLE_LIGHT1` до `PIVOT_TABLE_STYLE_LIGHT28`, среднее семейство от `PIVOT_TABLE_STYLE_MEDIUM1` до `PIVOT_TABLE_STYLE_MEDIUM28` и темное семейство от `PIVOT_TABLE_STYLE_DARK1` до `PIVOT_TABLE_STYLE_DARK_28`. Оно также определяет `None` и `Custom`. Элементы каждого семейства с более высокими номерами — это стили, добавленные в Excel 2017.
Эти предустановки доступны только для чтения. Если необходимо изменить цвета, границы или шрифты сверх возможностей предустановки, вместо этого необходимо определить пользовательский стиль сводной таблицы, как показано в [Сценарии 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Почему современные предустановки, а не автоформаты серии отчетов?** Значения `Report1`—`Report10` и `Table1`—`Table10` перечисления `PivotTableAutoFormatType` появились раньше, чем поддержка полей столбцов сводных таблиц, поэтому они не содержат оформления для заголовков полей столбцов, и Excel отображает такие заголовки без оформления. Предустановки `PivotTableStyleType` были разработаны для двумерной компоновки, которую использует современный Excel, и одинаково оформляют заголовки полей строк и полей столбцов.
{{% /alert %}}

В этом сценарии повторно используется набор данных Fruit/Year/Amount из Сценария 1, поле `Year` добавляется в область столбцов рядом с полем строк `Fruit` с помощью `PivotFieldType.COLUMN`, применяется предустановка темной темы `PIVOT_TABLE_STYLE_DARK1` с помощью `pivotTable.setPivotTableStyleType`, а результат сохраняется в формате `.xlsx` — формате, для которого `PivotTableStyleType` имеет смысл.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**
Встроенные предустановки не могут быть изменены. Когда необходимо переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:
1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Этот метод возвращает индекс только что созданного стиля.
2. Настройте стиль, добавив элементы (например, `WholeTable` или `GrandTotalRow`) через `TableStyle.tableStyleElements.add(TableStyleElementType)`, а затем назначьте `Style` каждому элементу через `TableStyleElement.setElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.pivotTableStyleName` равным имени стиля. Здесь не следует использовать `pivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}
`pivotTableStyleName` и `pivotTableStyleType` не взаимозаменяемы. Используйте `pivotTableStyleType` для встроенных предустановок, а `pivotTableStyleName` — для пользовательских стилей, определённых через `addPivotTableStyle`. Установка обоих свойств не вызывает ошибок, но отрисовывается только то, которое соответствует предполагаемому источнику.
Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.
Следующий пример определяет пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и жирным красным шрифтом для `GrandTotalRow`, затем применяет его через `pivotTableStyleName` и сохраняет как `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Заполнение исходных данных: строка заголовков + 9 строк данных (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// Добавление сводной таблицы из диапазона A1:C10, привязанной к E3, с именем
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Шаг 1: регистрация нового пользовательского стиля сводной таблицы и получение его индекса
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Шаг 2: добавление элемента WholeTable и применение тонких чёрных границ со всех четырёх сторон
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Шаг 3: добавление элемента GrandTotalRow и применение жирного красного шрифта
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Шаг 4: применение пользовательского стиля по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью formatAll**
`PivotTable.formatAll(Style)` — это shortcut, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее задано через `pivotTableStyleType` или `pivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}
`formatAll` переопределяет и `pivotTableStyleType`, и `pivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, не зависящий от темы внешний вид по всей сводной таблице.
Следующий пример создаёт `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяет его с помощью `formatAll` и сохраняет как `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Заполнение исходных данных: строка заголовка (строка 1) + 9 строк данных (строки 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Добавление сводной таблицы: исходный диапазон A1:C10, ячейка назначения E3, имя
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// Применение formatAll: принудительно применяет этот единый стиль к каждой ячейке сводной таблицы,
// переопределяя любой ранее установленный PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);
// Сохранение книги в современном формате .xlsx
workbook.save("output.xlsx");
```

## **Какой API стилей следует использовать?**
Выбор API стилей зависит от формата файла, в который выполняется сохранение. Используйте приведённую ниже таблицу в качестве краткого справочника.
| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.autoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.pivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.setElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.formatAll(Style)` | Shortcut, который переопределяет все остальные настройки стилей по всей сводной таблице. |
Если есть сомнения, сохраняйте в `.xlsx` и используйте `pivotTableStyleType` для встроенных тем или `pivotTableStyleName` для пользовательских тем.

{{< app/cells/assistant language="nodejs-java" >}}