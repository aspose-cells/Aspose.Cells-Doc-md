---
title: كيفية الكشف عن تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2700
url: /ar/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 تحتاج أحيانًا إلى اكتشاف تنسيق الملف قبل فتحه لأن امتداد الملف لا يضمن أن محتوى الملف مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذلك لا يمكن قراءته مباشرة ، أو لا ينبغي لنا قراءته. يوفر Aspose.Cells ملف[**FileFormatUtil.DetectFileFormat ()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) طريقة ثابتة وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.

{{% /alert %}}

يوضح نموذج التعليمات البرمجية التالي كيفية اكتشاف تنسيق ملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
