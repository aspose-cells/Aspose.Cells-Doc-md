---
title: تطبيق التصفية المتقدمة لMicrosoft Excel لعرض السجلات التي تلبي معايير معقدة باستخدام C++
linktitle: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 280
url: /ar/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: تعلم كيفية تطبيق التصفية المتقدمة لMicrosoft Excel لعرض السجلات التي تلبي معايير معقدة باستخدام API رقم Aspose.Cells for C++.
keywords: تطبيق عامل تصفية متقدم، تعيين عامل تصفية متقدم، إضافة عامل تصفية متقدم، إنشاء عامل تصفية متقدم، كيفية إضافة عامل تصفية متقدم إلى نطاق
---

## **سيناريوهات الاستخدام المحتملة**

يسمح لك Microsoft Excel بتطبيق *التصفية المتقدمة* على بيانات ورقة العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق التصفية المتقدمة باستخدام أمر *البيانات > متقدمة* كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

كما يسمح Aspose.Cells بتطبيق التصفية المتقدمة باستخدام طريقة [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/). تمامًا مثل Microsoft Excel، يقبل المعلمات التالية.

**isFilter**

يشير ما إذا كان يتم تصفية القائمة في المكان.

**listRange**

نطاق القائمة.

**criteriaRange**

نطاق المعيار.

**copyTo**

نطاق نسخ البيانات إليه.

**uniqueRecordOnly**

عرض أو نسخ الصفوف الفريدة فقط.

## **تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة**

الكود النموذجي التالي يطبق التصفية المتقدمة على ملف Excel [ملف Excel النموذجي](48496692.xlsx) ويولد ملف [ملف إخراج Excel](48496691.xlsx). تُظهر لقطة الشاشة كلا الملفين للمقارنة. كما ترى في لقطة الشاشة، تم تصفية البيانات داخل ملف الإخراج وفقًا لمعايير معقدة.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
