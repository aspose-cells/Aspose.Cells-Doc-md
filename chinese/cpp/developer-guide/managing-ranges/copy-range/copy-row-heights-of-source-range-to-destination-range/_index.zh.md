---
title: 用 C++ 将源范围的行高复制到目标范围
linktitle: 将源范围行高度复制到目标范围
type: docs
weight: 590
url: /zh/cpp/copy-row-heights-of-source-range-to-destination-range/
description: 学习如何使用 Aspose.Cells for C++ 将行高从源范围复制到目标范围。
---

{{% alert color="primary" %}}

有时用户需要将行高从源范围复制到目标范围。Aspose.Cells 提供了 [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) 枚举来实现这一点。当你用 [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) 枚举设置 [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) 属性时，源范围内所有行的高度将被复制到目标范围。

{{% /alert %}}

以下示例代码演示了如何使用 [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) 枚举将行高从源范围复制到目标范围。将此代码生成的 Excel 文件在 Microsoft Excel 中打开后，你会看到目标范围的行高与源范围完全一致。

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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
