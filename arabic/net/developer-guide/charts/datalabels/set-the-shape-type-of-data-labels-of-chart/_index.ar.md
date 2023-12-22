---
title: قم بتعيين نوع شكل تسميات البيانات للمخطط
description: تعرف على كيفية تعيين نوع شكل تسميات البيانات في المخططات باستخدام Aspose.Cells for .NET. سيشرح دليلنا أنواع الأشكال المختلفة المتاحة ويوضح لك كيفية اختيار الشكل المناسب لتسميات البيانات الخاصة بك لتحسين عرض المخططات وسهولة استخدامها.
keywords: Aspose.Cells for .NET, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /ar/net/set-the-shape-type-of-data-labels-of-chart/
---
##  **سيناريوهات الاستخدام المحتملة**
يمكنك تغيير نوع شكل تسميات البيانات الخاصة بالمخطط باستخدام الخاصية DataLabels.ShapeType. فهو يأخذ قيمة تعداد DataLabelShapeType ويغير نوع شكل تسميات البيانات وفقًا لذلك. بعض قيمها هي

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
##  **قم بتعيين نوع شكل تسميات البيانات للمخطط**
 يقوم نموذج التعليمات البرمجية التالي بتغيير نوع شكل تسميات بيانات المخطط إلى DataLabelShapeType.WedgeEllipseCallout. الرجاء مراجعة[عينة من ملف إكسل](60489778.xlsx) المستخدمة في هذا الرمز و[إخراج ملف إكسل](60489779.xlsx)المتولدة عنها. توضح لقطة الشاشة تأثير الكود على نموذج ملف Excel.

![ما يجب القيام به:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
