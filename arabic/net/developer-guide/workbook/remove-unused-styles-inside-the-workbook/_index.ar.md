---
title: إزالة الأنماط الغير مستخدمة في دفتر العمل
type: docs
weight: 340
url: /ar/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

الأنماط غير المستخدمة في ملف الإكسل لا تأخذ مساحة فقط، بل تسبب أيضاً مشكلات في الأداء أثناء التحويل إلى تنسيقات مختلفة مثل PDF، HTML، إلخ. يوفر Aspose.Cells الـ [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) لإزالة كل الأنماط غير المستخدمة داخل دفتر العمل.

{{% /alert %}}

يشرح الكود التالي استخدام [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles). يقوم الكود بتحميل [ملف إكسل النموذج](5115520.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم يسمى **AsposeStyle**, سيتم إزالة هذا النمط وجميع الأنماط الأخرى غير المستخدمة بعد تنفيذ الكود.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
