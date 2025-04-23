---
title: مستندات PDF الآمنة
type: docs
weight: 120
url: /ar/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات مرور للمالك والمستخدم أثناء الحفظ إلى PDF. ستكون كلمة المرور للمالك أو كلمة المرور للمستخدم مطلوبة لفتح المستند PDF المُشفر للعرض.

- يمكن أن تكون كلمة المرور للمستخدم فارغة أو سلسلة فارغة، في هذه الحالة لن يكون هناك حاجة إلى كلمة مرور من المستخدم عند فتح مستند PDF.
- فتح مستند PDF بكلمة مرور المالك الصحيحة يسمح بالوصول الكامل (دون تحديد أي قيود وصول) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود النموذجي أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

إذا كانت جداول البيانات تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل عرضها إلى PDF. يضمن هذا إعادة حساب القيم المعتمدة على الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
