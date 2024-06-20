---
title: دعم التواقيع الرقمية
type: docs
weight: 70
url: /ar/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

توفر التوقيع الرقمي ضمانًا بأن دفتر العمل صالح ولم يقم أحد بتعديله. إرفاق التوقيع الرقمي مماثل لختم مظروف. إذا وصل مظروف مختوم، فلديك بعض مستوى الثقة بأن لا أحد قام بالتلاعب بمحتوياته. 

يمكنك إنشاء توقيع رقمي شخصي باستخدام Microsoft Selfcert.exe أو أي أداة أخرى، أو يمكنك شراء توقيع رقمي. لتوقيع جداول البيانات، قم بإرفاق توقيع بأعمالك بمجرد إنشاء توقيع رقمي. 

يدعم Aspose.Cells for Reporting Services التواقيع الرقمية. 

{{% /alert %}} 
### **العمل مع التواقيع الرقمية**
#### **تنسيقات Excel المدعومة للتواقيع الرقمية**
يدعم Aspose.Cells for Reporting Services التواقيع الرقمية عند التصدير إلى تنسيقات Excel 2007 وملفات ODS.
#### **تكوين التواقيع الرقمية**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- عندما يتم تعيين DigitalSignature إلى off، يقوم Aspose.Cells for Reporting Services بإيقاف وظائف التوقيع الرقمي.
  على سبيل المثال: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- عندما يكون قيمة DigitalSignature مفعلة، يقوم Aspose.Cells.ReportingServices بتفعيل وظائف التوقيع الرقمي.
  على سبيل المثال: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

هناك أربعة معلمات في قسم DigitalSignature. هذه هي: 

- name - يشير إلى تقرير يحتاج إلى توقيع رقمي. يستخدم التقرير ملف PFX للتوقيع الرقمي عندما يكون المعلمة فارغة.
- pfxFilename - يشير إلى ملف PFX. يجب أن يكون اسم الملف اسم ملف كامل. لا يمكن تعيين قيمة فارغة.
- pfxPwd - يحدد كلمة المرور. لا يمكن تركها فارغة.
- الغرض - يشرح الغرض من التوقيع. يمكن أن يكون فارغًا.
  على سبيل المثال: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
