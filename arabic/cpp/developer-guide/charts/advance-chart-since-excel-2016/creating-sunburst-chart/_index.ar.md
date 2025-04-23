---
title: كيفية إنشاء رسم بياني لنجم الشمش باستخدام C++
description: تعلم كيفية إنشاء رسم بياني لنجم الشمس في Aspose.Cells for C++، وهو رسم بياني يعرض البيانات في دائرة. سيساعدك دليلنا على إعداد خصائص وتنسيقات متنوعة للرسم البياني الخاص بك، بما في ذلك تسميات البيانات، الأساطير، الألوان والمزيد.
keywords: Aspose.Cells for C++، رسم بياني لنجم الشمس، إنشاء، تعيين الخصائص، تسميات البيانات، الأسطورة، التنسيق، اللون، الدائرة، عرض البيانات.
type: docs
weight: 162
url: /ar/cpp/creating-sunburst-chart/
---

## **سيناريوهات الاستخدام المحتملة**
رسوم خرائط الأشجار جيدة للمقارنة بين النسب داخل الهرمية، ومع ذلك، رسوم خرائط الأشجار ليست جيدة في إظهار المستويات الهرمية بين أكبر الفئات وكل نقطة بيانات. رسم نجم الشمس هو رسم بياني بصري أفضل لذلك. الرسم النجم هو مثالي لعرض البيانات الهرمية. يُمثل كل مستوى من الهرمية بواسطة حلقة أو دائرة واحدة مع أدنى دائرة على مستوى أعلى الهرمية. يظهر رسم نجم الشمس بدون بيانات هرمية (مستوى واحد من الفئات) مشابهًا لرسمة الدونات. ومع ذلك، يُظهر رسم نجم الشمس متعدد المستويات كيف ترتبط الحلقات الخارجية بالحلقات الداخلية. يُعد رسم نجم الشمس الأكثر فاعلية في إظهار كيف يتم تقسيم حلقة واحدة إلى أجزائها المساهم، بينما يُعد نوع آخر من الرسوم الهرمية، وهو رسم خرائط الأشجار، مثاليًا للمقارنة بين الأحجام النسبية.

![todo:image_alt_text](sample.png)
## **رسم بياني للتفجير الشمسي**
بعد تشغيل الكود أدناه، سترون رسم بياني للتفجير الشمسي كما هو موضح أدناه.

![todo:image_alt_text](result.png)
## **الكود المثالي**
الكود المثالي التالي يحمل [ملف Excel العيني](sunburst.xlsx) ويُولّد [ملف Excel الإخراج](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
