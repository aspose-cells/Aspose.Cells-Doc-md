---
title: حذف المسافات الزائدة بعد فاصل السطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/net/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}}

 الرجاء استخدام[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) الملكية وتعيينها**حقيقي** لحذف جميع المسافات الزائدة التي تأتي بعد علامة فاصل الأسطر. بشكل افتراضي ، هذه الخاصية هي**خاطئة**ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}}

## تأثير تعيين الخاصية HTMLLoadOptions.DeleteRedundantSpaces إلى false و true

 توضح لقطة الشاشة التالية تأثير تعيين هذه الخاصية على**خاطئة** و**حقيقي**.

![ما يجب القيام به: image_بديل_نص](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فاصل السطر أثناء استيراد HTML

### عينة البرمجة

 يُظهر نموذج التعليمات البرمجية التالي استخدام امتداد الملف[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) خاصية. يرجى ضبطه**حقيقي** أو**خاطئة** للحصول على الإخراج كما هو موضح في الصورة أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
