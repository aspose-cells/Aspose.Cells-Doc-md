---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Node.js via Java, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и быстрый метод FormatAll.
keywords: Aspose.Cells for Node.js via Java стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). API, который следует вызывать, зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она была прочитана. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода `.xls` используйте свойство `PivotTable.autoFormatType` вместе с перечислением `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Этот API соответствует средству выбора автоформата, которое предлагал классический Excel для сводных таблиц.

Для современного вывода `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.pivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.pivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Worksheets.getTableStyles().addPivotTableStyle(...)`. Пользовательские стили необходимы в тех случаях, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.

Кроме того, `PivotTable.formatAll(Style)` является быстрым методом, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из вышеуказанных API именованных стилей. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**

`PivotTable.autoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: от `Report1` до `Report10`, `Classic`, а также от `Table1` до `Table10`.

{{% alert color="primary" %}}

`autoFormatType` учитывается только при сохранении рабочей книги в формате `.xls`. Когда та же рабочая книга сохраняется в формате `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и использует настройки `pivotTableStyleType` и `pivotTableStyleName`.

{{% /alert %}}

В следующем примере загружается новая рабочая книга, заполняются тестовые данные Fruit/Year/Amount, добавляется сводная таблица, применяется `PivotTableAutoFormatType.Report5`, и результат сохраняется как `.xls`.

```javascript
let workbook = new AsposeCells.Workbook();

// Получить первый рабочий лист
let sheet = workbook.getWorksheets().get(0);

// Заполнить исходные данные строкой заголовка (Fruit, Year, Amount)
// и 9 строками данных по grape, blueberry, kiwi, cherry за 2020 и 2021 годы
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

// Добавить сводную таблицу в ячейку назначения E3 с именем "Pivot1", используя исходный диапазон A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Назначить поля: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Применить предустановленный автоформат "Report5" из устаревшего формата XLS
// Примечание: это свойство имеет смысл только при сохранении в формате .xls.
// При сохранении в .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
// и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Сохранить книгу в устаревшем формате .xls
workbook.save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.pivotTableStyleType` принимает значение из перечисления `Aspose.Cells.PivotTableStyleType`. Перечисление охватывает светлые темы от `PivotTableStyleLight1` до `PivotTableStyleLight28` и тёмные темы от `PivotTableStyleDark1` до `PivotTableStyleDark28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файлов. В отличие от устаревшего автоформата, выбранный здесь стиль точно отображается Excel и сохраняется при циклическом обмене данными с другими инструментами Office.

В следующем примере используются те же данные Fruit/Year/Amount, создаётся идентичная сводная таблица, применяется `PivotTableStyleDark1`, и рабочая книга сохраняется как `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Строка заголовка: Фрукт / Год / Количество
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 строк данных Фрукт / Год / Количество
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

// Добавить сводную таблицу в E3 с именем "Pivot1", источник данных A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Фрукт -> Область строк, Год -> Область столбцов, Количество -> Область данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Применить современный именованный предустановленный стиль сводной таблицы Excel 2007+.
// PivotTableStyleType — правильный API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
// игнорируется Excel для этих форматов. PivotTableStyleDark1 принадлежит семейству тёмной темы
// (PivotTableStyleDark1..PivotTableStyleDark28), и то же перечисление также предоставляет
// новые темы Excel 2017 светлая/тёмная (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Сохранить как современный .xlsx — это формат, для которого PivotTableStyleType имеет значение.
workbook.save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки невозможно изменить. Когда требуется переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Метод возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (например, `WholeTable` или `GrandTotalRow`) через `TableStyle.tableStyleElements.add(TableStyleElementType)`, затем назначьте `Style` каждому элементу с помощью `TableStyleElement.setElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.pivotTableStyleName` равным имени стиля. Здесь не следует использовать `pivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`pivotTableStyleName` и `pivotTableStyleType` не являются взаимозаменяемыми. Используйте `pivotTableStyleType` для встроенных предустановок, а `pivotTableStyleName` — для пользовательских стилей, определённых через `addPivotTableStyle`. Установка обоих безвредна, но отображается только тот, который соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.

В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для элемента `WholeTable` и жирным красным шрифтом для элемента `GrandTotalRow`, затем он применяется через `pivotTableStyleName` и сохраняется как `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Заполнение исходных данных: строка заголовка + 9 строк данных (A1:C10)
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

// Добавление сводной таблицы на основе A1:C10, привязанной к E3, с именем "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

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
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Шаг 3: добавление элемента GrandTotalRow и применение жирного красного шрифта
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Шаг 4: применение пользовательского стиля по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Применение одного стиля к каждой ячейке сводной таблицы с помощью FormatAll**

`PivotTable.formatAll(Style)` — это быстрый метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее задано через `pivotTableStyleType` или `pivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`formatAll` переопределяет как `pivotTableStyleType`, так и `pivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, не зависящий от темы внешний вид по всей сводной таблице.

{{% /alert %}}

В следующем примере создаётся `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяется через `formatAll` и сохраняется как `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Заполнение исходных данных: строка заголовков (строка 1) + 9 строк данных (строки 2-10)
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

// Добавление сводной таблицы: исходный диапазон A1:C10, ячейка назначения E3, имя "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);

// Применение FormatAll: принудительно применяет этот стиль к каждой ячейке сводной таблицы,
// переопределяя любые ранее установленные PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// Сохранение книги в современном формате .xlsx
workbook.save("output.xlsx");
```

## **Какой API стилей следует использовать?**

Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте приведённую ниже таблицу в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.autoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.pivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.setElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.formatAll(Style)` | Быстрый метод, который переопределяет любые другие настройки стилей по всей сводной таблице. |

В случае сомнений сохраняйте в формате `.xlsx` и используйте `pivotTableStyleType` для встроенных тем или `pivotTableStyleName` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/ru/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="javascript" >}}