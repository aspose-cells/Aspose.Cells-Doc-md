---
title: تخصيص المخططات باستخدام ++C
linktitle: تخصيص المخططات
description: تعلم كيفية تخصيص المخططات في Aspose.Cells for C++. سيُظهر لك دليلنا كيفية تعديل تخطيطات المخطط، وإضافة وتنسيق سلاسل البيانات، وضبط المحاور، وتطبيق خيارات تنسيق متنوعة لتحسين مظهر واستخدام المخططات الخاصة بك.
keywords: Aspose.Cells for C++، رسم المخططات، التخصيص، التخطيطات، سلاسل البيانات، المحاور، التنسيق، المظهر، قابلية الاستخدام.
type: docs
weight: 40
url: /ar/cpp/customizing-charts/
---

## **إنشاء مخططات مخصصة**

حتى الآن، عندما ناقشنا المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات تنسيقها القياسية. نحن فقط نحدد مصدر البيانات، نضبط بعض الخاصيات، ويتم إنشاء المخطط بإعداداته الافتراضية. لكن API الخاصة بـ Aspose.Cells تدعم أيضًا إنشاء مخططات مخصصة تتيح للمطورين إنشاء مخططات بإعداداتهم الخاصة.

يمكن للمطورين إنشاء مخططات مخصصة أثناء التشغيل باستخدام Aspose.Cells.

يتألف المخطط من سلاسل بيانات. يُمثل كل سلسلة بيانات في Aspose.Cells بواسطة [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) كائن في حين تعمل كائن [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) كمجموعة لأشياء [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/). عند إنشاء مخطط مخصص، يحظى المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل بيانات مختلفة (التي تم جمعها في الكائن [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

حالياً، يدعم Aspose.Cells فقط المخططات المخصصة التي تجمع بين مخططات الفطيرة، والخط، والعمود، والتكديس العمودي، ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية.

{{% /alert %}}
