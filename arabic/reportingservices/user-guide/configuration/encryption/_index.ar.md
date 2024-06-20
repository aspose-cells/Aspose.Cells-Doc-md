---
title: التشفير
type: docs
weight: 40
url: /ar/reportingservices/encryption/
---

Aspose.Cells for Reporting Services يدعم ثلاثة أنواع من التشفير: XOR، تشفير ضعيف، و Microsoft Strong Cryptographic Provider. انظر معلومات تكوين التشفير في ملف **Aspose.Cells.ReportingServices.xml**.

عندما تكون قيمة التشفير **معطلة**, يقوم Aspose.Cells for Reporting Services بإيقاف ميزات التشفير.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

عندما تكون قيمة التشفير **مفعلة**, يقوم Aspose.Cells for Reporting Services بتشغيل التشفير.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

هناك أربعة معلمات في قسم التشفير:

- **اسم التقرير**: يشير إلى تقرير يحتاج إلى تشفير. إذا تم ترك المعلمة فارغة، فإن جميع التقارير تستخدم نفس طريقة التشفير.
- **كلمة المرور**: يحدد كلمة المرور. لا يمكن أن تكون فارغة.
- **نوع_التشفير**: يحدد نوع التشفير. لا يمكن أن يكون فارغًا.
- **طول_المفتاح**: يحدد طول المفتاح. لا يمكن أن يكون فارغًا.

{{< highlight java >}}

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
