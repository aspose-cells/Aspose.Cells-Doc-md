---
title: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2700
url: /ar/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

في بعض الأحيان ، قد تحتاج إلى اكتشاف تنسيق الملف قبل فتحه لأن امتداد الملف لا يضمن محتوى الملف المناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذا لا يمكن قراءته مباشرة ، أو يجب عدم قراءته. توفر Aspose.Cells الطريقة الثابتة [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.

{{% /alert %}}

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
{{< app/cells/assistant language="csharp" >}}
