---
title: Установка условных форматов для Excel и ODS файлов с помощью C++
linktitle: Условные Форматы
type: docs
weight: 60
url: /ru/cpp/conditional-formatting/
description: Как применять условные форматы к файлам Excel и ODS на C++.
keywords: Применить условные форматы 
---

## **Введение**

Условное форматирование - это расширенная функция Microsoft Excel, которая позволяет применять форматы к ячейке или диапазону ячеек и изменять этот формат в зависимости от значения ячейки или значения формулы. Например, вы можете сделать ячейку жирной только тогда, когда значение ячейки больше 500. Когда значение ячейки соответствует условию, указанный формат применяется к ячейке. Если значение ячейки не соответствует условию форматирования, используется форматирование по умолчанию. В Microsoft Excel выберите **Формат**, затем **Условное форматирование**, чтобы открыть диалоговое окно Условного форматирования.

Aspose.Cells поддерживает применение условного форматирования к ячейкам во время выполнения. В этой статье объясняется, как это сделать. Также объясняется, как рассчитать цвет, используемый Excel для условного форматирования по цветовой шкале.

## **Применение условного форматирования**

Aspose.Cells поддерживает условное форматирование несколькими способами:

- Использование дизайнерской таблицы
- Использование метода копирования.
- Создание условного форматирования во время выполнения.

### **Использование дизайнерской таблицы**

Разработчики могут создать дизайнерскую таблицу, содержащую условное форматирование в Microsoft Excel, а затем открыть эту таблицу с помощью Aspose.Cells. Aspose.Cells загружает и сохраняет дизайнерскую таблицу, сохраняя любые настройки условного форматирования.

### **Использование метода копирования**

Aspose.Cells позволяет разработчикам копировать настройки условного форматирования из одной ячейки в другую на листе, вызывая метод [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Применение условного форматирования во время выполнения**

Aspose.Cells позволяет добавлять и удалять условное форматирование во время выполнения. В приведенных ниже примерах кода показано, как установить условное форматирование:

1. Создайте рабочую книгу.
1. Добавьте пустое условное форматирование.
1. Укажите диапазон, к которому должно применяться форматирование.
1. Определите условия форматирования.
1. Сохраните файл.

После этого примера представлено еще несколько меньших примеров, показывающих, как применить настройки шрифта, настройки границ и узоры.

Microsoft Excel 2007 добавил более продвинутое условное форматирование, которое также поддерживает Aspose.Cells. Приведенные здесь примеры иллюстрируют, как использовать простое форматирование, а примеры Microsoft Excel 2007 показывают, как применять более расширенное условное форматирование.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Установить шрифт**

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Можно изменить только стиль шрифта, цвет текста, стиль подчеркивания и стиль зачеркивания.

{{% /alert %}}

### **Установить границу**

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
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Можно использовать только тонкие стили линий для граничной рамки. Диагональные линии не допускаются.

{{% /alert %}}

### **Установить узор**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Продвинутые темы**
- [Добавление условных форматирований 2-цветной шкалы и 3-цветной шкалы](/cells/ru/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Применение расширенного условного форматирования](/cells/ru/cpp/apply-advanced-conditional-formatting/)
- [Применение условного форматирования в рабочих листах](/cells/ru/cpp/apply-conditional-formatting-in-worksheets/)
- [Применение заливки для чередующихся строк и столбцов с условным форматированием](/cells/ru/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Генерировать изображения условного форматирования столбчатых диаграмм данных](/cells/ru/cpp/generate-conditional-formatting-databars-images/)
- [Получить наборы значков, столбчатые диаграммы данных или объекты цветовой шкалы, используемые в условном форматировании](/cells/ru/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
