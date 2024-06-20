---
title: التوقيعات الرقمية
type: docs
weight: 50
url: /ar/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services يدعم التوقيعات الرقمية عند تصدير ملفات Microsoft Excel 2007 أو ODS. لدينا بعض المعلومات حول تكوين التوقيعات الرقمية التي يمكن تعيينها في ملف **Aspose.Cells.ReportingServices.xml**.

عندما تكون قيمة التوقيع الرقمي **معطلة**, يقوم Aspose.Cells for Reporting Services بإيقاف التوقيعات الرقمية.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

عندما تكون قيمة التوقيع الرقمي **مفعلة**, يقوم Aspose.Cells for Reporting Services بتشغيل التوقيعات الرقمية.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

هناك أربعة معلمات في قسم التوقيع الرقمي. هذه هي: 

- **الاسم**: يمثل تقريرًا يحتاج إلى توقيع رقمي. عند ترك المعلمة فارغة، يستخدم التقارير ملف PFX للتوقيعات الرقمية.
- **pfxFilename**: يشير إلى ملف PFX. يجب أن يكون اسم الملف اسم مؤهل بالكامل، مع المسار وامتداد الملف. يجب ألا يكون فارغًا.
- **pfxPwd**: يحدد كلمة المرور. يجب ألا يكون فارغًا.
- **الغرض**: وصف لغرض التوقيع. يمكن أن يكون فارغًا.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
