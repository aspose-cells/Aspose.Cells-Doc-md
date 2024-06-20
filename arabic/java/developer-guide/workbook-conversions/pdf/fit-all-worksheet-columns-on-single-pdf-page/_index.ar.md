---
title: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 70
url: /ar/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

أحيانًا ترغب في إنشاء ملف PDF يتناسب مع جميع أعمدة ورقة العمل على صفحة واحدة. الخاصية [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) توفر هذه الميزة بطريقة سهلة الاستخدام. الحسابات المعقدة مثل ارتفاع وعرض صفحة الPDF الناتجة يتم التعامل بها داخليًا وتعتمد على البيانات في ورقة العمل.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) يضمن أن تُقدم كل أعمدة ورقة العمل على صفحة PDF واحدة، على الرغم من أن الصفوف قد تمتد إلى عدة صفحات حسب البيانات في ورقة العمل.

{{% alert color="primary" %}}

عندما تحتوي ورقة عمل معينة على العديد من الأعمدة، قد يظهر ملف PDF المُقدم بحجم صغير جدًا. ولا يزال من القابل للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}}

الكود عينة أدناه يوضح كيفية استخدام الخاصية [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) لعرض ورقة عمل كبيرة تحتوي على 100 عمود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل استدعاء الطريقة [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل عرض الجدول بتنسيق PDF. سيضمن ذلك إعادة حساب القيم التي تعتمد على الصيغة، وعرض القيم الصحيحة في PDF.

{{% /alert %}}
