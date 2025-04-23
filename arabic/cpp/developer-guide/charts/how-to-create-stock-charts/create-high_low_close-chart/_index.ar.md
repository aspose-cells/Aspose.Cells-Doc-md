--- 
title: إنشاء رسم بياني لأسهم الأعلى والأدنى والإغلاق مع C++ 
linktitle: إنشاء رسم بياني لأسهم High Low Close (HLC) 
description: تعلم كيفية إنشاء رسم بياني لأسهم عالية ومنخفضة وإغلاق باستخدام Aspose.Cells for C++. دليلنا خطوة بخطوة سيعرض كيف يمكن رسم بيانات سوق الأسهم، بما في ذلك الأسعار العليا والمنخفضة والإغلاق، على رسم بياني لتحليل أفضل وتصوير البيانات. 
keywords: Aspose.Cells for C++، رسم بياني عالي ومنخفض وإغلاق الأسهم، بيانات سوق الأسهم، التحليل، التصور. 
type: docs 
weight: 181 
url: /ar/cpp/create-high-low-close-stock-chart/ 
--- 

## **سيناريوهات الاستخدام المحتملة** 
يستخدم مخطط الأسهم High-Low-Close (HLC) أربع أعمدة من البيانات. العمود الأول هو فئة، عادة تاريخ ولكن يمكن أيضًا استخدام أسماء الأسهم. الأعمدة الثلاثة التالية بالترتيب هي للأسعار المرتفعة، منخفضة، والإغلاق. يتم توضيح نطاق السعر لكل فئة بخط عمودي من الأدنى إلى الأعلى، ويتم عرض سعر الإغلاق باستخدام دبوس امتدادي لليمين من هذا الخط. 

![todo:image_alt_text](sample.png) 
## **تحسينات الرؤية في الرسم البياني** 
في بعض الأحيان، لجعل الرسم البياني يبدو أكثر تفاعلية، يمكننا تعديل مظهر العلامة (الإغلاق)، أو جعلها تظهر على المحور الثانوي. 

![todo:image_alt_text](sample2.png) 
## **الكود المثالي** 
الكود العينة التالي يحمل [ملف إكسل العينة](High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
