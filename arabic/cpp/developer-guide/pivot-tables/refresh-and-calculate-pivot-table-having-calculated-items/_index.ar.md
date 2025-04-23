---
title: تحديث وحساب جدول Pivot الذي يحتوي على عناصر محسوبة باستخدام C++
linktitle: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: تحديث وحساب جدول Pivot مع عناصر محسوبة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells الآن تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) و [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

يحمّل الكود النموذجي التالي ملف إكسل المصدر والذي يحتوي على جدول محوري به ثلاثة عناصر محسوبة مثل "إضافة"، "قسمة"، "قسمة2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب الجدول المحوري باستخدام واجهات برمجة التطبيقات من Aspose.Cells وحفظ الملف بصيغة PDF. تظهر النتائج في ملف PDF المخرجات أن Aspose.Cells قام بتحديث وحساب الجدول المحوري بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel يدويًا بوضع القيمة 20 في الخلية D2 ثم تحديث الجدول المحوري بواسطة مفتاح الاختصار Alt+F5 أو النقر على زر تحديث الجدول المحوري.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
