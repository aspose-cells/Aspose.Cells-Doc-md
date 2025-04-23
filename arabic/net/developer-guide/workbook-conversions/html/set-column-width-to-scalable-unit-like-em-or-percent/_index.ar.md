---
title: تعيين عرض العمود إلى وحدة قابلة للتوسيع مثل em أو percent
type: docs
weight: 130
url: /ar/net/set-column-width-to-scalable-unit-like-em-or-percent/
---

إن إنشاء ملف HTML من جدول بيانات يعتبر شائعًا جدًا. يتم تعريف حجم الأعمدة بـ "pt" والذي يعمل في العديد من الحالات. ومع ذلك، يمكن أن يكون هناك حالة حيث قد لا يكون هذا الحجم الثابت مطلوبًا. على سبيل المثال، إذا كان عرض لوحة الحاوية 600 بكسل حيث يتم عرض صفحة HTML، فيجب تغيير هذا الحجم الثابت إلى وحدة قابلة للتوسيع مثل em أو percent للحصول على عرض عرض أفضل. يمكن استخدام الرمز العيني التالي حيث يُعين [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) على **true** لإنشاء عرض قابل للتوسيع.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
