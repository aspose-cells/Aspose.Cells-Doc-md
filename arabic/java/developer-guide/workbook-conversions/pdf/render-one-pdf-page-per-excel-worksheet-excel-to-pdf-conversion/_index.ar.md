---
title: عرض صفحة PDF واحدة لكل ورقة Excel  تحويل Excel إلى صيغة PDF
type: docs
weight: 40
url: /ar/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

عند العمل مع ملفات مايكروسوفت إكسل الكبيرة (على سبيل المثال، دفتر عمل يحتوي على العديد من الأوراق، كل ورقة تحتوي على 50 عمودًا و300 صفًا أو أكثر من البيانات)، قد ترغب في جعل مخرجات PDF تظهر صفحة واحدة لكل ورقة عمل، بصرف النظر عن حجم الورقة. هذا يعني أن كل صفحة عرض على الأرجح ستكون لها حجم صفحة مختلفة بشكل كبير. يمكن تحقيق هذا باستخدام الرقم المعرف Aspose.Cells for Java.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

إذا تم تعيين [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)إلى **true**, سيتم عرض جميع محتويات الورقة إلى صفحة واحدة في PDF. حجم الورقة المعين بواسطة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) غير صالح، ولكن الإعدادات الأخرى المعينة بواسطة [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) لا يزال لها تأثير.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، فمن الأفضل استدعاء الطريقة [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل عرض الجدول الحاسبي إلى PDF. هذا يضمن إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في ملف الـPDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
