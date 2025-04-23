---
title: مستندات PDF الآمنة
type: docs
weight: 260
url: /ar/java/secure-pdf-documents/
description: حماية ملفات PDF أثناء التحويل من ملفات Excel. يوضح هذا المقال كيفية إنشاء ملف PDF آمن من Excel باستخدام API Aspose.Cells for Java.
keywords: مستندات PDF آمنة في جافا، مستندات PDF آمنة، Excel إلى PDF آمن، Excel إلى PDF آمن في جافا، تحويل Excel إلى PDF آمن، تحويل Excel إلى PDF آمن في جافا، تحويل Excel إلى PDF محمي بكلمة مرور، تحويل Excel إلى PDF محمي بكلمة مرور في جافا، Excel إلى PDF محمي بكلمة مرور في جافا، Excel إلى PDF محمي بكلمة مرور
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات مرور للمالك والمستخدم أثناء الحفظ إلى PDF. ستكون كلمة المرور للمالك أو كلمة المرور للمستخدم مطلوبة لفتح المستند PDF المُشفر للعرض.

- يمكن أن تكون كلمة المرور للمستخدم فارغة أو سلسلة فارغة، في هذه الحالة لن يكون هناك حاجة إلى كلمة مرور من المستخدم عند فتح مستند PDF.
- فتح مستند PDF بكلمة مرور المالك الصحيحة يسمح بالوصول الكامل (دون تحديد أي قيود وصول) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود العيني أدناه كيفية إنشاء ملفات PDF مؤمنة باستخدام API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

إذا كانت جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) مباشرة قبل عرضه إلى PDF. يضمن هذا إعادة حساب القيم التي تعتمد على الصيغ، وعرض القيم الصحيحة في ملف PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
