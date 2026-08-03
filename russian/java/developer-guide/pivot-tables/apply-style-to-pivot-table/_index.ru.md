---
title: Применить стили к сводным таблицам в Aspose.Cells для .NET
linktitle: Применить стили к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Java, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и ярлык FormatAll.
keywords: Aspose.Cells Java стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). API, которое следует вызывать, зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она читается. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода `.xls` используйте свойство `PivotTable.AutoFormatType` вместе с перечислением `com.aspose.cells.PivotTableAutoFormatType`. Этот API соответствует средству выбора автоформата, которое предлагал классический Excel для сводных таблиц.

Для современных форматов вывода `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.PivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. Пользовательские стили необходимы в тех случаях, когда требуется изменить цвета, границы или шрифты за пределы того, что предлагают предустановки.

Кроме того, `PivotTable.formatAll(Style)` — это ярлык, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что установлено через любой из вышеупомянутых API имён стилей. Это полезно, когда требуется единообразный внешний вид независимо от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**

`PivotTable.AutoFormatType` принимает значение из перечисления `com.aspose.cells.PivotTableAutoFormatType`. Доступные значения: `REPORT_1` — `REPORT_10`, `CLASSIC`, а также `TABLE_1` — `TABLE_10`.

{{% alert color="primary" %}}

`AutoFormatType` учитывается только при сохранении рабочей книги как `.xls`. Когда та же самая рабочая книга сохраняется как `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и возвращается к настройкам `PivotTableStyleType` и `PivotTableStyleName`.

{{% /alert %}}

Следующий пример загружает новую рабочую книгу, заполняет примерными данными Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.REPORT_5` и сохраняет результат как `.xls`.

{{% alert color="primary" %}}

**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** — только с полями строк и значениями, без встроенного оформления для заголовков полей столбцов. Если сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из Сценария 2 ниже — они рассчитаны на двумерную раскладку современного Excel.

{{% /alert %}}

```java
import com.aspose.cells.*;

// Сценарий 1: Применение предустановленного автоформата для устаревшего формата XLS
// Используемый API: PivotTable.AutoFormatType
// Целевой формат файла: .xls (устаревший)
// Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-Java

// Создать новую рабочую книгу
Workbook workbook = new Workbook();

// Получить первый рабочий лист
Worksheet sheet = workbook.getWorksheets().get(0);

// Заполнить исходные данные строкой заголовков (Fruit, Year, Amount)
// и 9 строками данных, охватывающими grape, blueberry, kiwi, cherry за 2020 и 2021 годы
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
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Назначить поля: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Применить предустановленный автоформат "Report5" для устаревшего формата XLS
// Примечание: Это свойство имеет значение только при сохранении в формате .xls.
// При сохранении в формате .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
// и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// Сохранить рабочую книгу в устаревшем формате .xls
workbook.save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.PivotTableStyleType` принимает значение из перечисления `com.aspose.cells.PivotTableStyleType`. Перечисление охватывает светлые темы `PIVOT_TABLE_STYLE_LIGHT_1` — `PIVOT_TABLE_STYLE_LIGHT_28` и тёмные темы `PIVOT_TABLE_STYLE_DARK_1` — `PIVOT_TABLE_STYLE_DARK_28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файлов. В отличие от устаревшего автоформата, выбранный здесь стиль корректно отображается Excel и сохраняется при циклическом обмене через другие инструменты Office.

В следующем примере используются те же данные Fruit/Year/Amount, создаётся идентичная сводная таблица, применяется `PIVOT_TABLE_STYLE_DARK_1`, и рабочая книга сохраняется как `.xlsx`.

```java
import com.aspose.cells.*;

// Сценарий 2: Применение современного именованного предустановленного стиля
// Используемый API: PivotTable.PivotTableStyleType
// Целевой формат файла: .xlsx
// Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-Java

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Строка заголовка: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 строк данных Fruit / Year / Amount
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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Применить современный именованный предустановленный стиль сводной таблицы Excel 2007+.
// PivotTableStyleType является правильным API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
// игнорируется Excel для этих форматов. PivotTableStyleDark1 принадлежит семейству темной темы
// (PivotTableStyleDark1..PivotTableStyleDark28), и тот же enum также предоставляет
// более новые темы Excel 2017 светлые/темные (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Сохранить как современный .xlsx - это формат, для которого PivotTableStyleType имеет значение.
workbook.save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Всякий раз, когда требуется переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Этот метод возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (например, `WholeTable` или `GrandTotalRow`) через `TableStyle.getTableStyleElements().add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `TableStyleElement.setElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.PivotTableStyleName` равным имени стиля. Не используйте здесь `PivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`PivotTableStyleName` и `PivotTableStyleType` не являются взаимозаменяемыми. Используйте `PivotTableStyleType` для встроенных предустановок и `PivotTableStyleName` для пользовательских стилей, определённых через `addPivotTableStyle`. Установка обоих свойств не причинит вреда, но отображаться будет только то, которое соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` и `PAGE_FIELD_VALUES`.

В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и жирным красным шрифтом для `GrandTotalRow`, затем он применяется через `PivotTableStyleName` и сохраняется как `.xlsx`.

```java
import com.aspose.cells.*;

// Сценарий 3: Определение и применение пользовательского стиля сводной таблицы
// Используемый API: PivotTableStyleName + addPivotTableStyle
// Целевой формат файла: .xlsx
// Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-Java

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Заполнить исходные данные: строка заголовка + 9 строк данных (A1:C10)
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

// Добавить сводную таблицу из диапазона A1:C10, привязанную к E3, с именем "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Шаг 1: зарегистрировать новый пользовательский стиль сводной таблицы и сохранить его индекс
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Шаг 2: добавить элемент WholeTable и применить тонкие чёрные границы со всех четырёх сторон
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);

// Шаг 3: добавить элемент GrandTotalRow и применить жирный красный шрифт
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// Шаг 4: применить пользовательский стиль по имени (НЕ через PivotTableStyleType, который используется для встроенных стилей)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Применение одного стиля ко всем ячейкам сводной таблицы с помощью FormatAll**

`PivotTable.formatAll(Style)` — это ярлык, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `PivotTableStyleType` или `PivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`FormatAll` переопределяет как `PivotTableStyleType`, так и `PivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, независимый от темы внешний вид для всей сводной таблицы.

{{% /alert %}}

В следующем примере создаётся `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем он применяется через `formatAll` и сохраняется как `.xlsx`.

```java
import com.aspose.cells.*;

// Сценарий 4: Применение одного стиля ко всем ячейкам сводной таблицы
// Используемый API: PivotTable.formatAll(Style)
// Целевой формат файла: .xlsx
// Для полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-Java

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());

style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());

// Применение FormatAll: принудительно применяет этот единственный стиль к каждой ячейке сводной таблицы,
// переопределяя любой ранее установленный PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// Сохранение книги в современном формате .xlsx
workbook.save("output.xlsx");
```

## **Какой API стилей следует использовать?**

Выбор API стилей зависит от формата файла, в который выполняется сохранение. Используйте приведённую ниже таблицу в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.AutoFormatType` | Значения из `com.aspose.cells.PivotTableAutoFormatType` (например, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.PivotTableStyleType` | Значения из `com.aspose.cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.setElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.formatAll(Style)` | Ярлык, который переопределяет все остальные настройки стилей для всей сводной таблицы. |

В случае сомнений сохраняйте как `.xlsx` и используйте `PivotTableStyleType` для встроенных тем либо `PivotTableStyleName` для пользовательских тем.
{{< app/cells/assistant language="java" >}}