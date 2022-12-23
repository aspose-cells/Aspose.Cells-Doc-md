---
title: تقديم عناصر المخطط المحدد إلى مخططات Excel
type: docs
weight: 30
url: /ar/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

لعرض بعض المخططات فقط في تقرير إلى مخططات Excel:

1. افتح ال**Aspose.Cells.ReportingServices.xml** ملف.
1.  قم بتعديل معلمات التكوين الخاصة بـ**Aspose.Cells.ReportingServices.xml** ملف.
1. أضف معلومات تكوين التقرير المطلوب.
1. أضف المعلومات الخاصة بعناصر المخطط التي لا تريد تصديرها كمخططات قابلة للتحرير. يتم تصدير هذه العناصر كصور ثابتة.

على سبيل المثال:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**مخطط تم تصديره كصورة** 

![ما يجب القيام به: image_بديل_نص](render-selected-chart-items-to-excel-charts_1.png)

**مخطط تم تصديره كمخطط Excel قابل للتحرير** 

![ما يجب القيام به: image_بديل_نص](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
