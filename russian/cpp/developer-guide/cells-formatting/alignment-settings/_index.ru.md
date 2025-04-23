---
title: Настройки выравнивания с помощью C++
linktitle: Настройки выравнивания
description: В библиотеке Aspose.Cells вы можете использовать настройки выравнивания ячеек для настройки макета и отображения текста. Регулируя такие настройки, как горизонтальное выравнивание, вертикальное выравнивание и перенос текста, у вас есть больше контроля над тем, как текст распределяется в ячейках. В этом документе будут предоставлены подробные инструкции и образцовый код, чтобы помочь вам быстро освоить, как использовать Aspose.Cells для настройки выравнивания ячеек.
keywords: Aspose.Cells, настройка ячейки, горизонтальное выравнивание, вертикальное выравнивание, перенос текста
type: docs
weight: 20
url: /ru/cpp/cells-alignment-settings/
---

## **Настройка настроек выравнивания**

### **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

Как видно на приведенной выше фигуре, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Управление текстом.
- Направление текста.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и обсуждаются более подробно ниже.

### **Настройки выравнивания в Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Каждый элемент в коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) и [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) для класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) предоставляет полезные свойства для настройки настроек выравнивания.

Выберите любой тип выравнивания текста, используя перечисление [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/). Предопределенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) следующие:

|**Типы выравнивания текста**|**Описание**|
| :- | :- |
|Bottom|Представляет выравнивание текста по нижнему краю|
|Center|Представляет выравнивание текста по центру|
|CenterAcross|Представляет выравнивание текста по центру с наложением|
|Distributed|Представляет распределенное выравнивание текста|
|Fill|Представляет выравнивание текста по заливке|
|General|Представляет общее выравнивание текста|
|Justify|Представляет выравнивание текста по ширине|
|Left|Представляет выравнивание текста влево|
|Right|Представляет выравнивание текста вправо|
|Top|Представляет верхнее выравнивание текста|
|JustifiedLow|Выравнивает текст с настройкой длины кашиды для арабского текста.|
|ThaiDistributed|Распределяет текст на тайском, поскольку каждый символ рассматривается как слово.|

{{% alert color="primary" %}}

Также можно применить установку равномерного распределения с использованием свойства [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/).

{{% /alert %}}

#### **Горизонтальное выравнивание**

Используйте свойство [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) для горизонтального выравнивания текста.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Вертикальное выравнивание**

Аналогично горизонтальному выравниванию, используйте свойство [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) для вертикального выравнивания текста.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Отступ**

Возможно установить уровень отступа текста в ячейке с помощью свойства [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Ориентация**

Установите ориентацию (поворот) текста в ячейке с помощью свойства [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

##### **Перенос текста**

Перенос текста в ячейке облегчает его чтение: высота ячейки подстраивается под весь текст, вместо его обрезки или выливания в смежные ячейки. Установите включение или отключение переноса текста с помощью свойства [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Уменьшение для подгонки**

Вариантом для переноса текста в поле является уменьшение размера текста для вписывания его в размеры ячейки. Это делается путем установки свойства [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) в **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Объединение ячеек**

Как и в Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предоставляет два подхода к этой задаче. Один из способов - вызвать метод коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/). Метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Другой способ - сначала вызвать метод коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) для создания диапазона ячеек, которые будут объединены. Метод [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) принимает тот же набор параметров, что и метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/), обсуждаемый выше, и возвращает объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) также предоставляет метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/), который объединяет диапазон, указанный в объекте [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения задается свойством [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Aspose.Cells предоставляет предопределенные типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/cpp/line-breaks-and-text-wrapping/)
