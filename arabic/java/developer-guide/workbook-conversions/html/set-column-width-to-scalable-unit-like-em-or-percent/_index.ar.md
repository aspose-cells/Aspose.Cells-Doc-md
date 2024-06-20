---
title: تعيين عرض العمود إلى وحدة قابلة للتوسيع مثل em أو percent
type: docs
weight: 130
url: /ar/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

إن إنشاء ملف HTML من جدول بيانات يعتبر شائعًا للغاية. يُعرَّف حجم الأعمدة بـ "نقطة" والذي يعمل في العديد من الحالات. ومع ذلك، قد يكون هناك حالة حيث قد لا يكون هذا الحجم الثابت مطلوبًا. على سبيل المثال، إذا كان عرض اللوحة الحاوية 600 بكسل حيث يتم عرض صفحة HTML هذه. في هذه الحالة، قد تحصل على شريط التمرير الأفقي إذا كان عرض الجدول المُنشأ أكبر. كان مطلوبًا تغيير هذا الحجم الثابت إلى وحدة قابلة للتطويل مثل em أو percent للحصول على عرض أفضل. يمكن استخدام الكود العيني التالي حيث يتم ضبط [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) على **true** لإنشاء عرض قابل للتطويل.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
