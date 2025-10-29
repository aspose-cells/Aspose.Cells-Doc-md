---
title: 使用C++指定DBNum自定义格式化的示例
linktitle: 指定使用DBNum自定义模式格式
description: Aspose.Cells是一个支持使用自定义格式化模式的电子表格处理C++库。本文将向你展示如何使用Aspose.Cells库指定 dbnum 自定义格式，让用户更好地控制数字的显示方式。
keywords: Aspose.Cells，C++库，电子表格，自定义格式模式，格式化， dbnum ，控制显示
type: docs
weight: 110
url: /zh/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能的使用场景**

Aspose.Cells支持*DBNum*自定义格式。例如，如果单元格值为123，并指定其自定义格式为[DBNum2][$-804]General，则显示为壹佰贰拾叁。可以通过[**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)方法和[**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)属性自定义单元格格式。

## **示例代码**

以下示例代码演示如何指定*DBNum*自定义格式。请查看其[输出PDF](43352081.pdf)获取更多帮助。

```cpp
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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
