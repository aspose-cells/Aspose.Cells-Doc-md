---
title: تكوين التشفير
type: docs
weight: 40
url: /ar/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

 تدعم Aspose.Cells for Reporting Services التشفير ويمكنك عرض ملفات Microsoft Excel المشفرة. 

{{% /alert %}} 
### **أنواع التشفير**
تدعم Aspose.Cells for Reporting Services التشفير عند تصدير ملفات Excel. تدعم ثلاثة أنواع للتشفير:

- XOR
- تشفير ضعيف (WEAK ENCRYPTION)
- مزود التشفير القوي لمايكروسوفت
### **تكوين المعلومات**
هناك معلومات تكوين للتشفير في ملف **Aspose.Cells.ReportingServices.xml**. عندما يتم ضبط قيمة التشفير على "إيقاف", يقوم Aspose.Cells.ReportingServices بإيقاف التشفير.

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

عند تعيين التشفير على "تشغيل", يقوم Aspose.Cells.ReportingServices بتشغيل التشفير.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

هناك أربعة معلمات في قسم التشفير: اسم التقرير، كلمة المرور، نوع التشفير وطول المفتاح.

- اسم التقرير – يضبط التقرير الذي يحتاج إلى إعدادات التشفير. يستخدم التقرير نفس طريقة التشفير عندما يكون المعلمة فارغة.
- كلمة المرور – يضبط كلمة المرور. لا يمكن تركها فارغة.
- نوع التشفير – يضبط نوع التشفير. لا يمكن تركه فارغاً.
- طول المفتاح – يضبط طول المفتاح. لا يمكن تركه فارغاً. 

**XML**

{{< highlight csharp >}}

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
