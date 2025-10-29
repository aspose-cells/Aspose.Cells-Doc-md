---
title: التوقيع الرقمي لمشروع كود VBA بشهادة
type: docs
weight: 110
url: /ar/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

يمكنك توقيع شفريًا مشروع VBA باستخدام Aspose.Cells لبايثون via .NET مع طريقتها [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). يرجى اتباع هذه الخطوات للتحقق مما إذا كان ملف إكسل الخاص بك موقعًا رقميًا بشهادة.

- انقر فوق **Basic Visual** من علامة التبويب **المطور** لفتح **البيئة المتقدمة لتطبيقات Basic Visual**
- انقر فوق **أدوات** > **التواقيع الرقمية...** في **بيئة البصمات البصرية لتطبيقات Basic Visual**

وسيظهر النموذج التوقيع **الرقمي** يظهر إذا كان المستند موقعًا رقميًا بشهادة أم لا.

{{% /alert %}} 

## **التوقيع الرقمي على مشروع شفرة VBA باستخدام شهادة في بايثون**

يوضح الكود العيني التالي كيفية استخدام الأسلوب [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). إليك ملفات الإدخال والإخراج للكود العيني. يمكنك استخدام أي ملف Excel وأي شهادة لاختبار هذا الكود.

- [ملف Excel المصدر](5115028.xlsm) المستخدم في الكود العيني.
- [ملف pfx العيني](5115039.pfx) لإنشاء توقيع رقمي. يرجى تثبيته على جهاز الكمبيوتر الخاص بك لتشغيل هذا الكود. كلمة المرور الخاصة به هي 1234.
- [ملف Excel الناتج](5115029.xlsm) الذي تم إنشاؤه بواسطة الكود العيني.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
