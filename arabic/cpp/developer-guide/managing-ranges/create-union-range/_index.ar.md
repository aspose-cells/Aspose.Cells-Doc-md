---
title: إنشاء اتحاد النطاق باستخدام C++
linktitle: إنشاء مجموعة الاتحاد
type: docs
weight: 360
url: /ar/cpp/create-union-range/
description: إنشاء اتحاد نطاق في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

## **إنشاء مجموعة الاتحاد**
يوفر Aspose.Cells القدرة على إنشاء اتحاد نطاق باستخدام طريقة [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). تستقبل طريقة [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) معلمتين، العنوان لإنشاء الاتحاد والنطاق، وفهرس ورقة العمل. وتعيد طريقة [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) كائن [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/).

يوضح مقتطف الكود التالي كيفية إنشاء اتحاد نطاق باستخدام طريقة [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). الملف الناتج بواسطة الكود مرفق للمراجعة.

- [ملف الناتج](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
