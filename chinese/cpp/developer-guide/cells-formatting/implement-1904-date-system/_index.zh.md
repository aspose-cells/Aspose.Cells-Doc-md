---
title: 使用 C++ 实现 1904 日期系统
linktitle: 实现1904日期系统
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库。它支持实现1904日期系统，允许用户根据1904年1月1日的日期系统进行计算和格式化。本文介绍了如何使用Aspose.Cells库实现1904日期系统。
keywords: Aspose.Cells, 1904日期系统, 电子表格, 计算, 格式化
type: docs
weight: 7000
url: /zh/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel支持两种日期系统：1900日期系统（Excel for Windows 中实施的默认日期系统）和1904日期系统。1904日期系统通常用于与Macintosh Excel文件兼容，并且是在使用Excel for Macintosh时的默认系统。您可以使用 Aspose.Cells 设置Excel文件的1904日期系统。

{{% /alert %}}

在 Microsoft Excel 中实现1904日期系统（例如 Microsoft Excel 2003）：

1. 从“工具”菜单中选择“选项”，并选择“计算”选项卡。
1. 选择“1904日期系统”选项。
1. 点击**确定**。

|**在Microsoft Excel中选择1904日期系统**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
请参阅以下示例代码，了解如何使用Aspose.Cells API 实现此功能。

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
