---
title: Aspose.Cells for Java 2.5.2 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/java/aspose-cells-for-java-2-5-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 2.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.5.2/)

{{% /alert %}} 

 يسعدنا أن نعلن Aspose.Cells for Java 2.5.2!

 ما الذي تغير:

- يدعم قراءة الجداول المحورية من ملفات القوالب.
 يضيف LineShape إلى ملفات Excel 2007 XLSX.
 يوفر الدعم لتعيين اسم السلسلة عند تعيين مصدر بيانات المخطط.
 يدعم الحصول على / تعيين رؤية خطوط الشبكة لأوراق العمل المختلفة في ملفات ODS.
 تم إجراء تحسين لقراءة الأشكال من ملفات XLSX.
 تم إجراء تحسينات لميزات Chart-to-Image و Sheet-to-Image و Excel-to-PDF.
 تم إجراء تحسين لتحليل الصيغ.
 تم إجراء تحسين لنسخ Cells.
31 إصلاحات وتحسينات.

 تم حل المشكلات في Aspose.Cells for Java 2.5.2.





 تغييرات ملحوظة للمستخدمين:



 في الإصدارات القديمة ، استخدم FormatCondition.getStyle () للتسبب في أن FormatConditions تحافظ على كائن النمط الخاص بها. سيؤدي تعديل كائن النمط الذي تم إرجاعه في getStyle () لاحقًا إلى تغيير نمط FormatCondition مباشرةً.

من هذا الإصدار ، سيستخدم FormatCondition فئة نمط أكثر واقعية DXFStyle (فئة فرعية من Style ، يمكننا من خلالها توفير ميزات أكثر مرونة ليتم دعمها في المستقبل). على سبيل المثال ، الآن سيعيد FormatCondition.getStyle () نسخة واحدة من كائن DXFStyle بدلاً من كائن النمط. وننصح المستخدمين باستخدام كائن DXFStyle لأسلوب FormatCondition.setStye (Style). سيتم تحويل كافة كائنات النمط التي تم تعيينها إلى FormatCondition إلى DXFStyle وتجميعها في تجمع عام لـ Workbook. وبالتالي فإن FormatCondition ستحتفظ فقط بمرجع DXFStyle. تعديل كائن DXFStyle الذي تم إرجاعه لـ getStyle () لاحقًا لن يغير نمط FormatCondition. لجعل التعديل ساري المفعول ، يحتاج المستخدمون إلى استدعاء setStyle () لـ FormatCondition بعد تعديل النمط.
