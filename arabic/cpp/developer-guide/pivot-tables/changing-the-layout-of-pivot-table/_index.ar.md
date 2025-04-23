---
title: تغيير تخطيط الجدول المحوري باستخدام C++
linktitle: تغيير تخطيط جدول الدوران
type: docs
weight: 10
url: /ar/cpp/changing-the-layout-of-pivot-table/
description: تعلم كيفية تغيير تخطيط الجدول المحوري في الأشكال المدمجة والخطية والجدولية باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تغيير تخطيط الجدول المحوري باستخدام قائمة *PivotTable Tools > Design > Report Layout*. يمكنك تغيير التخطيط بهذه الأشكال الثلاثة:

إظهار بتنسيق مضغوط
إظهار بتنسيق مخطط
إظهار بتنسيق جدولي

توفر Aspose.Cells أيضًا [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/) و [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/) و [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) لطرق تغيير تخطيط الجدول المحوري بهذه الأشكال الثلاثة.

{{% /alert %}}

يُظهر رمز النموذج التالي أولاً الجدول المحوري في **الشكل المدمج**، ثم يظهر الجدول في **الشكل الخارجي**، وأخيرًا، يُعرض الجدول في **الشكل الجدولي**.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_sample.xlsx";

    // Create workbook object from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 1 - Show the pivot table in compact form
    pivotTable.ShowInCompactForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"CompactForm_out.xlsx");

    // 2 - Show the pivot table in outline form
    pivotTable.ShowInOutlineForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"OutlineForm_out.xlsx");

    // 3 - Show the pivot table in tabular form
    pivotTable.ShowInTabularForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"TabularForm_out.xlsx");

    std::cout << "Pivot table forms saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
