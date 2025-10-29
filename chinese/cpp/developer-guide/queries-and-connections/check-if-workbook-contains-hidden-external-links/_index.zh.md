---
title: 使用 C++ 检查工作簿是否包含隐藏的外部链接
linktitle: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 230
url: /zh/cpp/check-if-workbook-contains-hidden-external-links/
description: 学习如何使用 Aspose.Cells for C++检测Excel工作簿中的隐藏外部链接。
---

## **可能的使用场景**
 有时工作簿中包含隐藏的外部链接，无法在Microsoft Excel中查看。Aspose.Cells 会检索所有外部链接，无论它们是否可见。然而，你可以检查 [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) 属性以确认外部链接是否可见。

## **检查工作簿是否包含隐藏的外部链接**
 以下示例加载包含隐藏外部链接的 [源Excel文件](5115413.xlsx)。这些链接在Microsoft Excel中不可见，但在工作簿中存在。打印 [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) 和 [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/)，之后会输出 [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) 属性。在控制台输出中，你可以看到所有外部链接都不可见。

### **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **控制台输出**
这是执行给定[源Excel文件](5115413.xlsx)时上述示例代码的控制台输出。

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
