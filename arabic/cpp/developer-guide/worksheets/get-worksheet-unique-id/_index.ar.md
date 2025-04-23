---
title: الحصول على معرف فريد لورقة العمل باستخدام C++
linktitle: الحصول على معرف فريد لورقة العمل
type: docs
weight: 190
url: /ar/cpp/get-worksheet-unique-id/
description: توضح هذه المقالة كيفية الحصول على معرف فريد لورقة عمل إكسل باستخدام مكتبة وواجهة برمجة تطبيقات C++ برمجياً.
keywords: معرف فريد لورقة عمل إكسل C++، معرف فريد لورقة عمل C++
---

## **احصل على معرف فريد لورقة العمل**

تتيح Aspose.Cells إمكانية الحصول على المعرف الفريد لورقة العمل باستخدام طريقة [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/). يوضح مقتطف الكود التالي استخدام طريقة [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) لطباعة المعرف الفريد لورقة العمل. يستخدم مقتطف الكود هذا ملف إكسل النموذجي [105480213.xlsx](105480213.xlsx).

### كود المصدر

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
