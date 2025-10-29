---
title: 通过HTML设置单元格值以显示项目符号，使用C++
linktitle: 通过使用HTML设置单元格值显示项目符号
type: docs
weight: 130
url: /zh/cpp/display-bullets-by-setting-cell-value-using/
description: 使用HTML和易于使用的Aspose.Cells for C++ API为Excel单元格添加项目符号。
keywords: 在Excel中添加项目符号，使用C++在Excel中添加项目符号，显示Excel中的项目符号，使用HTML添加项目符号，HTML中显示项目符号，使用HTML显示项目符号
---

{{% alert color="primary" %}}

Aspose.Cells支持使用HTML代码显示项目符号。本文将解释如何通过使用HTML设置单元格值来显示项目符号。我们将使用[**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)属性使用我们的HTML设置单元格值。

{{% /alert %}}

## 使用HTML通过设置单元格值显示项目符号的C++代码

以下代码使用HTML代码设置单元格值。一旦运行此代码，您将获得下面图像中显示的输出。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 示例代码生成的输出

以下截图显示了上述示例代码的输出。

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
