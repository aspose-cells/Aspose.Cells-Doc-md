---
title: احتواء كافة أعمدة ورقة العمل على PDF صفحة واحدة
type: docs
weight: 70
url: /ar/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 في بعض الأحيان تريد إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل في صفحة واحدة. ال[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)توفر الخاصية هذه الميزة بطريقة سهلة الاستخدام للغاية. تتم معالجة الحسابات المعقدة مثل ارتفاع وعرض صفحة الإخراج PDF داخليًا وتعتمد على البيانات الموجودة في ورقة العمل.

{{% /alert %}}

## **احتواء أعمدة ورقة العمل في صفحة واحدة PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)يضمن عرض جميع أعمدة ورقة العمل على صفحة PDF واحدة ، على الرغم من إمكانية توسيع الصفوف إلى عدة صفحات بناءً على البيانات الموجودة في ورقة العمل.

{{% alert color="primary" %}}

عندما تحتوي ورقة عمل معينة على العديد من الأعمدة ، قد يعرض الملف PDF المحتويات بحجم صغير جدًا. لا يزال من الممكن قراءته عند توسيع نطاقه في تطبيق عرض مثل Acrobat Reader.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية أدناه كيفية استخدام ملف[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)لعرض ورقة عمل كبيرة من 100 عمود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[**مصنف .calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) فقط قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
