---
title: 用C++获取带格式和不带格式的单元格字符串值
linktitle: 获取单元格字符串值
type: docs
weight: 240
url: /zh/cpp/get-cell-string-value-with-and-without-formatting/
description: 学习如何通过 Aspose.Cells for C++ API 获取带格式和不带格式的单元格字符串值。
keywords: 使用带有格式和不带格式的单元格字符串值，检索带格式和不带格式的单元格字符串值，获取带格式和不带格式的单元格字符串值
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) 方法，可以用来获取单元格的字符串值，无论是否带有任何格式。假设你有一个值为0.012345的单元格，并将其格式化为仅显示两位小数，那么在Excel中会显示为0.01。你可以使用 [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) 方法以字符串形式同时获取0.01和0.012345。它接受 [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) 枚举作为参数，具有以下值：

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

以下示例代码解释了使用[**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)方法的用法。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
