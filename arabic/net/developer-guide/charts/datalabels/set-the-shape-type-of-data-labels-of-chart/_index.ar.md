---
title: تعيين نوع الشكل لتسميات بيانات الرسم البياني
description: تعلم كيفية تعيين نوع الشكل لتسميات بيانات في الرسوم البيانية باستخدام Aspose.Cells for .NET. سيشرح دليلنا أنواع الأشكال المختلفة المتاحة وسيظهر لك كيفية اختيار الشكل المناسب لتسميات بياناتك لتعزيز العرض التقديمي والاستخدامية لرسومك البيانية.
keywords: Aspose.Cells for .NET، الرسم البياني، تسميات البيانات، أنواع الأشكال، العرض التقديمي، الاستخدامية.
type: docs
weight: 110
url: /ar/net/set-the-shape-type-of-data-labels-of-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تغيير نوع الشكل لتسميات بيانات الرسم البياني باستخدام خاصية DataLabels.ShapeType. يأخذ قيمة تعداد DataLabelShapeType ويغير نوع الشكل لتسميات بيانات بناءً عليه. بعض قيمه هي

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **تعيين نوع الشكل لتسميات بيانات الرسم البياني**
الشيفرة النموذجية التالي تغيير نوع الشكل لتسميات بيانات الرسم البياني إلى DataLabelShapeType.WedgeEllipseCallout. يُرجى الاطلاع على [الملف النموذجي لـ Excel](60489778.xlsx) المستخدم في هذه الشفرة و [الملف الناتج لـ Excel](60489779.xlsx) الذي تم إنشاؤه بواسطته. يوضح لقطة الشاشة تأثير الشفرة على ملف Excel النموذجي. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
