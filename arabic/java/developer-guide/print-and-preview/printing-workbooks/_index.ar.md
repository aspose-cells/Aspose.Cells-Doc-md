---
title: دفاتر الطباعة
type: docs
weight: 20
url: /ar/java/printing-workbooks/
description: كيفية طباعة أوراق العمل والمصنف باستخدام Java. توفر هذه المقالة كود Java لطباعة أوراق العمل والمصنف باستخدام Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

تم تصميم هذا المستند لتزويد المطورين بفهم (بطريقة مضغوطة) حول كيفية طباعة جداول البيانات.

{{% /alert %}}

## سيناريو الاستخدام

بعد الانتهاء من إنشاء جدول البيانات ، قد ترغب في طباعة نسخة ورقية من الورقة حسب حاجتك. عندما تقوم بالطباعة ، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد اختيارك. تُظهر لقطة الشاشة التالية مربع الحوار لطباعة المصنف باستخدام Excel.

![ما يجب القيام به: image_بديل_نص](printing-workbooks_1.png)

**شكل:** مربع حوار الطباعة

## طباعة مصنفات باستخدام Aspose.Cells

 يوفر Aspose.Cells for Java أ[**إلى الطابعة**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) طريقة ال[**عرض الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) صف دراسي. باستخدام ملف[**عرض الورقة للطابعة**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) ، يمكنك توفير اسم الطابعة بالإضافة إلى اسم مهمة الطباعة.

## عينة من الرموز

### طباعة ورقة العمل المحددة

 يوضح مقتطف الشفرة التالي استخدام ملف[**عرض الورقة للطابعة**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) طريقة لطباعة ورقة العمل التي اخترتها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### طباعة مصنف كامل

 يمكنك أيضًا استخدام ملف[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) طريقة لطباعة المصنف بأكمله. يوضح مقتطف الشفرة التالي استخدام ملف[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) طريقة لطباعة المصنف بأكمله.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## مقالات ذات صلة

- [حدد اسم المهمة أو المستند أثناء الطباعة باستخدام Aspose.Cells](/cells/ar/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
