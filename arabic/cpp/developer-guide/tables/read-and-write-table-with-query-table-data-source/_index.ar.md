---
title: اقرأ واكتب جدولًا بمصدر بيانات جدول الاستعلام باستخدام C++
linktitle: قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام
type: docs
weight: 30
url: /ar/cpp/read-and-write-table-with-query-table-data-source/
description: تعرف على كيفية قراءة وكتابة الجداول باستخدام QueryTable كمصدر بيانات باستخدام Aspose.Cells for C++.
---

## **قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام**
مع Aspose.Cells، يمكنك قراءة وكتابة جدول يحتوي على QueryTable كمصدر للبيانات. الدعم لهذه الميزة موجود أيضًا لملفات XLS. يوضح المقطع التالي قراءة وكتابة جدول من هذا النوع من خلال قراءة الجدول أولًا ثم تعديله لإضافة صف الإجماليات.

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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

الملفات Excel المصدر والإخراج مرفقة للمرجعية.

[ملف المصدر](96928091.xls)

[ملف الناتج](96928092.xls)
