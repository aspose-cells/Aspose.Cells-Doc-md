---
title: التوقيعات الرقمية
type: docs
weight: 50
url: /ar/reportingservices/digital-signatures/
---
 Aspose.Cells لخدمات التقارير يدعم التواقيع الرقمية عند تصدير Microsoft ملفات Excel 2007 أو ملفات ODS. لدينا بعض معلومات التكوين للتوقيعات الرقمية التي يمكن تعيينها في ملف**Aspose.Cells.ReportingServices.xml** ملف.

 عندما تكون قيمة التوقيع الرقمي**إيقاف**، Aspose.Cells لخدمات التقارير يقوم بإيقاف تشغيل التواقيع الرقمية.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 عندما تكون قيمة التوقيع الرقمي**على**، Aspose.Cells لخدمات التقارير يقوم بتشغيل التواقيع الرقمية.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 هناك أربعة معلمات في قسم التوقيع الرقمي. هؤلاء هم:

- **اسم**يمثل تقريرًا يحتاج إلى توقيع رقمي. عندما تُترك المعلمة فارغة ، تستخدم التقارير ملف PFX للتوقيعات الرقمية.
- **pfx اسم الملف**: يشير إلى ملف PFX. يجب أن يكون اسم الملف اسم ملف مؤهلًا بالكامل ، مكتملًا بالمسار وامتداد الملف. يجب ألا يكون فارغًا.
- **pfxPwd**: يحدد كلمة المرور. يجب ألا يكون فارغًا.
- **غاية**: وصف ما إذا كان التوقيع ل. يمكن أن تكون فارغة.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
