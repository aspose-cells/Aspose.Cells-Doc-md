---
title: 通过 Microsoft Excel 与 C++ 自动刷新 OLE 对象
linktitle: 自动刷新 OLE 对象
type: docs
weight: 270
url: /zh/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: 学习如何使用 Aspose.Cells 结合 C++ 在 Microsoft Excel 中自动刷新 OLE 对象。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) 属性，用于在在 Microsoft Excel 中打开文件时刷新 OLE 对象。借助此属性，OLE 对象将显示由 Microsoft Excel 生成的正确的 OLE 图像。

{{% /alert %}}

以下示例代码加载了带有非真实OLE图像的[示例Excel文件](5115231.xlsx)。OLE对象实际上是Microsoft Word文档，但示例Excel文件显示的动物图像而非Microsoft Word图像。不过，如果你打开[输出Excel文件](5115225.xlsx)，会看到Microsoft Excel显示了正确的OLE图像。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
