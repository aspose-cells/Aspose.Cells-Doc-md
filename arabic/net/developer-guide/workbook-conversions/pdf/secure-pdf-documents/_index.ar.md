---
title: مستندات PDF آمنة
type: docs
weight: 120
url: /ar/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يحتاج المطورون إلى العمل مع ملفات PDF المشفرة. على سبيل المثال ، يحتاجون إلى تأمين المستندات بكلمات مرور المستخدم والمالك بحيث لا يمكن لأي شخص فتحها فقط ، أو يريدون تقييد ما إذا كان يمكن طباعة محتوى المستند أو استخراجه.

تشرح هذه المقالة كيفية تمرير خيارات أمان PDF عند حفظ جداول البيانات في PDF.

{{% /alert %}}

 يوفر Aspose.Cells ملف[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) مساحة للعمل مع الأمان. يصف نموذج التعليمات البرمجية أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ ، فمن الأفضل الاتصال[**المصنف .CalculateFormula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)قبل تحويله إلى PDF. يضمن ذلك إعادة حساب القيم التابعة للصيغة وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
