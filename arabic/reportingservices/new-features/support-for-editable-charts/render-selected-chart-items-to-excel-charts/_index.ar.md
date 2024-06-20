---
title: عرض عناصر الرسم البياني المحددة كمخططات Excel
type: docs
weight: 30
url: /ar/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

لعرض بعض الرسوم البيانية فقط في تقرير إلى مخططات Excel:

1. افتح ملف **Aspose.Cells.ReportingServices.xml**.
1. قم بتعديل معلمات التكوين في ملف **Aspose.Cells.ReportingServices.xml**.
1. أضف معلومات تكوين التقرير المرغوبة.
1. أضف المعلومات لعناصر الرسم البياني التي لا ترغب في تصديرها كرسوم بيانية قابلة للتحرير. يتم تصدير هذه العناصر كصور ثابتة.

على سبيل المثال:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**رسم بياني يتم تصديره كصورة** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**رسم بياني يتم تصديره كرسم بياني قابل للتحرير في Excel** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
