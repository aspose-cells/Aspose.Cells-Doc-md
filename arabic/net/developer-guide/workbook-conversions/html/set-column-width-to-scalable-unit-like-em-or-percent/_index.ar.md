---
title: اضبط عرض العمود على وحدة قابلة للتحجيم مثل em أو نسبة مئوية
type: docs
weight: 130
url: /ar/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
يعد إنشاء ملف HTML من جدول بيانات أمرًا شائعًا جدًا. يتم تحديد حجم الأعمدة في "pt" والتي تعمل في كثير من الحالات. ومع ذلك ، يمكن أن تكون هناك حالة قد لا يكون فيها هذا الحجم الثابت مطلوبًا. على سبيل المثال ، إذا كان عرض لوحة الحاوية هو 600 بكسل حيث يتم عرض صفحة HTML هذه. في هذه الحالة ، قد تحصل على شريط تمرير أفقي إذا كان عرض الجدول الذي تم إنشاؤه أكبر. كان مطلوبًا أن يتم تغيير هذا الحجم الثابت إلى وحدة قابلة للتوسع مثل em أو النسبة المئوية للحصول على عرض تقديمي أفضل. يمكن استخدام نموذج التعليمات البرمجية التالية حيث[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) تم تعيينه على**حقيقي** لإنشاء عرض قابل للتطوير.

يمكن تنزيل نموذج ملف المصدر وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
