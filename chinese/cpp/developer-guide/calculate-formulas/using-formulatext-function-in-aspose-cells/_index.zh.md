---
title: 使用FormulaText函数在Aspose.Cells与C++中
linktitle: 使用FormulaText函数
description: 本文介绍了如何使用Aspose.Cells库中的FormulaText函数处理Microsoft Excel中的公式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法获取和设置单元格的公式文本并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, FormulaText函数
type: docs
weight: 60
url: /zh/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText是Excel 2013及以后的函数。不支持以前的版本，如Excel 2010或2007等。正如其名称所示，它打印给定单元格中存在的公式的文本。本文将向您展示如何使用Aspose.Cells利用此函数。

{{% /alert %}} 

以下示例代码显示了如何使用Aspose.Cells中的FormulaText。代码首先在单元格A1中编写一个公式，然后使用FormulaText在单元格A2中打印出公式的文本。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
