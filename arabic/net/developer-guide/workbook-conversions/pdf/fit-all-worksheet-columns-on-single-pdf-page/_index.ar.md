---
title: احتواء جميع أعمدة ورقة العمل في صفحة PDF واحدة
type: docs
weight: 160
url: /ar/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

في بعض الأحيان تريد إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل في صفحة واحدة. ال[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) توفر الخاصية هذه الميزة بطريقة سهلة الاستخدام للغاية. تتم معالجة الحسابات المعقدة مثل ارتفاع وعرض ملف PDF الناتج داخليًا وتعتمد على البيانات الموجودة في ورقة العمل.

{{% /alert %}}

## **احتواء أعمدة ورقة العمل في صفحة PDF واحدة**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)يضمن عرض جميع الأعمدة في ورقة العمل إلى صفحة PDF واحدة ، على الرغم من أن الصفوف قد تتوسع إلى عدة صفحات بناءً على البيانات الموجودة في ورقة العمل.

يوضح نموذج التعليمات البرمجية أدناه كيفية الاستخدام[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)لعرض ورقة عمل كبيرة من 100 عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

عندما تحتوي ورقة عمل معينة على العديد من الأعمدة ، فقد يعرض ملف PDF المعروض المحتوى بحجم صغير جدًا. لا يزال من الممكن قراءته عند توسيع نطاقه في تطبيق عرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[**المصنف .CalculateFormula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) مباشرة قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
