---
title: تعيين خيار جدول Pivot  لعرض الخلايا الفارغة مع C++
linktitle: ضبط خيار جدول الدوري  إظهار الخلايا الفارغة
type: docs
weight: 40
url: /ar/cpp/setting-pivot-table-option-for-empty-cells-show/
description: تعلم كيفية تعيين خيار "لعرض الخلايا الفارغة" في جداول Pivot باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يمكنك ضبط خيارات جدول الجدول المحوري المختلفة باستخدام Aspose.Cells. خيار واحد هو "عرض الخلايا الفارغة". من خلال ضبط هذا الخيار، يتم عرض جميع الخلايا الفارغة في جدول الجدول المحوري بصورة سلسلة محددة.

{{% /alert %}}

## **ضبط خيار جدول الجدول المحوري في Microsoft Excel**

للعثور على هذا الخيار وضبطه في Microsoft Excel:

1. حدد جدول الجدول المحوري وانقر بزر الماوس الأيمن.
1. حدد **خيارات الجدول الدوري**.
1. حدد علامة التبويب **التخطيط والشكل**.
1. حدد خيار **إظهار الخلايا الفارغة** وحدد سلسلة.

## **ضبط خيار جدول الجدول المحوري باستخدام Aspose.Cells**

توفر Aspose.Cells الخصائص [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) و [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) لضبط خيار جدول الجدول المحوري "عرض الخلايا الفارغة".

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## مقالات ذات صلة

- [تنسيق جدول الجدول المحوري](/cells/ar/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
