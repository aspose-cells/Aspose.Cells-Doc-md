---
title: احفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 130
url: /ar/python-net/save-each-worksheet-to-a-different-pdf-file/
description: تعرف على كيفية حفظ كل ورقة عمل في ملف PDF مختلف مع Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET يدعم تحويل XLS ملف (يحتوي على صور ومخططات وغيرها) إلى PDF مستند. Aspose.Cells for Python via .NET يمكن أن تعمل بشكل مستقل لتحويل جدول بيانات إلى PDF ولا تحتاج إلى استخدام Aspose.PDF for .NET للتحويل. لا يتطلب التحويل أن يقوم البرنامج بإنشاء أو استخدام أي ملفات مؤقتة حيث يمكن إجراء العملية بأكملها في الذاكرة.

{{% /alert %}} 
##  **احفظ كل ورقة عمل في ملف PDF مختلف**
 إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف Excel القالب الخاص بك لإنشاء ملفات PDF مختلفة، فيمكنك تحقيق ذلك بسهولة. يمكنك محاولة تعيين فهرس ورقة واحدة على**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** الخيار في وقت واحد لتقديم إلى PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل الاتصال به[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) مباشرة قبل تقديم جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
