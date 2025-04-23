---
title: 使用C++在渲染Excel为PDF时绘制时间线
linktitle: 将Excel渲染为PDF时绘制时间轴
type: docs
weight: 60
url: /zh/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: 在C++中使用Aspose.Cells管理Excel文件的时间线。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下将时间轴渲染为PDF
---

## **将Excel文件应用时间轴并导出为PDF。Aspose.Cells for Java现在默认支持此功能。只需将带有时间轴的Excel文件导出为PDF，生成的PDF将显示应用的时间轴。**
如果你的Excel文件已经应用了时间线，并希望在导出为PDF时保留时间线设置，Aspose.Cells现在默认支持此功能。只需将带时间线的Excel导出为PDF，生成的PDF将显示时间线。

以下示例代码加载包含现有时间轴的[样本Excel文件](input.xlsx)，然后将工作簿另存为[输出PDF文件](out.pdf)。以下屏幕截图比较了源Excel文件和生成的PDF文件。

<img src="out.png" width="60%">

## **示例代码**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

