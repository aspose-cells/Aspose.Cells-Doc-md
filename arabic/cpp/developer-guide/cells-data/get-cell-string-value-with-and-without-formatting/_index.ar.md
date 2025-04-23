---
title: الحصول على قيمة سلسلة الخلية مع وبدون تنسيق باستخدام C++
linktitle: الحصول على قيمة سلسلة الخلية
type: docs
weight: 240
url: /ar/cpp/get-cell-string-value-with-and-without-formatting/
description: تعلم كيفية الحصول على قيمة سلسلة الخلية مع وبدون تنسيق من خلال واجهة برمجة تطبيقات Aspose.Cells for C++.
keywords: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
---

{{% alert color="primary" %}}

 يوفر Aspose.Cells طريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) التي يمكن استخدامها للحصول على قيمة النص للخلية مع أو بدون أي تنسيق. لنفترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. ستعرض بعد ذلك كـ 0.01 في Excel. يمكنك استرداد القيم النصية كـ 0.01 و كـ 0.012345 باستخدام الطريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). يأخذ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) كقيمة enum والتي تتضمن القيم التالية:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

يشرح الكود المثال التالي استخدام الطريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/).

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
