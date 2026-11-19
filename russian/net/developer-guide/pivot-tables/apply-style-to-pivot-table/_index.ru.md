---
title: Применение стилей к сводным таблицам в Aspose.Cells for .NET
linktitle: Применение стилей к сводным таблицам в Aspose.Cells for .NET
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for .NET, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и вспомогательный метод FormatAll.
keywords: стиль сводной таблицы Aspose.Cells .NET, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Выбор API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.
{{% /alert %}}

## **Введение**
Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она считывается. Рабочую книгу, загруженную из файла `.xls`, можно повторно сохранить как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.
- `PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.PivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Пользовательские стили необходимы, когда требуется изменить цвета, границы или шрифты сверх того, что предлагают предустановки.
Кроме того, `PivotTable.FormatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было задано через любой из приведённых выше API стилей. Это полезно, когда требуется единообразный внешний вид независимо от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**
`PivotTable.AutoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: от `Report1` до `Report10`, `Classic` и от `Table1` до `Table10`.
Следующий пример загружает новую рабочую книгу, заполняет её примерами данных Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.Report5` и сохраняет результат как `.xls`.

{{% alert color="primary" %}}
**Почему нет полей столбцов?** Автоформаты серии Report (от `Report1` до `Report10`, от `Table1` до `Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** с полями строк и значениями — у них нет встроенного оформления для заголовков полей столбцов. Если вашей сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из [Сценария 2](#apply-a-modern-named-preset-pivot-table-style), которые предназначены для двухмерного макета, используемого современным Excel.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");
sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);
sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);
sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);
sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);
sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);
sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);
sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);
sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);
sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);
// Add a pivot table at destination cell E3, using source range A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Save the workbook in legacy .xls format
workbook.Save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**
`PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей, которые Excel 2007 представил для сводных таблиц. Перечисление `PivotTableStyleType` предоставляет три семейства тем: светлое семейство от `PivotTableStyleLight1` до `PivotTableStyleLight28`, среднее семейство от `PivotTableStyleMedium1` до `PivotTableStyleMedium28` и темное семейство от `PivotTableStyleDark1` до `PivotTableStyleDark28`. Оно также определяет `None` и `Custom`. Члены с более высокими номерами в каждом семействе — это стили, добавленные в Excel 2017.
Эти предустановки доступны только для чтения. Как только необходимо изменить цвета, границы или шрифты сверх того, что предоставляет предустановка, следует определить пользовательский стиль сводной таблицы, как показано в [Сценарии 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Почему современные предустановки, а не автоформатирование серий отчетов?** Значения `Report1`—`Report10` и `Table1`—`Table10` перечисления `PivotTableAutoFormatType` существовали до появления полей столбцов сводных таблиц, поэтому они не содержат оформления для заголовков полей столбцов, и Excel отображает такие заголовки без оформления. Предустановки `PivotTableStyleType` разработаны для двумерной компоновки, которую использует современный Excel, и одинаково оформляют заголовки полей строк и полей столбцов.
{{% /alert %}}

В этом сценарии повторно используется набор данных Fruit/Year/Amount из сценария 1, поле `Year` добавляется в область столбцов рядом с полем строк `Fruit` с помощью `PivotFieldType.Column`, применяется предустановка темной темы `PivotTableStyleDark1` с помощью `PivotTable.PivotTableStyleType`, а результат сохраняется в формате `.xlsx` — формате, для которого `PivotTableStyleType` имеет смысл.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
// Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
// (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
// GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Header row: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);
// Add a pivot table at E3, sourced from A1:C10
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.Save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**
Встроенные предустановки не могут быть изменены. Когда вам нужно переопределить цвета, границы или шрифты, необходимо определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:
1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Этот метод возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WholeTable` или `GrandTotalRow`) через `TableStyle.TableStyleElements.Add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `TableStyleElement.SetElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.PivotTableStyleName` равным имени стиля. Не используйте здесь `PivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}
`PivotTableStyleName` и `PivotTableStyleType` не взаимозаменяемы. Используйте `PivotTableStyleType` для встроенных предустановок и `PivotTableStyleName` для пользовательских стилей, определённых через `AddPivotTableStyle`. Установка обоих свойств безвредна, но отображается только то, которое соответствует предполагаемому источнику.
Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.
Следующий пример определяет пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и жирным красным шрифтом для `GrandTotalRow`, затем применяет его через `PivotTableStyleName` и сохраняет как `.xlsx`.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
using Aspose.Cells.Tables;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row + 9 data rows (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);
// Add pivot table sourced from A1:C10, anchored at E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// Step 2: add a WholeTable element and apply thin black borders on all four sides
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **Применение одного стиля к каждой ячейке сводной таблицы с помощью FormatAll**
`PivotTable.FormatAll(Style)` — это вспомогательный метод, который применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `PivotTableStyleType` или `PivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}
`FormatAll` переопределяет и `PivotTableStyleType`, и `PivotTableStyleName`. Используйте его только в том случае, когда требуется единообразный, не зависящий от темы внешний вид по всей сводной таблице.
Следующий пример создаёт `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяет его с помощью `FormatAll` и сохраняет как `.xlsx`.
{{% /alert %}}

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 4: Apply a single Style to every pivot table cell using FormatAll
// API in use: PivotTable.FormatAll(Style)
// Target format: .xlsx
// GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);
// Add pivot table: source range A1:C10, destination cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;
// Apply FormatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.FormatAll(style);
// Save the workbook in the modern .xlsx format
workbook.Save("output.xlsx");
```

## **Какой API стилей следует использовать?**
Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте таблицу ниже в качестве краткого справочника.
| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.AutoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современные форматы. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.PivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.SetElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.FormatAll(Style)` | Вспомогательный метод, переопределяющий любые другие настройки стилей по всей сводной таблице. |
В случае сомнений сохраняйте в формате `.xlsx` и используйте `PivotTableStyleType` для встроенных тем или `PivotTableStyleName` для пользовательских тем.

## Связанные статьи
- [Добавление полей строк и столбцов сводной таблицы в Aspose.Cells for .NET](/cells/ru/net/pivot-table-add-row-and-column-fields/)
- [Управление полями значений сводной таблицы в Aspose.Cells for .NET](/cells/ru/net/manage-value-fields/)
- [Обновление сводных таблиц в Aspose.Cells for .NET](/cells/ru/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}