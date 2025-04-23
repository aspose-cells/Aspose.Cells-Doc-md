---
title: 用 C++ 实现非连续范围
linktitle: 实现非连续范围
type: docs
weight: 700
url: /zh/cpp/implementing-non-sequential-ranges/
description: 学习如何使用 Aspose.Cells 和 C++ 创建非邻接单元格的命名范围。
---

{{% alert color="primary" %}} 

通常，命名范围是连续和相邻的单元格组成的矩形。但有时，您可能需要使用一个非连续的单元格范围，其中单元格不是相邻的。Aspose.Cells支持创建具有非相邻单元格的命名范围。

{{% /alert %}} 

下面的示例代码展示了如何用 Aspose.Cells for C++ 创建一个非连续命名范围。

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

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
