---
title: تعيين نوع الشكل لتسميات بيانات الرسم البياني
description: تعرف على كيفية تعيين نوع شكل علامات البيانات في المخططات باستخدام Aspose.Cells for Python via .NET. سيرينا دليلنا أنواع الأشكال المختلفة المتاحة وكيفية اختيار الشكل المناسب لعلامات البيانات لتعزيز العرض والاستخدامية.
keywords: Aspose.Cells for Python via .NET، مخططات، علامات البيانات، أنواع الأشكال، العرض، الاستخدامية.
type: docs
weight: 110
url: /ar/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تغيير نوع الشكل لتسميات بيانات الرسم البياني باستخدام خاصية DataLabels.ShapeType. يأخذ قيمة تعداد DataLabelShapeType ويغير نوع الشكل لتسميات بيانات بناءً عليه. بعض قيمه هي

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **تعيين نوع الشكل لتسميات بيانات الرسم البياني**
الشيفرة النموذجية التالي تغيير نوع الشكل لتسميات بيانات الرسم البياني إلى DataLabelShapeType.WedgeEllipseCallout. يُرجى الاطلاع على [الملف النموذجي لـ Excel](60489778.xlsx) المستخدم في هذه الشفرة و [الملف الناتج لـ Excel](60489779.xlsx) الذي تم إنشاؤه بواسطته. يوضح لقطة الشاشة تأثير الشفرة على ملف Excel النموذجي. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
