---
title: نسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline باستخدام C++
linktitle: نسخ Sparkline عن طريق تحديد نطاق البيانات والموقع
type: docs
weight: 300
url: /ar/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: تعلم كيفية نسخ sparklines عن طريق تحديد نطاق البيانات والموقع باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يسمح Microsoft Excel لك بنسخ شرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط. تدعم Aspose.Cells هذه الميزة.

{{% /alert %}}

لنسخ الشرارة إلى خلايا أخرى في Microsoft Excel:

1. حدد الخلية التي تحتوي على الشرارة.
1. حدد **Edit Data** من **قسم Sparkline** من **tDesign** علامة التبويب.
1. حدد **Edit Group Location & Data**.
1. حدد نطاق البيانات والموقع.
1. انقر على **موافق**.

يوفر Aspose.Cells طريقة `SparklineCollection.Add(dataRange, row, column)` لتحديد نطاق البيانات وموقع مجموعة Sparkline. يقوم الكود النموذجي التالي بتحميل ملف Excel المصدر كما هو موضح في الصورة أعلاه، ثم يصل إلى أول مجموعة Sparkline ويضيف نطاقات البيانات والمواقع في المجموعة. أخيراً، يكتب ملف Excel الناتج على القرص والذي يظهر أيضًا في الصورة أعلاه.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
