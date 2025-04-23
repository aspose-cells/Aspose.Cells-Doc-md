---
title: Изменение выравнивания ячеек и сохранение существующего форматирования с помощью C++
description: Используйте библиотеку Aspose.Cells для изменения выравнивания ячеек и сохранения существующего форматирования
keywords: Aspose.Cells, C++, выравнивание ячеек, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вы хотите изменить выравнивание нескольких ячеек, при этом сохранив существующее форматирование. Aspose.Cells позволяет сделать это с помощью свойства [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/). Если установить его в **true**, изменения в выравнивании произойдут, иначе — нет. Обратите внимание, что объект [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) передается как параметр в метод [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
