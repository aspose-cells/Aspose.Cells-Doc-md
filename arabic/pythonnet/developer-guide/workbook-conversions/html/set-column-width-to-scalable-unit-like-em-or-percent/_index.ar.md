---
title: تعيين عرض العمود إلى وحدة قابلة للتوسيع مثل em أو percent
type: docs
weight: 130
url: /ar/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

إن إنشاء ملف HTML من جدول بيانات يعتبر شائعًا جدًا. يتم تعريف حجم الأعمدة بـ "pt" والذي يعمل في العديد من الحالات. ومع ذلك، يمكن أن يكون هناك حالة حيث قد لا يكون هذا الحجم الثابت مطلوبًا. على سبيل المثال، إذا كان عرض لوحة الحاوية 600 بكسل حيث يتم عرض صفحة HTML، فيجب تغيير هذا الحجم الثابت إلى وحدة قابلة للتوسيع مثل em أو percent للحصول على عرض عرض أفضل. يمكن استخدام الرمز العيني التالي حيث يُعين [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) على **true** لإنشاء عرض قابل للتوسيع.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
