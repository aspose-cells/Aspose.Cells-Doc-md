---
title: رسم بياني إلى PDF باستخدام C++
linktitle: تحويل الرسم البياني إلى PDF
description: تعلم كيفية استخدام Aspose.Cells for C++ لتحويل رسم بياني إلى مستند PDF. سيُظهر دليلنا كيفية تصدير رسم بياني من مايكرسوفت إكسل وحفظه كملف PDF للمزيد من التوزيع والأرشفة.
keywords: Aspose.Cells for C++، رسم بياني إلى PDF، مايكروسوفت إكسل، تحويل إلى PDF، تصدير، توزيع، أرشفة.
type: docs
weight: 47
url: /ar/cpp/chart-to-pdf/
---

## **عرض الرسم البياني إلى PDF**

من أجل عرض الرسم البياني بتنسيق PDF، قامت واجهات برمجة التطبيقات Aspose.Cells بكشف طريقة [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) مع القدرة على تخزين PDF الناتج على مسار القرص أو من خلال التدفق.

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

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إنشاء رسم بياني PDF بحجم الصفحة المطلوب**
يمكنك إنشاء PDF للرسم البياني بحجم الصفحة الذي تريده باستخدام Aspose.Cells وتحديد طريقة محاذاة الرسم داخل الصفحة كالأعلى، الأسفل، المنتصف، اليسار، اليمين، إلخ. بالإضافة إلى ذلك، يمكن إنشاء الرسم البياني الناتج في تدفق أو على القرص. يرجى الاطلاع على الكود النموذجي التالي الذي يحمل ملف إكسل العيني، ويصل إلى أول رسم بياني داخل ورقة العمل، ثم يحولها إلى PDF الناتج بحجم الصفحة المطلوب. تُظهر الصورة التالية أن حجم الصفحة في ملف PDF الناتج هو 7x7 كما هو محدد داخل الكود، وأن الرسم البياني محاذي في المنتصف أفقياً وعمودياً.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
