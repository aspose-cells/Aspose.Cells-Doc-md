﻿---
title: Aspose.Cells for Java 2.2.0 ملاحظات الإصدار
type: docs
weight: 80
url: /ar/java/aspose-cells-for-java-2-2-0-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 2.2.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.2.0/)

{{% /alert %}} 

 يسعدنا أن نعلن Aspose.Cells for Java 2.2.0!

 ما الذي تغير:

- يضبط الصيغ ذات الصفوف / العمود / المعلمات التي تتجاوز حد MS Excel 2003
 يدعم الاحتفاظ بالبيانات الأصلية المقروءة من ملف قالب MS Excel 2010
 معالجة خطوط سباركلينز MS Excel 2010
 يوفر أنماطًا ممتدة تم حفظها بواسطة MS Excel 2007 لملفات XLS
 يدعم الكشف التلقائي عن نوع تنسيق الملف أثناء فتح ملف القالب دون تحديد تنسيق لملفات Html و SpreadSheeML
 يزيل مخططًا من مجموعة المخططات
 يسمح بحذف الصفوف / الأعمدة الفارغة في ورقة العمل
يدعم حفظ اللون إلى أقرب لون مطابق في اللوحة عندما لا يكون اللون المحدد من قبل المستخدم في اللوحة القياسية.
 تصدير سمة استدارة النص لميزة Excel إلى Pdf
 تصدير المخططات كصور لميزة Excel إلى Pdf
 يزيل ناحية الطباعة الموجودة
 يتضمن تحسينات لحفظ المناطق المدمجة: تحقق من تلك المناطق المكررة / المتداخلة وأزلها أو ادمجها والتي قد تتسبب في ظهور رسالة تحذير تظهر الملف الذي تم إنشاؤه عند فتحه في MS Excel
 يتضمن تحسينات لإضافة فواصل الصفحات: تحقق من فواصل الصفحات المكررة وأزلها قبل الحفظ
 يتضمن تحسينا لميزة الرسم البياني للصورة
 65 إصلاحات وتحسينات أخرى.

 تم حل المشكلات في Aspose.Cells لـ Jav

 تغييرات ملحوظة للمستخدمين:



 في الإصدارات القديمة ، ستعمل أساليب Workbook.save (String) و Workbook.save (InputStream) دائمًا على حفظ الملف الناتج بتنسيق ملف Excel97TO2003.

من هذا الإصدار ، إذا تم تحديد نوع تنسيق المصنف ، فستقوم أساليب Workbook.save (String) و Workbook.save (InputStream) بحفظ الملف الناتج بالتنسيق المحدد بواسطة المصنف. يمكن تعيين نوع تنسيق المصنف بواسطة أسلوب Workbook.setFileFormatType (int). أو ، يمكن تعيينه كتنسيق ملف قالب الإدخال تلقائيًا عند فتح ملف قالب موجود.

 علاوة على ذلك ، يعتمد حد الصف / العمود للصيغ وحد عدد المعلمات للصيغ على نوع تنسيق المصنف أيضًا. قبل أن تتجاوز حد الصف / العمود / المعلمة للصيغ لبرنامج MS Excel 2003 ، يجب عليك تعيين تنسيق المصنف بشكل صريح لبعض الأنواع الأخرى ، مثل EXCEL2007.