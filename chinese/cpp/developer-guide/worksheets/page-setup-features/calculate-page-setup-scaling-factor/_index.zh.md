---
title: 用 C++ 计算页面设置缩放比例
linktitle: 计算页面设置缩放因子
type: docs
weight: 300
url: /zh/cpp/calculate-page-setup-scaling-factor/
description: 本文提供示例代码，说明如何使用 C++ API 或库通过程序方式计算网页宽度为 n 页，高度为 m 页的页面设置缩放比例。
keywords: 用 C++ 调整适合宽度为 n 页，高度为 m 页的页面设置，计算缩放比例
---

{{% alert color="primary" %}}

当您使用“按n页宽和m页高适应”选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。您可以使用[**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/)属性计算相同的内容。该属性返回一个Double值，可以转换为百分比值。例如，如果它返回0.5，则表示缩放因子为50%。

{{% /alert %}}

以下示例代码说明了如何使用[**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/)属性计算页面设置缩放因子。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
