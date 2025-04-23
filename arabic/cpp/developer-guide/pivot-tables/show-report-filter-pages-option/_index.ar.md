---
title: عرض صفحة تقرير الفلتر مع خيار C++
linktitle: عرض صفحة خيار تصفية التقارير
type: docs
weight: 110
url: /ar/cpp/show-report-filter-pages-option/
description: تعلم كيف تمكّن خيار "عرض صفحات تصفية التقرير" في جداول البيانات المحورية باستخدام Aspose.Cells for C++.
---

## **عرض خيار تصفية صفحات التقرير**
يدعم Excel إنشاء الجداول المحورية، وإضافة عوامل تصفية التقارير، وتمكين خيار "عرض صفحات تصفية التقرير". كما يدعم Aspose.Cells هذه الميزة لتمكين خيار "عرض صفحات تصفية التقرير" على الجدول المحوري الذي تم إنشاؤه. أدناه لقطة شاشة توضح خيار "عرض صفحات تصفية التقرير" في Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

يمكن تنزيل ملف المصدر وملفات الإخراج التجريبية من هنا لاختبار الشيفرة التجريبية:

`[ملف إكسل المصدر](81920786.xlsx)` 

[ملف إكسل الناتج](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
