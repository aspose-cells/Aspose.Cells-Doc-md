---
title: الحصول على عرض عرض النص لقيمة الخلية باستخدام C++
linktitle: الحصول على عرض النص لقيمة الخلية
type: docs
weight: 50
url: /ar/cpp/get-text-width-of-cell-value/
description: تعلم كيفية الحصول على عرض عرض النص لقيمة الخلية من خلال API Aspose.Cells for C++.
keywords: الحصول على عرض النص لقيمة الخلية، الحصول على عرض النص لقيمة الخلية
---

## **الحصول على عرض النص لقيمة الخلية**

 في بعض الأحيان، قد يحتاج المطورون إلى حساب عرض قيمة الخلية لتنظيم البيانات في بعض التصاميم. توفر Aspose.Cells الطريقة [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) التي تسمح للمطورين بالحصول على عرض نص قيمة الخلية. يوضح الرمز النموذجي التالي كيفية استخدام [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) للوصول إلى عرض النص لقيمة الخلية.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

ملف المصدر (96928090.xlsx)

## كود عينة

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
