---
title: إضافة اتصال محوري باستخدام C++
linktitle: إضافة اتصال المحور
type: docs
weight: 30
url: /ar/cpp/add-pivot-connection/
description: تعلم كيفية إضافة اتصال محوري مع مكتبة Aspose.Cells باستخدام C++.
keywords: إضافة اتصال المحور بدون مكتب 2013، مكتب 2016، مكتب 2019 ومكتب 365.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت ترغب في ربط المنقي والجدول المحوري في Excel، عليك بالنقر بزر الماوس الأيمن على المنقي واختيار عنصر "اتصالات التقرير...". في قائمة الخيارات، يمكنك القيام بعمليات على مربع الاختيار. بالمثل، إذا كنت ترغب في ربط المنقي والجدول المحوري عن طريق استخدام واجهة برمجة التطبيقات Aspose.Cells، يرجى استخدام الطريقة [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/). ستقوم بربط المنقي والجدول المحوري.

## **ربط المنقي والجدول المحوري**

يحمل الكود النموذجي التالي [ملف Excel عيني](add-pivot-connection.xlsx) الذي يحتوي على منقي موجود. يصل إلى المنقي ومن ثم يقوم بربط المنقي والجدول المحوري. وأخيرًا، يحفظ المصنف كـ [ملف Excel الناتج](add-pivot-connection-out.xlsx). 

## **الكود المثالي**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
