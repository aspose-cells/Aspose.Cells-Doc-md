---
title: 用C++合并或取消合并单元格范围
linktitle: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/cpp/merge-or-unmerge-range-of-cells/
description: 用C++在Excel中合并和取消合并范围内的单元格。
keywords: 用C++合并和取消合并范围内的单元格，使用C++合并和取消合并范围内的单元格，使用C++合并和取消合并单元格范围，使用C++合并和取消合并单元格，使用C++在Excel中合并和取消合并单元格，使用C++在Excel中合并单元格，使用C++取消合并单元格，使用C++在范围内合并单元格
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 来合并或拆分一系列单元格。Aspose.Cells 为此提供了 [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) 和 [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) 方法。本文解释了如何将一系列单元格合并为单个单元格。

{{% /alert %}}

## **示例**

以下示例代码首先创建一个范围 — A1:D4 — 然后使用[**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)方法将该范围中的单元格合并成一个单元格。类似地，你也可以通过创建范围并调用[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)方法来拆分单元格。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
