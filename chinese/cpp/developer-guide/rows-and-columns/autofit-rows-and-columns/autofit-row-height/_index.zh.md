---
title: 在加载文件时自动调整行高（C++）
linktitle: 在加载文件时自动调整行高
type: docs
weight: 120
url: /zh/cpp/autofit-row-height/
description: 了解如何使用 Aspose.Cells 与 C++ 自动适应未使用自定义高度的行。
keywords: 在加载文件时自动调整行高，打开Excel文件时自动调整行高。
---

## **可能的使用场景**
 行高会自动匹配内容字体，但当缓存行的高度不匹配文件中内容的高度时，MS Excel 在加载文件时会自动调整行高，而 Aspose.Cells 为了提高性能不会自动调整。如果需要在加载文件时使用 Aspose.Cells 程序自动匹配行高，可以通过参数 [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) 实现。

请参考以下图像数据。我们可以观察到第11行的缓存行高为15，但是Excel在加载文件时会自动调整行高。
<br>
<img src="1.png" width=70% />

## **使用Aspose.Cells调整行高**
如果直接加载文件并将其保存为PDF，那么数据在PDF中将无法完全显示，因为其缓存行高仅为15。
<br>
<img src="2.png" width=70% />
<br>
 如果在加载文件时将参数 [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) 设置为 true，Aspose.Cells 将自动调整行高。调整后的行高可以有效满足文本显示需求。
<br>
<img src="3.png" width=70% />

## ** C++ 示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
