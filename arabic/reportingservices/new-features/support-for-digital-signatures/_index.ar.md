---
title: دعم التواقيع الرقمية
type: docs
weight: 70
url: /ar/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

 يوفر التوقيع الرقمي ضمانًا بأن المصنف صالح ولم يغيره أحد. يشبه إرفاق التوقيع الرقمي ختم الظرف. إذا وصل مغلف مغلقًا ، فلديك بعض التأكيد على أنه لم يعبث أحد بمحتوياته.

 يمكنك إنشاء توقيع رقمي شخصي باستخدام Microsoft Selfcert.exe أو أي أداة أخرى ، أو يمكنك شراء توقيع رقمي. لتوقيع جدول بيانات ، قم بإرفاق توقيع بمصنفاتك بمجرد إنشاء توقيع رقمي.

 يدعم Aspose.Cells Reporting Services التواقيع الرقمية.

{{% /alert %}} 
### **العمل مع التوقيعات الرقمية**
#### **تنسيقات Excel المدعومة للتوقيعات الرقمية**
Aspose.Cells لخدمات التقارير يدعم التواقيع الرقمية عند التصدير إلى تنسيقات ملفات Excel 2007 و ODS.
#### **تكوين التوقيعات الرقمية**
 ال**Aspose.Cells.ReportingServices.xml** يحتوي الملف على معلومات التكوين ونص التوقيع الرقمي في ملف<DigitalSignature> بطاقة شعار:

- عند ضبط DigitalSignature على إيقاف التشغيل ، يقوم Aspose.Cells لـ Reporting Services بإيقاف تشغيل وظيفة التوقيع الرقمي.
 فمثلا:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- عندما تكون قيمة التوقيع الرقمي قيد التشغيل ، تقوم Aspose.Cells.ReportingServices بتشغيل وظيفة التوقيع الرقمي.
 فمثلا:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 هناك أربعة معلمات في قسم التوقيع الرقمي. هؤلاء هم :

- الاسم - يشير إلى تقرير يحتاج إلى توقيع رقمي. يستخدم التقرير ملف PFX للتوقيع الرقمي عندما تكون المعلمة فارغة.
- pfxFilename - يشير إلى ملف PFX. يجب أن يكون اسم الملف اسم ملف كامل. لا يمكن تعيينه على قيمة فارغة.
- pfxPwd - يضبط كلمة المرور. لا يمكن تركه فارغًا.
- الغرض - يشرح الغرض من التوقيع. يمكن أن تكون فارغة.
 فمثلا:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
