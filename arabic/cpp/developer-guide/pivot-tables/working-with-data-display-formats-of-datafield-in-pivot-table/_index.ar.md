---
title: العمل مع تنسيقات عرض البيانات لحقل البيانات في Pivot Table باستخدام C++
linktitle: العمل مع تنسيقات عرض البيانات لحقل البيانات في Pivot Table
type: docs
weight: 140
url: /ar/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: تعلم كيفية العمل مع تنسيقات عرض البيانات لحقل البيانات في Pivot Table باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells جميع تنسيقات عرض البيانات لحقل البيانات.

{{% /alert %}}

## **خيار تنسيق العرض "ترتيب الأصغر إلى الأكبر" و"ترتيب الأكبر إلى الأصغر"**

يوفر Aspose.Cells القدرة على تعيين خيار تنسيق العرض لحقول pivot. لهذا، يوفر API الخاص بـ [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) الخاصية. لترتيب الأكبر إلى الأصغر، يمكنك ضبط الخاصية [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) إلى [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). يوضح مقتطف الكود التالي إعداد خيارات تنسيق العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف إكسل المصدر](101089332.xlsx)

[ملف إكسل الإخراج](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
