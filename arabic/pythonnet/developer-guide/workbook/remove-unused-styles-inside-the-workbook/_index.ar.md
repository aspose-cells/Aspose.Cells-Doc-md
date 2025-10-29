---
title: إزالة الأنماط الغير مستخدمة في دفتر العمل
type: docs
weight: 340
url: /ar/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

الأنماط غير المستخدمة في ملف إكسل لا تأخذ مساحة فحسب، بل تتسبب أيضًا في مشاكل أداء أثناء التحويل إلى تنسيقات أخرى مثل PDF وHTML. يُوفر Aspose.Cells لبايثون via .NET الخاصية [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) لإزالة جميع الأنماط غير المستخدمة داخل كتاب العمل.

{{% /alert %}}

يشرح الكود التالي استخدام [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). يقوم الكود بتحميل [ملف إكسل النموذج](5115520.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم يسمى **AsposeStyle**, سيتم إزالة هذا النمط وجميع الأنماط الأخرى غير المستخدمة بعد تنفيذ الكود.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
