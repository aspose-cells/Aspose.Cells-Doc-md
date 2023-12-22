---
title: تأمين PDF الوثائق
type: docs
weight: 260
url: /ar/java/secure-pdf-documents/
description: تأمين ملفات PDF أثناء التحويل من ملفات Excel. توضح هذه المقالة إنشاء ملف PDF آمن من Excel باستخدام Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع الملفات المشفرة PDF. على سبيل المثال:

- قم بتأمين المستندات باستخدام كلمات مرور المالك والمستخدم حتى لا يتمكن أي شخص من فتحها.
- قم بتعيين القيود أو الأذونات للمستند بعد فتح المستند. على سبيل المثال، تقييد ما إذا كان يمكن طباعة محتوى المستند أو استخراجه.

تشرح هذه المقالة كيفية تمرير خيارات الأمان PDF عند حفظ جداول البيانات إلى PDF.

{{% /alert %}}

 Aspose.Cells يوفر[**خيارات PDF الأمنية**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)للعمل مع الأمن. يمكنك تعيين كلمات مرور المالك والمستخدم أثناء الحفظ في PDF. ستكون كلمة مرور المالك أو كلمة مرور المستخدم مطلوبة لفتح مستند PDF المشفر للعرض.

- يمكن أن تكون كلمة مرور المستخدم فارغة أو سلسلة فارغة، وفي هذه الحالة لن تكون كلمة المرور مطلوبة من المستخدم عند فتح مستند PDF.
- يتيح فتح المستند PDF باستخدام كلمة مرور المالك الصحيحة الوصول الكامل (دون تحديد أي قيود وصول) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور مستخدم) يسمح بوصول محدود حسب الأذونات المحددة.

يصف نموذج التعليمات البرمجية أدناه كيفية إنشاء ملفات PDF آمنة مع Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل الاتصال به[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()مباشرة قبل تقديمه إلى PDF. وهذا يضمن إعادة حساب القيم التابعة للصيغة، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
