---
title: 在 C++ 中设置公式的外部链接
linktitle: 设置公式中的外部链接
type: docs
weight: 20
url: /zh/cpp/set-external-links-in-formulas/
description: 学习如何使用 Aspose.Cells 将外部文件链接包含在公式中，使用 C++。
---

{{% alert color="primary" %}} 

有时，有必要在公式中包含对外部文件的链接，例如，根据外部文件评估单元格或范围值。Aspose.Cells提供了这个功能，本文档解释了如何使用它。

{{% /alert %}} 

下面的示例代码显示了如何在公式中包含外部文件。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
