---
title: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: يوضح هذا الموضوع كيفية حذف المسافات الزائدة بعد فاصل الأسطر أثناء استيراد HTML باستخدام Aspose.Cells for Python via NET.
keywords: حذف المسافات الزائدة بعد فاصل الأسطر أثناء استيراد HTML، حذف المسافات الزائدة أثناء استيراد html.
---

{{% alert color="primary" %}}

الرجاء استخدام خاصية [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) وتعيينها **true** لحذف جميع المسافات الزائدة بعد وسم فاصل السطر. بشكل افتراضي، تكون هذه الخاصية **false** وتُحافظ المسافات الزائدة في ملفات الإكسل الناتجة.

{{% /alert %}}

## تأثير ضبط خاصية HTMLLoadOptions.delete_redundant_spaces على الصفحة

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

الكود البرمجي التالي يُظهر استخدام خاصية [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/). الرجاء تعيينها **true** أو **false** للحصول على الناتج كما هو موضح في اللقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
