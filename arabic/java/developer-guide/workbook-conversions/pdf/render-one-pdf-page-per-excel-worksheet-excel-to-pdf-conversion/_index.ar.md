---
title: تقديم صفحة PDF واحدة لكل ورقة عمل Excel - تحويل Excel إلى PDF
type: docs
weight: 40
url: /ar/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

عند العمل باستخدام ملفات Excel كبيرة Microsoft (على سبيل المثال ، مصنف يحتوي على العديد من الأوراق ، كل منها يحتوي على 50 عمودًا و 300 صف أو أكثر من البيانات) ، قد ترغب في أن يُظهر إخراج PDF صفحة واحدة لكل ورقة عمل ، بغض النظر عن حجم ورقة العمل . قد يعني هذا أنه من المحتمل أن يكون لكل صفحة حجم صفحة مختلف تمامًا. يمكن تحقيق ذلك باستخدام Aspose.Cells for Java.

{{% /alert %}}

يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي يحول ملف Excel مع أوراق عمل متعددة إلى PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 إذا كان[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) تم تعيين الخيار إلى**حقيقي** ، يتم تقديم كل محتويات الورقة إلى صفحة PDF واحدة. تم تحديد حجم الورق بواسطة[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) غير صالح ، لكن الإعدادات الأخرى التي تم ضبطها باستخدام[**اعداد الصفحة**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)لا يزال ساري المفعول.

{{% /alert %}} {{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل استدعاء[**مصنف .calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) فقط قبل تحويل جدول البيانات إلى PDF. يضمن ذلك إعادة حساب القيم التابعة للصيغة ، وتجسيد القيم الصحيحة في ملف PDF.

{{% /alert %}}
