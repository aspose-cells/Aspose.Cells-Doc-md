---  
title: كيفية إنشاء رسم بياني مدمج باستخدام C++  
linktitle: كيفية إنشاء رسم بياني مختلط  
description: تعلم كيفية إنشاء رسم بياني مدمج باستخدام Aspose.Cells for C++. ستوضح دليلك الشامل كيفية دمج أنواع مختلفة من الرسوم البيانية في رسم بياني مدمج واحد لعرض بيانات أكثر فعالية.  
keywords: Aspose.Cells for C++، رسم بياني مدمج، دمج أنواع الرسوم البيانية، عرض البيانات، التصوير البياني الفعال.  
type: docs  
weight: 73  
url: /ar/cpp/create-combo-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**  
تتيح لك رسوم الكومبو في Excel الاستفادة من هذا الخيار لأنك يمكنك دمج نوعين أو أكثر من أنواع الرسوم البيانية بسهولة لجعل بياناتك مفهومة. تكون رسوم الكومبو مفيدة عندما تحتوي بياناتك على أنواع متعددة من القيم بما في ذلك السعر والحجم. علاوة على ذلك، تكون رسوم الكومبو ممكنة عندما تتغير أرقام بياناتك بشكل واسع من سلسلة إلى سلسلة.  


![todo:image_alt_text](sample.png)  
## **رسم بياني مختلط**  
بعد تشغيل الرمز أدناه، سترون الرسم البياني المختلط كما هو موضح أدناه.  

![todo:image_alt_text](result.png)  
## **الكود المثالي**  
يقوم الرمز العيني التالي بتحميل [ملف Excel العيني] التالي(combo.xlsx) وإنتاج [ملف Excel الإخراج المعني] التالي(out.xlsx).  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook
    Workbook workbook(u"combo.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a stock volume (VHLC) chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 15, 0, 34, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title
    chart.GetTitle().SetText(u"Combo Chart");

    // Set the Legend position to bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E12", true);

    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A12";

    // Set the Series[1], Series[2], and Series[3] to different Marker Styles
    for (int32_t j = 0; j < chart.GetNSeries().GetCount(); j++)
    {
        switch (j)
        {
            case 1:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Circle);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Pink());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 2:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Orange());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 3:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Square);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::LightBlue());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
        }
    }

    // Set the chart type for Series[0]
    chart.GetNSeries().Get(0).SetType(ChartType::Line);

    // Set style for the border of the first series
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Solid);

    // Set color for the first series
    chart.GetNSeries().Get(0).GetBorder().SetColor(Color::DarkBlue());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
