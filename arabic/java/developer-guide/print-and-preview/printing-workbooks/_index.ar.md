---
title: طباعة الجداول
type: docs
weight: 20
url: /ar/java/printing-workbooks/
description: كيف يمكن طباعة ورقات العمل والصفحات باستخدام جافا. يوفر هذا المقال الرمز في جافا لطباعة ورقات العمل والصفحات باستخدام واجهة برمجة التطبيقات رقم Aspose.Cells for Java.
keywords: طباعة ورقات العمل، طباعة صفحات العمل، طباعة صفحات جدول البيانات، طباعة صفحة عمل، طباعة صفحة العمل في جافا، طباعة صفحات جدول البيانات في جافا، طباعة صفحات جدول البيانات في إكسل باستخدام جافا، طباعة صفحة إكسل باستخدام جافا، طباعة ورقة عمل، طباعة صفحة عمل
---

{{% alert color="primary" %}}

تم تصميم هذا المستند لتزويد المطورين بفهم موجز حول كيفية طباعة جداول البيانات.

{{% /alert %}}

## سيناريو الاستخدام

بعد الانتهاء من إنشاء جدول البيانات الخاص بك، سترغب على الأرجح في طباعة نسخة ورقية من الصفحة وذلك لاحتياجك. عندما تقوم بالطباعة، يفترض ببرنامج MS Excel أنك تود طباعة مساحة صفحة العمل بأكملها ما لم تحدد اختيارك. يوضح اللقطة الشاشية التالية نافذة الحوار لطباعة ورقة العمل مع Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**الشكل:** مربع الحوار للطباعة

## طباعة ورقات العمل باستخدام Aspose.Cells

توفر Aspose.Cells for Java طريقة [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) من الفئة [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). من خلال استخدام الطريقة [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))، يمكنك تحديد اسم الطابعة وكذلك اسم وظيفة الطباعة.

## كود عينة

### طباعة صفحة العمل المحددة

كود العينة التالي يوضح استخدام الطريقة [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) لطباعة ورقة عملك المحددة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### طباعة ورقة البيانات بأكملها

يمكنك أيضًا استخدام الطريقة [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) لطباعة المصنف بأكمله. يوضح كود العينة التالي استخدام الطريقة [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) لطباعة المصنف بأكمله.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## مقالات ذات صلة

- [تحديد اسم المهمة أو المستند أثناء الطباعة باستخدام Aspose.Cells](/cells/ar/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
