---
title: حذف الفراغات الزائدة بعد فاصل السطر عند استيراد HTML باستخدام Golang عبر C++
linktitle: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: تعرف على كيفية حذف الفراغات الزائدة بعد فواصل السطور عند استيراد HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يرجى استخدام الخاصية [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) وتعيينها **true** لحذف جميع المسافات الزائدة التي تأتي بعد وسم فاصل الأسطر. بشكل افتراضي، تكون هذه الخاصية **false** ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}}

## تأثير تعيين خاصية HTMLLoadOptions.DeleteRedundantSpaces بقيمة false و true

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

الكود البرمجي التالي يُظهر استخدام خاصية [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). الرجاء تعيينها **true** أو **false** للحصول على الناتج كما هو موضح في اللقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
