---
title: عرض صفحة PDF واحدة لكل ورقة Excel  تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

عند العمل مع ملفات Microsoft Excel الكبيرة (على سبيل المثال، سجل عمل يحتوي على العديد من الأوراق، كل ورقة بها 50 عمود و300 أو أكثر صفوف من البيانات)، قد ترغب في أن تظهر الناتج كملف PDF صفحة واحدة لكل ورقة عمل، بصرف النظر عن حجم الورقة. يمكن تحقيق ذلك عن طريق استخدام Aspose.Cells for .NET.

{{% /alert %}} 

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

إذا تم تعيين الخيار [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) إلى **true**, سيتم عرض محتوى الورقة كاملة في صفحة واحدة من ملف PDF.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل تقديم جدول البيانات إلى PDF. هذا يضمن إعادة حساب قيم الصيغ وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
