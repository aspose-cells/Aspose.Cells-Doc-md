---
title: عرض صفحة PDF واحدة لكل ورقة Excel  تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: تعلم كيفية إنشاء صفحة PDF واحدة لكل ورقة عمل برنامج إكسيل أثناء تحويل ملف Excel إلى PDF باستخدام واجهة برمجة تطبيقات Aspose.Cells لـ Python via .NET.
keywords: إنشاء صفحة PDF واحدة لكل ورقة عمل برنامج إكسيل باستخدام Python أثناء حفظ الملف إلى PDF، صفحة PDF واحدة لكل ورقة عمل برنامج إكسيل أثناء حفظ ملف إكسيل إلى PDF باستخدام Python, إظهار صفحة واحدة لكل ورقة عمل عند تحويل ملف Excel إلى PDF بواسطة Python
---

{{% alert color="primary" %}} 

عند العمل مع ملفات Microsoft Excel الكبيرة (على سبيل المثال، دفتر عمل يحتوي على العديد من الأوراق، كل منها به 50 عمودًا و300 صف أو أكثر من البيانات)، قد ترغب في عرض صفحة واحدة في ال PDF الناتجة لكل ورقة عمل، بغض النظر عن حجم الورقة. وهذا يعني أن كل صفحة من الممكن أن تكون لها حجم صفحة مختلف تمامًا. يمكن تحقيق ذلك باستخدام واجهة برمجة تطبيقات Aspose.Cells لـ Python via .NET.

{{% /alert %}} 

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

إذا تم تعيين خيار [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) إلى **صح**, سيتم عرض كل محتوى الورقة على صفحة PDF واحدة.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، من الأفضل استدعاء طريقة [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) قبل عرض جدول البيانات إلى PDF. هذا يضمن إعادة حساب القيم التي تعتمد على الصيغة، وعرض القيم الصحيحة في PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
