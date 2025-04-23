---
title: إزالة اتصال Pivot باستخدام C++
linktitle: إزالة اتصال الجدول المحوري
type: docs
weight: 30
url: /ar/cpp/remove-pivot-connection/
description: تعلم كيفية إزالة اتصال Pivot باستخدام مكتبة Aspose.Cells باستخدام C++.
keywords: إزالة اتصال الجدول المحوري من دون استخدام Office 2013، Office 2016، Office 2019 أو Office 365.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت ترغب في فصل قالب التصفية عن جدول المحور في إكسل، فيجب عليك النقر بزر الماوس الأيمن على قالب التصفية واختيار العنصر "اتصالات التقرير...". في قائمة الخيارات، يمكنك التحكم في مربع الاختيار. بالمثل، إذا كنت ترغب في فصل قالب التصفية عن جدول المحور باستخدام واجهة برمجية Aspose.Cells، يرجى استخدام الطريقة [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/). ستقوم بفصل قالب التصفية عن جدول المحور.

## **فصل قالب التصفية عن جدول المحور**

الكود العينة التالي يحمل [ملف إكسل عينة](remove-pivot-connection.xlsx) الذي يحتوي على قالب تصفية موجود. يدخل إلى قوالب التصفية ثم يفصل قالب التصفية عن جدول المحور. وأخيراً، يحفظ الدفتر ك [ملف إكسل الناتج](remove-pivot-connection-out.xlsx). 

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
