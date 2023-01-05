---
title: كيفية الكشف عن تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2000
url: /ar/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 تحتاج أحيانًا إلى اكتشاف تنسيق الملف قبل فتحه لأن امتداد الملف لا يضمن أن محتوى الملف مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذلك لا يمكن قراءته مباشرة ، أو لا ينبغي لنا قراءته. يوفر Aspose.Cells ملف[**FileFormatUtil.detectFileFormat ()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)طريقة ثابتة وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.

{{% /alert %}}

## **رمز Java لاكتشاف تنسيق الملف وتحقق مما إذا كان الملف مشفرًا**

يوضح نموذج التعليمات البرمجية التالي كيفية اكتشاف تنسيق ملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا أم لا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
