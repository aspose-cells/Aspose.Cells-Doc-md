---
title: Применение стилей к сводным таблицам
linktitle: Применение стилей к сводным таблицам
description: Узнайте, как применять встроенные и пользовательские стили к сводным таблицам в Aspose.Cells for C++, включая устаревшие автоформаты XLS, современные именованные стили Excel 2007+, пользовательские стили сводных таблиц и сокращение FormatAll
keywords: Aspose.Cells C++ стиль сводной таблицы, PivotTableStyleType, AutoFormatType, FormatAll, пользовательский стиль, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ru/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает применение как устаревших автоформатов сводных таблиц (предназначенных для файлов `.xls`), так и современных именованных или пользовательских стилей сводных таблиц (предназначенных для файлов `.xlsx`, `.xlsm` и `.xlsb`). Вызываемый API зависит от формата файла, в который сохраняется рабочая книга, а не от формата, из которого она была загружена.

{{% /alert %}}

## **Введение**

Aspose.Cells предоставляет два параллельных API стилей для сводных таблиц. Выбор между ними определяется форматом файла, в который вы сохраняете рабочую книгу, а не форматом, из которого вы её читаете. Рабочая книга, загруженная из файла `.xls`, может быть повторно сохранена как `.xlsx`, и в этом случае применяется современный API стилей, а не устаревший.

Для устаревшего вывода в формате `.xls` используйте свойство `PivotTable.AutoFormatType` вместе с перечислением `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Этот API соответствует средству выбора автоформата, которое предлагал классический Excel для сводных таблиц.

Для современных форматов вывода `.xlsx`, `.xlsm` и `.xlsb` доступны два варианта API стилей:

- `PivotTable.PivotTableStyleType` выбирает один из встроенных именованных стилей (светлые и тёмные темы, включая стили, добавленные в Excel 2017). Эти предустановки доступны только для чтения.
- `PivotTable.PivotTableStyleName` выбирает пользовательский стиль, который вы определяете самостоятельно через `Worksheets.TableStyles.AddPivotTableStyle(...)`. Пользовательские стили необходимы в тех случаях, когда требуется изменить цвета, границы или шрифты за пределы того, что предлагают предустановки.

Кроме того, `PivotTable.FormatAll(Style)` является сокращением, которое применяет один объект `Style` к каждой ячейке сводной таблицы, переопределяя всё, что задано через любой из указанных выше API имён стилей. Это полезно, когда требуется единообразный внешний вид вне зависимости от базовой темы.

## **Применение предустановленного автоформата устаревшего XLS**

`PivotTable.AutoFormatType` принимает значение из перечисления `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Доступные значения: `Report1`–`Report10`, `Classic` и `Table1`–`Table10`.

{{% alert color="primary" %}}

`AutoFormatType` учитывается только при сохранении рабочей книги в формате `.xls`. Когда та же рабочая книга сохраняется как `.xlsx`, `.xlsm` или `.xlsb`, Excel игнорирует это свойство и возвращается к настройкам `PivotTableStyleType` и `PivotTableStyleName`.

{{% /alert %}}

В следующем примере загружается новая рабочая книга, заполняются примерные данные Fruit/Year/Amount, добавляется сводная таблица, применяется `PivotTableAutoFormatType.Report5`, и результат сохраняется в формате `.xls`.

{{% alert color="primary" %}}

**Почему нет полей столбцов?** Автоформаты серии Report (`Report1`–`Report10`, `Table1`–`Table10`) были разработаны в классическом Excel для **одномерных сводных таблиц** — только с полями строк и значениями, без встроенного оформления для заголовков полей столбцов. Если сводной таблице нужны поля столбцов, используйте современные предустановки `PivotTableStyleType` из Сценария 2 ниже — они рассчитаны на двумерную раскладку современного Excel.

{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Создаём новую рабочую книгу
    Workbook workbook;

    // Получаем первый рабочий лист
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Заполняем исходные данные строкой заголовка (Fruit, Year, Amount)
    // и 9 строками данных, охватывающими grape, blueberry, kiwi, cherry за 2020 и 2021 годы
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // Добавляем сводную таблицу в ячейку назначения E3 с именем "Pivot1", используя исходный диапазон A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Назначаем поля: Fruit -> Строки, Year -> Столбцы, Amount -> Данные
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Применяем предустановленный автоформат устаревшего формата XLS "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Сохраняем рабочую книгу в устаревшем формате .xls
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Применение современного именованного предустановленного стиля сводной таблицы**

`PivotTable.PivotTableStyleType` принимает значение из перечисления `Aspose.Cells.PivotTableStyleType`. Перечисление охватывает светлые темы `PivotTableStyleLight1`–`PivotTableStyleLight28` и тёмные темы `PivotTableStyleDark1`–`PivotTableStyleDark28`. Стили, добавленные в Excel 2017 (вторая волна светлых и тёмных тем), доступны через то же перечисление.

Это рекомендуемый API для любого современного формата файлов. В отличие от устаревшего автоформата, выбранный здесь стиль точно отображается Excel и сохраняется при циклическом обмене данными с другими инструментами Office.

В следующем примере используются те же данные Fruit/Year/Amount, создаётся идентичная сводная таблица, применяется `PivotTableStyleDark1`, и рабочая книга сохраняется в формате `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Определение и применение пользовательского стиля сводной таблицы**

Встроенные предустановки не могут быть изменены. Всякий раз, когда вам нужно переопределить цвета, границы или шрифты, вы должны определить пользовательский стиль сводной таблицы. Рабочий процесс состоит из трёх шагов:

1. Добавьте пользовательский стиль в коллекцию `TableStyles` рабочей книги через `Worksheets.TableStyles.AddPivotTableStyle(string name)`. Это возвращает индекс вновь созданного стиля.
2. Настройте стиль, добавляя элементы (такие как `WholeTable` или `GrandTotalRow`) через `TableStyle.TableStyleElements.Add(TableStyleElementType)`, затем назначьте `Style` каждому элементу через `TableStyleElement.SetElementStyle(Style)`.
3. Примените пользовательский стиль к сводной таблице, установив `PivotTable.PivotTableStyleName` равным имени стиля. Не используйте здесь `PivotTableStyleType`, так как это свойство выбирает встроенные предустановки.

{{% alert color="primary" %}}

`PivotTableStyleName` и `PivotTableStyleType` не являются взаимозаменяемыми. Используйте `PivotTableStyleType` для встроенных предустановок и `PivotTableStyleName` для пользовательских стилей, которые вы определили через `AddPivotTableStyle`. Установка обоих свойств не вызывает ошибок, но отображается только то, которое соответствует предполагаемому источнику.

{{% /alert %}}

Доступные значения `TableStyleElementType` включают `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` и `PageFieldValues`.

В следующем примере определяется пользовательский стиль сводной таблицы с тонкой чёрной границей для `WholeTable` и жирным красным шрифтом для `GrandTotalRow`, затем он применяется через `PivotTableStyleName` и сохраняется в формате `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Заполнение исходных данных: строка заголовка + 9 строк данных (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // Добавление сводной таблицы с источником A1:C10, привязанной к E3, с именем "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Шаг 1: регистрация нового пользовательского стиля сводной таблицы и сохранение его индекса
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Шаг 2: добавление элемента WholeTable и применение тонких черных границ со всех четырех сторон
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Шаг 3: добавление элемента GrandTotalRow и применение жирного красного шрифта
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Шаг 4: применение пользовательского стиля по имени (НЕ через PivotTableStyleType, который предназначен для встроенных предустановок)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Применение одного стиля к каждой ячейке сводной таблицы с помощью FormatAll**

`PivotTable.FormatAll(Style)` является сокращением, которое применяет один объект `Style` к каждой ячейке сводной таблицы, включая область данных, заголовки строк и столбцов, а также итоги. Всё, что было ранее установлено через `PivotTableStyleType` или `PivotTableStyleName`, переопределяется.

{{% alert color="primary" %}}

`FormatAll` переопределяет как `PivotTableStyleType`, так и `PivotTableStyleName`. Используйте его только тогда, когда требуется единообразный, независимый от темы внешний вид по всей сводной таблице.

{{% /alert %}}

В следующем примере создаётся `Style` с жёлтой сплошной заливкой, жирным тёмно-синим шрифтом и тонкими чёрными границами со всех сторон, затем он применяется с помощью `FormatAll` и сохраняется в формате `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Строка заголовка
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Строки данных
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Добавить сводную таблицу: исходный диапазон A1:C10, ячейка назначения E3, имя "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Назначить поля сводной таблицы
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Создать стиль, который будет применён к каждой ячейке сводной таблицы
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // Применить FormatAll
    pivotTable.FormatAll(style);

    // Сохранить книгу
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Какой API стилей мне следует использовать?**

Выбор API стилей зависит от формата файла, в который вы сохраняете. Используйте таблицу ниже в качестве краткого справочника.

| Целевой формат файла | Используемый API | Примечания |
|---|---|---|
| `.xls` (устаревший) | `PivotTable.AutoFormatType` | Значения из `Aspose.Cells.Pivot.PivotTableAutoFormatType` (например, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Игнорируется при сохранении в современных форматах. |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, встроенный стиль) | `PivotTable.PivotTableStyleType` | Значения из `Aspose.Cells.PivotTableStyleType` (светлые/тёмные темы, включая дополнения Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (современный, пользовательский стиль) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Используйте, когда встроенных предустановок недостаточно. Настройка через `TableStyleElement.SetElementStyle(...)`. |
| Любой формат (единообразное переопределение) | `PivotTable.FormatAll(Style)` | Сокращение, которое переопределяет все остальные настройки стилей по всей сводной таблице. |

В случае сомнений сохраняйте в формате `.xlsx` и используйте `PivotTableStyleType` для встроенных тем или `PivotTableStyleName` для пользовательских тем.

## **Связанные статьи**

- [Обновление сводных таблиц в Aspose.Cells for Aspose.Cells for C++](/cells/ru/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}