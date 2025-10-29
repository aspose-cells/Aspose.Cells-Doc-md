---
title: 设置共享公式（用 C++）
linktitle: 设置共享公式
type: docs
weight: 10
url: /zh/cpp/setting-shared-formula/
description: 学习如何在 Excel 工作表中用 Aspose.Cells 设置共享公式，使用 C++。
---

{{% alert color="primary" %}}

如果你想在工作表中添加一个会进行计算的函数，本文介绍如何使用 Aspose.Cells实现此任务。

{{% /alert %}}

## 使用Aspose.Cells设置共享公式

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

|**带单列数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

Aspose.Cells允许您使用[**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/)属性指定一个公式。有两种选项可用于将公式添加到列中的其他单元格（B3、B4、B5等等）。

或者像你为第一个单元格所做的那样，为每个单元格设置公式，并相应更新单元格引用（A3*0.09, A4*0.09, A5*0.09 等）。这需要逐行更新单元格引用，也需要 Aspose.Cells 逐个解析每个公式，对于大型表格或复杂公式会比较耗时，也会多出一些代码，虽然循环可以略微减少这些代码。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，使得税款可以正确计算。这种[**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) 方法比第一种方法更有效。

以下示例演示了如何使用它。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
