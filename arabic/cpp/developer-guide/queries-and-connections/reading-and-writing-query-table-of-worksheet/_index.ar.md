---
title: قراءة وكتابة جدول الاستعلام في ورقة العمل باستخدام C++
linktitle: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 40
url: /ar/cpp/reading-and-writing-query-table-of-worksheet/
description: تعلم كيفية قراءة وكتابة جداول الاستعلام في أوراق عمل Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells مجموعة `Worksheet.QueryTables`، والتي تُرجع كائن من نوع `QueryTable` حسب الفهرس. تحتوي على الخاصيتين التاليتين:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

كلاهما قيمتان منطقيتان (Boolean). يمكنك رؤيتهما عبر Microsoft Excel من خلال **البيانات > الاتصالات > الخصائص**.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام لورقة العمل

يقرأ الكود النموذجي التالي أول `QueryTable` من ورقة العمل الأولى ثم يطبع كلا من خصائص `QueryTable`. ثم يضبط `QueryTable.PreserveFormatting` على `true`.

يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [ملف Excel المصدر](5115533.xlsx)
- [ملف Excel الناتج](5115537.xlsx)

```c++
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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### إخراج الكونسول

إليك الإخراج في وحدة التحكم للكود أعلاه:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرجاع نطاق نتائج جدول الاستعلام

يتيح Aspose.Cells خيار قراءة العنوان (أي نطاق النتائج للخلايا) لجدول الاستعلام. يوضح الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل الملف النموذجي [هنا](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
