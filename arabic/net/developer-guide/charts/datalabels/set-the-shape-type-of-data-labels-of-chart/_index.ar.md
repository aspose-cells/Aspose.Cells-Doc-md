---
title: قم بتعيين نوع شكل تسميات البيانات للمخطط
type: docs
weight: 110
url: /ar/net/set-the-shape-type-of-data-labels-of-chart/
---
## **سيناريوهات الاستخدام الممكنة**
يمكنك تغيير نوع شكل تسميات البيانات للمخطط باستخدام الخاصية DataLabels.ShapeType. يأخذ قيمة تعداد DataLabelShapeType ويغير نوع شكل تسميات البيانات وفقًا لذلك. بعض قيمها

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **قم بتعيين نوع شكل تسميات البيانات للمخطط**
 يغير نموذج التعليمات البرمجية التالي نوع شكل تسميات البيانات في المخطط إلى DataLabelShapeType.WedgeEllipseCallout. الرجاء مراجعة[نموذج لملف Excel](60489778.xlsx) المستخدمة في هذا الرمز و[إخراج ملف Excel](60489779.xlsx) ولدت به. تُظهر لقطة الشاشة تأثير الكود على نموذج ملف Excel.

![ما يجب القيام به: image_بديل_نص](set-the-shape-type-of-data-labels-of-chart_1.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
