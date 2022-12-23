---
title: التشفير
type: docs
weight: 40
url: /ar/reportingservices/encryption/
---
Aspose.Cells for Reporting Services يدعم ثلاثة أنواع من التشفير: XOR و WEAK ENCRYPTION و Microsoft مزود تشفير قوي. راجع معلومات تكوين التشفير في ملف**Aspose.Cells.ReportingServices.xml** ملف.

 عندما تكون قيمة التشفير**إيقاف**، Aspose.Cells for Reporting Services يقوم بإيقاف تشغيل ميزات التشفير.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 عندما تكون قيمة التشفير**تشغيل**، Aspose.Cells for Reporting Services يقوم بتشغيل التشفير.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

هناك أربع معاملات في قسم التشفير:

- **تقرير اسم**: يشير إلى تقرير يحتاج إلى تشفير. إذا تُركت المعلمة فارغة ، فإن جميع التقارير تستخدم نفس طريقة التشفير.
- **كلمة المرور**: يحدد كلمة المرور. لا يمكن أن يكون فارغا.
- **نوع التشفير**: يحدد نوع التشفير. لا يمكن أن يكون فارغا.
- **طول المفتاح**: يحدد طول المفتاح. لا يمكن أن يكون فارغا.

{{< highlight "java" >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
