---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for Node.js via C++, включая устаревшие XLS-автоформаты, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и сокращение FormatAll.
keywords: Aspose.Cells Node.js via C++ стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Вызываемый API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочую книгу, а не форматом, из которого она была прочитана. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода `.xls` используйте свойство `PivotTable.AutoFormatType` вместе с перечислением `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Этот API соответствует выбору автоформата, который классический Excel предлагал для сводных таблиц.

Для современного вывода `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.PivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.

Кроме того, `PivotTable.FormatAll(Style)` — это сокращение, которое применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из API имён стилей выше. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**

`PivotTable.AutoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: от `Report1` до `Report10`, `Classic` и от `Table1` до `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` учитывается только при сохранении рабочей книги как `.xls`. Когда та же рабочая книга сохраняется как `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и возвращается к настройкам `PivotTableStyleType` и `PivotTableStyleName`.

{{% /alert %}}

Следующий пример загружает новую рабочую книгу, заполняет образец данных Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.Report5` и сохраняет результат как `.xls`.

{{% alert color="primary" %}}

**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** — только с полями строк и значениями, без встроенного оформления для заголовков полей столбцов. Если сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из Сценария 2 ниже — они рассчитаны на двумерную раскладку современного Excel.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// Сценарий 1: Применение предустановленного автоформата из старого формата XLS
// Используемый API: PivotTable.AutoFormatType
// Целевой формат файла: .xls (устаревший)
// Полные примеры и файлы данных доступны по ссылке https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Создание новой книги
const workbook = new AsposeCells.Workbook();

// Получение первого листа
const sheet = workbook.getWorksheets().get(0);

// Заполнение исходных данных строкой заголовков (Fruit, Year, Amount)
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

// Добавление сводной таблицы в ячейку назначения E3, с именем "Pivot1", использующей исходный диапазон A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// Назначение полей: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Применение предустановленного автоформата из старого формата XLS "Report5"
// Примечание: Это свойство имеет смысл только при сохранении в формате .xls.
// При сохранении в форматах .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
// и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Сохранение книги в устаревшем формате .xls
workbook.save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.PivotTableStyleType` принимает значение из перечисления `Aspose.Cells.PivotTableStyleType`. Перечисление охватывает светлые темы от `PivotTableStyleLight1` до `PivotTableStyleLight28` и тёмные темы от `PivotTableStyleDark1` до `PivotTableStyleDark28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файлов. В отличие от устаревшего автоформата, выбранный здесь стиль точно отображается Excel и сохраняется при циклическом обмене через другие инструменты Office.

Следующий пример использует те же данные Fruit/Year/Amount, создаёт идентичную сводную таблицу, применяет `PivotTableStyleDark1` и сохраняет рабочую книгу как `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Строка заголовков: Фрукт / Год / Количество
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 строк данных: Фрукт / Год / Количество
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

// Добавить сводную таблицу в ячейке E3 с именем "Pivot1", источник данных — A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Применить современный именованный стиль сводной таблицы из набора Excel 2007+.
// PivotTableStyleType — корректный API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
// игнорируется Excel для этих форматов. PivotTableStyleDark1 принадлежит семейству тёмных тем
// (PivotTableStyleDark1..PivotTableStyleDark28), и то же перечисление также предоставляет
// новые светлые/тёмные темы Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// Сохранить как современный .xlsx — это формат, для которого PivotTableStyleType имеет значение.
workbook.save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Когда необходимо переопределить цвета, границы или шрифты, следует определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Это возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WholeTable` или `GrandTotalRow`) через `TableStyle.TableStyleElements.Add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `TableStyleElement.SetElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.PivotTableStyleName` равным имени стиля. Не используйте здесь `PivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`PivotTableStyleName` и `PivotTableStyleType` не взаимозаменяемы. Используйте `PivotTableStyleType` для встроенных предустановок и `PivotTableStyleName` для пользовательских стилей, определённых через `AddPivotTableStyle`. Установка обоих безвредна, но отображается только тот, который соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.

Следующий пример определяет пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и жирным красным шрифтом для `GrandTotalRow`, затем применяет его через `PivotTableStyleName` и сохраняет как `.xlsx`.

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

// Добавление сводной таблицы с источником A1:C10, привязанной к E3, с именем "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Шаг 1: зарегистрировать новый пользовательский стиль сводной таблицы и сохранить его индекс
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Шаг 2: добавить элемент WholeTable и применить тонкие чёрные границы со всех четырёх сторон
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);

// Шаг 3: добавить элемент GrandTotalRow и применить жирный красный шрифт
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);

// Шаг 4: применить пользовательский стиль по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Применение одного стиля к каждой ячейке сводной таблицы с помощью FormatAll**

`PivotTable.FormatAll(Style)` — это сокращение, которое применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее задано через `PivotTableStyleType` или `PivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`FormatAll` переопределяет как `PivotTableStyleType`, так и `PivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, независимый от темы внешний вид во всей сводной таблице.

{{% /alert %}}

Следующий пример создаёт `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяет его с помощью `FormatAll` и сохраняет как `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Заполнить исходные данные: строка заголовка (строка 1) + 9 строк данных (строки 2-10)
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

// Добавить сводную таблицу: исходный диапазон A1:C10, ячейка назначения E3, имя "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Назначить поля сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Создать стиль, который будет принудительно применён к каждой ячейке сводной таблицы
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

// Применить FormatAll: принудительно применяет этот единственный стиль к каждой ячейке сводной таблицы,
// переопределяя любой ранее установленный PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// Сохранить книгу в современном формате .xlsx
workbook.save("output.xlsx");
```

## **Какой API стилей следует использовать?**

Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте приведённую ниже таблицу в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.AutoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.PivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.SetElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.FormatAll(Style)` | Сокращение, переопределяющее все остальные настройки стилей во всей сводной таблице. |

В случае сомнений сохраняйте как `.xlsx` и используйте `PivotTableStyleType` для встроенных тем или `PivotTableStyleName` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells для Aspose.Cells для Node.js через C++](/cells/ru/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript" >}}
