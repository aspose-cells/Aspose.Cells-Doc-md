---
title: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2700
url: /ar/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى كشف تنسيق ملف قبل فتحه لأن امتداد الملف لا يضمن أن المحتوى مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) بحيث لا يمكن قراءته مباشرة، أو يجب ألا نقوم بقراءته. توفر Aspose.Cells لبايثون via .NET الطريقة الثابتة [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.

{{% /alert %}}

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

