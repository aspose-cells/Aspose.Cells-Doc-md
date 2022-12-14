---
title: مستندات PDF آمنة
type: docs
weight: 260
url: /ar/java/secure-pdf-documents/
description: تأمين ملفات PDF أثناء التحويل من ملفات Excel. توضح هذه المقالة إنشاء ملف PDF آمن من Excel باستخدام Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المطورون إلى العمل مع ملفات PDF المشفرة. على سبيل المثال ، يحتاجون إلى تأمين المستندات بكلمات مرور المستخدم والمالك بحيث لا يمكن لأي شخص فتحها فقط ، أو يريدون تقييد ما إذا كان يمكن طباعة محتوى المستند أو استخراجه.

تشرح هذه المقالة كيفية تمرير خيارات أمان PDF عند حفظ جداول البيانات في PDF.

{{% /alert %}} 

 توفر واجهات برمجة التطبيقات Aspose.Cells امتداد[**خيارات PdfSecurity**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)فئة للعمل بأمان تنسيق ملف PDF. يصف نموذج التعليمات البرمجية أدناه كيفية إنشاء ملفات PDF مؤمنة باستخدام Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ ، فمن الأفضل الاتصال[**Workbook.calculateFormula ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) قبل تحويله إلى PDF. يضمن ذلك إعادة حساب القيم التابعة للصيغة ، وتجسيد القيم الصحيحة في ملف PDF.

{{% /alert %}}
