---
title: تقديم واحد PDF صفحة لكل ورقة عمل Excel - تحويل Excel إلى PDF
type: docs
weight: 100
url: /ar/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

عند العمل باستخدام ملفات Excel كبيرة Microsoft (على سبيل المثال ، مصنف يحتوي على العديد من الأوراق ، كل منها يحتوي على 50 عمودًا و 300 صف أو أكثر من البيانات) ، قد ترغب في أن يعرض إخراج PDF صفحة واحدة لكل ورقة عمل ، بغض النظر عن حجم ورقة العمل . قد يعني هذا أنه من المحتمل أن يكون لكل صفحة حجم صفحة مختلف تمامًا. يمكن تحقيق ذلك باستخدام Aspose.Cells for .NET.

{{% /alert %}} 

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يحول ملف Excel مع أوراق عمل متعددة إلى PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 إذا كان[OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) تم تعيين الخيار إلى**حقيقي**، سيتم تحويل كافة محتويات الورقة إلى صفحة PDF واحدة.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[المصنف .CalculateFormula ()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)قبل تحويل جدول البيانات إلى PDF. هذا يضمن إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
