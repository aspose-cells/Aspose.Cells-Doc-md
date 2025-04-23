---
title: 使用C++在工作表中显示公式而非值
linktitle: 显示公式而非值
type: docs
weight: 20
url: /zh/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: 本文提供了使用C++ API以编程方式在Excel工作表或电子表格中显示公式而非值的示例代码。
---

{{% alert color="primary" %}}

可以使用**公式**选项来显示Microsoft Excel中公式而不是计算值。当显示公式时，Microsoft Excel在工作表中显示公式。您可以使用Aspose.Cells实现相同的功能。

{{% /alert %}}

Aspose.Cells提供了一个[**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/)属性。将其设置为**true**可以使Microsoft Excel显示公式。

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

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
