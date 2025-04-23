---
title: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

الرجاء استخدام خاصية [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) وتعيينها **true** لحذف جميع المسافات الزائدة بعد وسم فاصل السطر. بشكل افتراضي، تكون هذه الخاصية **false** وتُحافظ المسافات الزائدة في ملفات الإكسل الناتجة.

{{% /alert %}}

## تأثير تعيين خاصية HTMLLoadOptions.DeleteRedundantSpaces بقيمة false و true

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

الكود البرمجي التالي يُظهر استخدام خاصية [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). الرجاء تعيينها **true** أو **false** للحصول على الناتج كما هو موضح في اللقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
