---
title: إدارة عناوين الرسوم البيانية في إكسل باستخدام C++
linktitle: العناوين
description: تعلم كيفية استخدام Aspose.Cells for C++ لإضافة وتنسيق عناوين الرسوم البيانية ومحاورها في مايكرسوفت إكسل. سيُظهر دليلنا كيفية تعيين أنواع مختلفة من العناوين، وتعديل مظهرها، وتغيير عناوين المحاور لتحسين تمثيل البيانات ووضوحها.
keywords: Aspose.Cells for C++، عناوين الرسوم البيانية، عناوين المحاور، مايكرسوفت إكسل، تمثيل البيانات، المظهر.
type: docs
weight: 50
url: /ar/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

في رسوم بيانية Excel، هناك نوعان من العناوين:
1. عنوان الرسم البياني 
1. عناوين المحاور

{{% /alert %}}

## **خيارات العنوان**
كما يسمح Aspose.Cells أيضًا بإدارة عناوين الرسوم البيانية في وقت التشغيل. مع كائن [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/)، يمكنك تغيير النص، الخط، وتنسيق التعبئة للعناوين.

|![todo:image_alt_text](chart_title.png)|

## **ضبط عناوين الرسوم البيانية أو المحاور**
يمكنك استخدام مايكرسوفت إكسل لتعيين عناوين رسم بياني ومحاورها في بيئة WYSIWYG. كما تسمح Aspose.Cells للمطورين بضبط عناوين رسوماتهم ومحاورها أثناء التشغيل. تحتوي كل الرسوم البيانية ومحاورها على خاصية [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) التي يمكن استخدامها لتعيين عناوينها، كما هو موضح في المثال أدناه.

يعرض مقطع الكود التالي كيفية تعيين عناوين للمخططات والمحاور.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [قراءة عنوان الرسم البياني من ملف ODS](/cells/ar/cpp/read-chart-subtitle-from-ods-file/)
