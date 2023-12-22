---
title: تقديم صفحة واحدة PDF لكل ورقة عمل Excel - تحويل Excel إلى PDF
type: docs
weight: 100
url: /ar/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: تعرف على كيفية عرض صفحة واحدة PDF لكل ورقة عمل Excel أثناء تحويل Excel إلى PDF مع Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

عند العمل مع ملفات Excel كبيرة الحجم Microsoft (على سبيل المثال، مصنف يحتوي على العديد من الأوراق، تحتوي كل منها على 50 عمودًا و300 صف أو أكثر من البيانات)، قد ترغب في أن يُظهر الإخراج PDF صفحة واحدة لكل ورقة عمل، بغض النظر عن حجم ورقة العمل . وهذا يعني أنه من المحتمل أن يكون لكل صفحة حجم صفحة مختلف جذريًا. ويمكن تحقيق ذلك باستخدام Aspose.Cells for Python via .NET API.

{{% /alert %}} 

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يحول ملف Excel مع أوراق عمل متعددة إلى PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 إذا[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)تم ضبط الخيار على *true**، وسيتم عرض كل محتوى الورقة في صفحة واحدة برقم PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل الاتصال به[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) الطريقة مباشرة قبل تقديم جدول البيانات إلى PDF. وهذا يضمن إعادة حساب القيم التابعة للصيغة، ويتم عرض القيم الصحيحة في PDF.

{{% /alert %}}
