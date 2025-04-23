---
title: 使用C++将含图片或图表的XLS文件转换成PDF
linktitle: 将带有图像或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: 使用Aspose.Cells将含有图像或图表的XLS文件转换为PDF文件。
---

{{% alert color="primary" %}} 

Aspose.Cells支持将包含图片和图表的XLS文件转换为PDF文档。Aspose.Cells for C++可以独立完成将电子表格转换为PDF的任务：不需要Aspose.PDF for C++。此过程可以在内存中完成，因为不依赖临时或中间XML文件。这意味着大文件（如含有图片、图表及其他绘图对象的Excel）可以快速高效地转换。

{{% /alert %}} 
## **示例代码**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

 如果电子表格包含公式，建议在渲染为PDF之前调用[Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/)方法。这样可以确保公式依赖的值被重新计算，并在PDF中正确显示。

{{% /alert %}}
