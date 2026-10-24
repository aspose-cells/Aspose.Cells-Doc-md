---
title: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2000
url: /ar/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

في بعض الأحيان تحتاج إلى اكتشاف تنسيق ملف قبل فتحه لأن امتداد الملف لا يضمن أن محتوى الملف مناسب. يمكن أن يكون الملف مشفرًا (ملف محمي بكلمة مرور) بحيث لا يمكن قراءته مباشرة، أو يجب عدم قراءته. توفر Aspose.Cells الطريقة الثابتة [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat-java.io.InputStream-) وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة الوثائق.

{{% /alert %}}

## **الشيفرة في جافا لاكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا**

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
{{< app/cells/assistant language="java" >}}
