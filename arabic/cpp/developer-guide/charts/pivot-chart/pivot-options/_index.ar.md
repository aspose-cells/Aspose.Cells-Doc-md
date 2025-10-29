---
title: كيفية إدارة PivotChart باستخدام PivotOptions في C++
linktitle: Pivot Options
type: docs
weight: 10
url: /ar/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: كيفية إدارة PivotChart باستخدام PivotOptions باستخدام C++.
keywords: PivotChart
---

## ما هو PivotChart

PivotChart في Excel هو تمثيل رسومي للبيانات تم إنشاؤه من PivotTable. يتيح للمستخدمين تصور البيانات وتحليلها ديناميكيًا من خلال تلخيص وعرض المعلومات في شكل رسوم بيانية. تكون PivotCharts تفاعلية ويمكن تعديلها بسهولة لعرض وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات والعرض في Excel.

## كيفية إدارة PivotChart مع PivotOptions

من خلال استخدام Aspose.Cells، يمكنك استخدام [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) لإدارة PivotChart.

ملف وكود مثالي:  
[ملف المثال](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

مع الكود المثالي أعلاه، يمكنك التحقق من ملف النتيجة بالتأثير التالي، كما هو موضح في الشكل:

**![النتيجة](الناتج.png)**
{{< app/cells/assistant language="cpp" >}}
