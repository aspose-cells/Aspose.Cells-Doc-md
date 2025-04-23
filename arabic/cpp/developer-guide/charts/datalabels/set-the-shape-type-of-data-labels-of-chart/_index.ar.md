---
title: ضبط نوع شكل تسميات البيانات في المخطط باستخدام ++C
linktitle: تعيين نوع الشكل لتسميات بيانات الرسم البياني
description: تعرف على كيفية ضبط نوع شكل تسميات البيانات في المخططات باستخدام Aspose.Cells for C++. سيشرح دليلنا أنواع الأشكال المتاحة ويوضح كيفية اختيار الشكل المناسب لتسميات البيانات الخاصة بك لتعزيز العرض وسهولة الاستخدام.
keywords: Aspose.Cells for C++، التخطيط، تسميات البيانات، أنواع الأشكال، العرض، سهولة الاستخدام.
type: docs
weight: 110
url: /ar/cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تغيير نوع شكل تسميات البيانات للمخطط باستخدام خاصية `DataLabels.ShapeType`. تأخذ قيمة تعدد الأشكال `DataLabelShapeType` وتغير نوع شكل تسميات البيانات وفقًا لذلك. بعض قيمها هي:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **تعيين نوع الشكل لتسميات بيانات الرسم البياني**
يعرض الكود النموذجي التالي تغيير نوع شكل تسميات البيانات على الرسم البياني إلى `DataLabelShapeType.WedgeEllipseCallout`. يرجى الاطلاع على ملف Excel النموذجي [الملف](60489778.xlsx) المستخدم في هذا الكود وملف Excel الناتج [الملف](60489779.xlsx) الذي تم إنشاؤه بواسطة الكود. يُظهر لقطة شاشة تأثير الكود على ملف Excel النموذجي. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    U16String inputFilePath = u"sampleSetShapeTypeOfDataLabelsOfChart.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Access first series
    Series srs = ch.GetNSeries().Get(0);

    // Set the shape type of data labels i.e. Speech Bubble Oval
    srs.GetDataLabels().SetShapeType(DataLabelShapeType::WedgeEllipseCallout);

    // Save the output Excel file
    U16String outputFilePath = u"outputSetShapeTypeOfDataLabelsOfChart.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Shape type of data labels set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
