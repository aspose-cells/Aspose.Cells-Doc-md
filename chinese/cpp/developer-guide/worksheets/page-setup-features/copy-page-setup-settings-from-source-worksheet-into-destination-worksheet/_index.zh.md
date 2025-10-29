---
title: 用 C++ 将页面设置从源工作表复制到目标工作表
linktitle: 复制页面设置
type: docs
weight: 80
url: /zh/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: 本文说明如何使用 C++ API 或示例代码，将页面设置从源工作表复制到目标工作表。
keywords: 用 C++ 复制页面设置，复制页面设置到目标工作表
---

## **可能的使用场景**

当您向工作簿添加新工作表时，它包含默认的*页面设置*。有时您需要将页面设置([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/))从一个工作表转移到另一个工作表。本文解释了如何使用Aspose.Cells APIs从一个工作表复制页面设置到另一个工作表。

## **将源工作表中的页面设置复制到目标工作表**

以下示例代码说明了如何使用[**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/)方法从一个工作表复制*页面设置*到另一个工作表。请查看以下示例代码及其控制台输出以供参考。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
