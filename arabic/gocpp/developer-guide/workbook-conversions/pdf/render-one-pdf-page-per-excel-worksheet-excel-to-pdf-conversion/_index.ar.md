---
title: عرض صفحة PDF واحدة لكل ورقة عمل في Excel  تحويل Excel إلى PDF باستخدام Golang عبر C++
type: docs
weight: 100
url: /ar/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: تحويل أوراق عمل إكسل إلى تنسيق PDF مع صفحة واحدة لكل ورقة باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}} 

عند العمل مع ملفات Excel كبيرة جدًا (على سبيل المثال، مصنف يحتوي على العديد من الأوراق، وكل منها يحتوي على 50 عمودًا و300 أو أكثر من الصفوف)، قد ترغب في أن يعرض إذًا المخرج PDF صفحة واحدة لكل ورقة، بغض النظر عن حجم الورقة. هذا يعني أن كل صفحة قد تكون ذات حجم صفحة مختلف بشكل جذري. يمكن تحقيق ذلك باستخدام Aspose.Cells for C++.

{{% /alert %}} 

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

إذا تم تعيين خيار [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) على **true**، سيتم عرض محتوى جميع الأوراق في صفحة PDF واحدة.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل استدعاء [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) قبل تصدير جدول البيانات إلى PDF مباشرة. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وظهور القيم الصحيحة في PDF.

{{% /alert %}}
