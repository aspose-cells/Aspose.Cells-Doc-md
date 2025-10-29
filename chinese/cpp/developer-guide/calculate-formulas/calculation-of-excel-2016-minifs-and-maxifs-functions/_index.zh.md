---
title: 用C++计算Excel 2016的MINIFS和MAXIFS函数
description: 本文介绍如何使用Aspose.Cells库在C++中计算Microsoft Excel 2016的MINIFS和MAXIFS函数。
keywords: Aspose.Cells, Excel, 2016, MINIFS函数, MAXIFS函数, 计算
type: docs
weight: 300
url: /zh/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能的使用场景**
Microsoft Excel 2016支持MINIFS和MAXIFS函数。这些函数在Excel 2013或更早版本中不支持。Aspose.Cells也支持这些函数的计算。以下截图展示了这些函数的用法。请阅读截图中的红色注释，了解它们是如何工作的。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **计算Excel 2016的MINIFS和MAXIFS函数**
下面的示例代码加载[示例Excel文件](5115149.xlsx)，调用[Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)方法通过Aspose.Cells执行公式计算，然后将结果保存为[输出PDF](5115154.pdf)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
