---
title: 检测工作表中的合并单元格
linktitle: 检测合并单元格
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库。它支持检测工作表中的合并单元格，方便用户识别和操作这些单元格。本文将介绍如何使用 Aspose.Cells 库检测合并单元格。
keywords: Aspose.Cells，工作表，合并单元，检测，识别，操作
type: docs
weight: 80
url: /zh/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

本文介绍如何在工作表中获取合并的单元区域。

Aspose.Cells允许您在工作表中获取合并的单元区域。您也可以取消合并（拆分）它们。本文展示了使用**Aspose.Cells API**执行任务的最简单的代码。

{{% /alert %}}

该组件提供 [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) 方法，可以获取所有合并单元格。以下示例代码演示如何在工作表中检测合并单元格。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
