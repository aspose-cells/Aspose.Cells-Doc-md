---
title: 判断工作表纸张大小是否自动
linktitle: 确定工作表的纸张尺寸是否为自动
type: docs
weight: 90
url: /zh/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: 本文说明如何使用 C++ API 或示例代码，判断工作表的纸张大小是否为自动。
keywords: 判断工作表的纸张大小是否为自动 c++
---

## **可能的使用场景**

大多数情况下，工作表的纸张大小是自动的。当为自动时，通常设置为“Letter”。有时用户会根据需要设置工作表的纸张大小，此时纸张大小不是自动的。你可以使用 **Worksheet** 类的 [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) 属性检查工作表的纸张设置是否为自动。

## **确定工作表的纸张大小是否自动**

以下给出的示例代码加载以下两个Excel文件

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

并且判断他们的第一个工作表的纸张大小是否为自动。在 Microsoft Excel 中，你可以通过页面设置窗口检查纸张大小是否为自动，如此屏幕截图所示。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **控制台输出**

以下是上述示例代码在给定的示例Excel文件上执行时的控制台输出。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
