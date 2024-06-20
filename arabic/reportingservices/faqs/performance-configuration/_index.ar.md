---
title: تكوين الأداء
type: docs
weight: 20
url: /ar/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

يمكن للمستخدمين تحسين الأداء إلى حد معين. يمكنك تكوين بعض السمات والمعلمات في ملف **Aspose.Cells.ReportingServices.xml** كما هو موضح أدناه.

{{% /alert %}} 
### **القسم الأداء**
يظهر قسم الأداء كما هو افتراضيًا.

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}
### **معلمات الأداء**
- LimitCellsNumberForMerged – القيمة الافتراضية للمعلمة هي 1000000. تتم ضبط قيمة المعلمة من قبل العميل ولا تتأثر بمفتاح المعلمة الأداء. يرجى الرجوع إلى التكوين التالي. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – يمكن أن يكون إما صحيحًا أو خاطئًا: 
  - عند تعيين معلمة الأداء على 'إيقاف'، القيمة الافتراضية هي خاطئة.
  - عند تعيين معلمة الأداء على 'تشغيل'، القيمة الافتراضية هي صحيحة.
  - عند تعيين معلمة الأداء على 'تشغيل'، يمكن لتقرير العنصر الفرعي إعادة ضبط معلمة AutoRowFile التقرير.
    يرجى الإشارة إلى التكوين التالي. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    	<Report name="Test">

      	<AutoRowFit value="False"/>

      	<SetStyle value="True"/>

      	<Merged value="True"/>

      	<ConditionalFormatting value="True"/>

      	</Report>

</Performance>



{{< /highlight >}}

- هل تم دمجه - يمكن أن يكون إما صحيحًا أو خاطئًا: 
  - عند تعيين معلمة الأداء على 'إيقاف'، القيمة الافتراضية هي خاطئة.
  - عند تعيين معلمة الأداء على 'تشغيل'، القيمة الافتراضية هي صحيحة.
  - عند تعيين معلمة الأداء على 'تشغيل'، يمكن لتقرير العنصر الفرعي إعادة ضبط معلمة AutoRowFile التقرير.
    يرجى الإشارة إلى التكوين التالي. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

- هل تم تعيين النمط - يمكن أن يكون إما صحيحًا أو خاطئًا: 
  - عند تعيين معلمة الأداء على 'إيقاف'، القيمة الافتراضية هي خاطئة.
  - عند تعيين معلمة الأداء على 'تشغيل'، القيمة الافتراضية هي صحيحة.
  - عند تعيين معلمة الأداء على 'تشغيل'، يمكن لتقرير العنصر الفرعي إعادة ضبط معلمة AutoRowFile التقرير.
    يرجى الإشارة إلى التكوين التالي. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

- هل التنسيق الشرطي - يمكن أن يكون إما صحيحًا أو خاطئًا: 
  - عند تعيين معلمة الأداء على 'إيقاف'، القيمة الافتراضية هي خاطئة.
  - عند تعيين معلمة الأداء على 'تشغيل'، القيمة الافتراضية هي صحيحة.
  - عند تعيين معلمة الأداء على 'تشغيل'، يمكن لتقرير العنصر الفرعي إعادة ضبط معلمة AutoRowFile التقرير.
  - عند تعيين معلمة IsSetStyle على القيمة خاطئة، فإن قيمة المعلمة الأداء غير صالحة.
    يرجى الإشارة إلى التكوين التالي. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

</Performance>



{{< /highlight >}}
