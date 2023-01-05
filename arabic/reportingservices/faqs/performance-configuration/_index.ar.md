---
title: تكوين الأداء
type: docs
weight: 20
url: /ar/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

 يمكن للمستخدمين تحسين الأداء إلى حد معين. يمكنك تكوين بعض السمات والمعلمات في ملف**Aspose.Cells.ReportingServices.xml** ملف كما هو موضح أدناه.

{{% /alert %}} 
### **قسم الأداء**
يعرض هذا قسم الأداء كما هو افتراضيًا.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}
### **معايير الأداء**
-  LimitCellsNumberForMerged - القيمة الافتراضية للمعامل هي 1000000. يتم تعيين قيمة المعلمة بواسطة العميل ولا تتأثر بمبدِّل معلمة الأداء. يرجى الرجوع إلى التكوين التالي.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit - يمكن أن يكون صوابًا أو خطأً:
 - عند ضبط معلمة الأداء على "إيقاف" ، تكون القيمة الافتراضية هي "خطأ".
 - عند ضبط معلمة الأداء على "تشغيل" ، تكون القيمة الافتراضية صحيحة.
 - عند تعيين معلمة الأداء على "تشغيل" ، يمكن لتقرير عنصر فرعي إعادة تعيين معلمة AutoRowFile للتقرير.
يرجى الرجوع إلى التكوين التالي.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    	<Report name="Test">

      	<AutoRowFit value="False"/>

      	<SetStyle value="True"/>

      	<Merged value="True"/>

      	<ConditionalFormatting value="True"/>

      	</Report>

</Performance>



{{< /highlight >}}

-  IsMerged - يمكن أن يكون صحيحًا أو خطأ:
 - عند ضبط معلمة الأداء على "إيقاف" ، تكون القيمة الافتراضية هي "خطأ".
 - عند ضبط معلمة الأداء على "تشغيل" ، تكون القيمة الافتراضية صحيحة.
 - عند تعيين معلمة الأداء على "تشغيل" ، يمكن لتقرير عنصر فرعي إعادة تعيين معلمة AutoRowFile للتقرير.
يرجى الرجوع إلى التكوين التالي.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

-  IsSetStyle - يمكن أن يكون إما صوابًا أو خطأً:
 - عند ضبط معلمة الأداء على "إيقاف" ، تكون القيمة الافتراضية هي "خطأ".
 - عند ضبط معلمة الأداء على "تشغيل" ، تكون القيمة الافتراضية صحيحة.
 - عند تعيين معلمة الأداء على "تشغيل" ، يمكن لتقرير عنصر فرعي إعادة تعيين معلمة AutoRowFile للتقرير.
يرجى الرجوع إلى التكوين التالي.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

-  IsConditionalFormatting - يمكن أن يكون إما صحيحًا أو خطأ:
 - عند ضبط معلمة الأداء على "إيقاف" ، تكون القيمة الافتراضية هي "خطأ".
 - عند ضبط معلمة الأداء على "تشغيل" ، تكون القيمة الافتراضية صحيحة.
 - عند تعيين معلمة الأداء على "تشغيل" ، يمكن لتقرير العنصر الفرعي إعادة تعيين معلمة AutoRowFile لتقرير النقاط.
 - عند تعيين معلمة IsSetStyle على خطأ ، تكون قيمة معلمة الأداء غير صالحة.
يرجى الرجوع إلى التكوين التالي.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

</Performance>



{{< /highlight >}}
