---
title: التوقيع الرقمي لمشروع كود VBA بشهادة
type: docs
weight: 110
url: /ar/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

يمكنك توقيع مشروع كود VBA الخاص بك رقميًا باستخدام Aspose.Cells مع الأسلوب [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). يرجى اتباع هذه الخطوات للتحقق مما إذا كان ملف Excel الخاص بك موقع رقميًا بشهادة.

- انقر فوق **Basic Visual** من علامة التبويب **المطور** لفتح **البيئة المتقدمة لتطبيقات Basic Visual**
- انقر فوق **أدوات** > **التواقيع الرقمية...** في **بيئة البصمات البصرية لتطبيقات Basic Visual**

وسيظهر النموذج التوقيع **الرقمي** يظهر إذا كان المستند موقعًا رقميًا بشهادة أم لا.

{{% /alert %}} 

## **توقيع مشروع كود VBA رقميًا بشهادة في C#**

يوضح الكود العيني التالي كيفية استخدام الأسلوب [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). إليك ملفات الإدخال والإخراج للكود العيني. يمكنك استخدام أي ملف Excel وأي شهادة لاختبار هذا الكود.

- [ملف Excel المصدر](5115028.xlsm) المستخدم في الكود العيني.
- [ملف pfx العيني](5115039.pfx) لإنشاء توقيع رقمي. يرجى تثبيته على جهاز الكمبيوتر الخاص بك لتشغيل هذا الكود. كلمة المرور الخاصة به هي 1234.
- [ملف Excel الناتج](5115029.xlsm) الذي تم إنشاؤه بواسطة الكود العيني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
