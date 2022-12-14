---
title: تكوين التشفير
type: docs
weight: 40
url: /ar/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells لخدمات التقارير يدعم التشفير ويمكنك تقديم ملفات Excel Microsoft المشفرة.

{{% /alert %}} 
### **أنواع التشفير**
يدعم Aspose.Cells Reporting Services التشفير عند تصدير ملفات Excel. يدعم ثلاثة أنواع من التشفير:

- XOR
- ضعف التشفير
- Microsoft مزود تشفير قوي
### **تكوين المعلومات**
 توجد معلومات تكوين للتشفير في ملف**Aspose.Cells.ReportingServices.xml** ملف. عند تعيين قيمة Encryption (التشفير) على "off" ، تقوم Aspose.Cells.ReportingServices بإيقاف تشغيل التشفير.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

عند تعيين التشفير على "تشغيل" ، يقوم Aspose.Cells.ReportingServices بتشغيل التشفير.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

توجد أربع معلمات في قسم التشفير: ReportName وكلمة المرور و EncryptionType و KeyLength.

- ReportName - يعيّن التقرير الذي يحتاج إلى إعدادات التشفير. يستخدم التقرير نفس طريقة التشفير عندما تكون المعلمة فارغة.
- كلمة المرور - لتعيين كلمة المرور. لا يمكن تركه فارغًا.
- نوع التشفير - يحدد نوع التشفير. لا يمكن تركه فارغًا.
-  KeyLength - يضبط طول المفتاح. لا يمكن تركه فارغًا.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="on">

<Report name="Test" >

<Password value="12345"/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

<Report name="" >

<Password value="123456"/>

<EncryptionType value="XOR"/>

<KeyLength value="128"/>

</Report>

</Encryption>



{{< /highlight >}}
