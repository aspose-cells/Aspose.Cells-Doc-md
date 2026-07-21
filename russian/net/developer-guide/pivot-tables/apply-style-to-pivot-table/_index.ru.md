---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for .NET, включая устаревшие XLS-автоформаты, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и сокращение FormatAll.
keywords: Aspose.Cells .NET стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). API, которое следует вызывать, зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который сохраняется рабочая книга, а не форматом, из которого она была прочитана. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода в формате `.xls` используйте свойство `PivotTable.AutoFormatType` вместе с перечислением `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Это API соответствует средству выбора автоформата, которое предлагал классический Excel для сводных таблиц.

Для современного вывода в форматах `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.PivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Пользовательские стили требуются всякий раз, когда вы хотите изменить цвета, границы или шрифты за пределами того, что предлагают предустановки.

Кроме того, `PivotTable.FormatAll(Style)` — это сокращение, которое применяет единый объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что было установлено через любой из API имён стилей, описанных выше. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение устаревшего предустановленного автоформата XLS**

`PivotTable.AutoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: `Report1`–`Report10`, `Classic`, а также `Table1`–`Table10`.

{{% alert color="primary" %}}

`AutoFormatType` учитывается только тогда, когда рабочая книга сохраняется в формате `.xls`. Когда та же рабочая книга сохраняется как `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и возвращается к настройкам `PivotTableStyleType` и `PivotTableStyleName`.

{{% /alert %}}

Следующий пример загружает новую рабочую книгу, заполняет примерными данными Fruit/Year/Amount, добавляет сводную таблицу, применяет `PivotTableAutoFormatType.Report5` и сохраняет результат как `.xls`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Сценарий 1: Применение предустановленного автоформата устаревшего формата XLS
// Используемый API: PivotTable.AutoFormatType
// Целевой формат файла: .xls (устаревший)
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Создать новую рабочую книгу
Workbook workbook = new Workbook();

// Получить первый рабочий лист
Worksheet sheet = workbook.Worksheets[0];

// Заполнить исходные данные строкой заголовка (Fruit, Year, Amount)
// и 9 строками данных, охватывающими виноград, чернику, киви, вишню за 2020 и 2021 годы
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

// Добавить сводную таблицу в ячейке назначения E3, с именем "Pivot1", используя исходный диапазон A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Назначить поля: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Применить предустановленный автоформат устаревшего формата XLS "Report5"
// Примечание: Это свойство имеет смысл только при сохранении в формате .xls.
// При сохранении в формате .xlsx/.xlsm/.xlsb Excel игнорирует AutoFormatType
// и использует то, что указано в PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Сохранить рабочую книгу в устаревшем формате .xls
workbook.Save("output.xls");
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.PivotTableStyleType` принимает значение из перечисления `Aspose.Cells.PivotTableStyleType`. Перечисление охватывает светлые темы `PivotTableStyleLight1`–`PivotTableStyleLight28` и тёмные темы `PivotTableStyleDark1`–`PivotTableStyleDark28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файлов. В отличие от устаревшего автоформата, выбранный здесь стиль корректно отображается Excel и сохраняется при циклическом обмене данными с другими инструментами Office.

Следующий пример использует те же данные Fruit/Year/Amount, создаёт идентичную сводную таблицу, применяет `PivotTableStyleDark1` и сохраняет рабочую книгу как `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Сценарий 2: Применение современного именованного предустановленного стиля Excel 2007+ с помощью PivotTableStyleType.
// Целевой формат файла: .xlsx. Перечисление PivotTableStyleType находится в пространстве имён Aspose.Cells
// (а не в Aspose.Cells.Pivot) — поэтому нам не нужен дополнительный using.
// Ссылка на GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Строка заголовков: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 строк данных Fruit / Year / Amount
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

// Добавляем сводную таблицу в ячейке E3 с именем "Pivot1", источник данных A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Назначаем поля сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Применяем современный именованный предустановленный стиль сводной таблицы Excel 2007+.
// PivotTableStyleType — это правильный API для файлов .xlsx / .xlsm / .xlsb; AutoFormatType
// игнорируется Excel для этих форматов. PivotTableStyleDark1 относится к семейству тёмной темы
// (PivotTableStyleDark1..PivotTableStyleDark28), и то же перечисление также предоставляет
// более новые темы Excel 2017 светлая/тёмная (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Сохраняем как современный формат .xlsx — это формат, для которого PivotTableStyleType имеет значение.
workbook.Save("output.xlsx");
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Всякий раз, когда вам нужно переопределить цвета, границы или шрифты, вы должны определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Это возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WholeTable` или `GrandTotalRow`) через `TableStyle.TableStyleElements.Add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `TableStyleElement.SetElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.PivotTableStyleName` равным имени стиля. Здесь не следует использовать `PivotTableStyleType`, поскольку это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`PivotTableStyleName` и `PivotTableStyleType` не являются взаимозаменяемыми. Используйте `PivotTableStyleType` для встроенных предустановок, а `PivotTableStyleName` — для пользовательских стилей, которые вы определили через `AddPivotTableStyle`. Установка обоих безвредна, но отображается только тот, который соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.

Следующий пример определяет пользовательский стиль сводной таблицы с тонкой чёрной границей на `WholeTable` и жирным красным шрифтом на `GrandTotalRow`, затем применяет его через `PivotTableStyleName` и сохраняет как `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Заполнить исходные данные: строка заголовка + 9 строк данных (A1:C10)
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

// Добавить сводную таблицу из диапазона A1:C10 с якорем в E3, именем "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Шаг 1: зарегистрировать новый пользовательский стиль сводной таблицы и запомнить его индекс
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Шаг 2: добавить элемент WholeTable и применить тонкие чёрные границы со всех четырёх сторон
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

// Шаг 3: добавить элемент GrandTotalRow и применить жирный красный шрифт
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Шаг 4: применить пользовательский стиль по имени (НЕ через PivotTableStyleType, который предназначен для встроенных стилей)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Применение единого стиля ко всем ячейкам сводной таблицы с помощью FormatAll**

`PivotTable.FormatAll(Style)` — это сокращение, которое применяет единый объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `PivotTableStyleType` или `PivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`FormatAll` переопределяет как `PivotTableStyleType`, так и `PivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, независимый от темы внешний вид по всей сводной таблице.

{{% /alert %}}

Следующий пример создаёт `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем применяет его с помощью `FormatAll` и сохраняет как `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Сценарий 4: Применение единого стиля к каждой ячейке сводной таблицы с помощью FormatAll
// Используемый API: PivotTable.FormatAll(Style)
// Целевой формат: .xlsx
// Ссылка на GitHub: см. репозиторий Aspose.Cells-for-.NET — примеры стилизации сводных таблиц

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Заполнение исходных данных: строка заголовков (строка 1) + 9 строк данных (строки 2-10)
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

// Добавление сводной таблицы: исходный диапазон A1:C10, целевая ячейка E3, имя "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Назначение полей сводной таблицы: Fruit -> область строк, Year -> область столбцов, Amount -> область данных
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Создание стиля, который будет принудительно применён к каждой ячейке сводной таблицы
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

// Применение FormatAll: принудительно применяет этот единый стиль к каждой ячейке сводной таблицы,
// переопределяя любой ранее установленный PivotTableStyleType / PivotTableStyleName
pivotTable.FormatAll(style);

// Сохранение книги в современном формате .xlsx
workbook.Save("output.xlsx");
```

## **Какой API стилей мне следует использовать?**

Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте приведённую ниже таблицу в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.AutoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.PivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настраивается через `TableStyleElement.SetElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.FormatAll(Style)` | Сокращение, которое переопределяет все остальные настройки стилей по всей сводной таблице. |

В случае сомнений сохраняйте в формате `.xlsx` и используйте `PivotTableStyleType` для встроенных тем или `PivotTableStyleName` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells for .NET](/cells/ru/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}