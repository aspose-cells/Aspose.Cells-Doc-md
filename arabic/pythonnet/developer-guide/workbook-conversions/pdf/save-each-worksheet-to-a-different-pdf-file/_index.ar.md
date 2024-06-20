---
title: حفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 130
url: /ar/python-net/save-each-worksheet-to-a-different-pdf-file/
description: تعلم كيفية حفظ كل ورق عمل إلى ملف PDF مختلف مع Aspose.Cells لبرنامجPython via .NET
keywords: Python حفظ كل ورق عمل إلى ملف PDF مختلف
---

{{% alert color="primary" %}} 

Aspose.Cells لبرنامجPython via .NET يدعم تحويل ملفات XLS (التي تحتوي على صور ورسوم بيانية وما إلى ذلك) إلى مستندات PDF. برنامج Aspose.Cells لبرنامجPython via .NET يمكن أن يعمل بشكل مستقل لتحويل جدول بيانات إلى PDF ولا تحتاج إلى استخدام Aspose.PDF لنظام التشغيل .NET للتحويل. التحويل لا يتطلب استخدام البرنامج لإنشاء أو استخدام أي ملفات مؤقتة حيث يمكن القيام بالعملية بالكامل في الذاكرة.

{{% /alert %}} 
## **حفظ كل ورقة عمل في ملف PDF مختلف**
إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف الإكسيل النموذجي لتوليد ملفات PDF مختلفة، يمكنك تحقيق هذا بسهولة. يمكنك تجربة ضبط رقم الورقة الواحدة إلى الخيار [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) في كل مرة لتقديم إلى PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
