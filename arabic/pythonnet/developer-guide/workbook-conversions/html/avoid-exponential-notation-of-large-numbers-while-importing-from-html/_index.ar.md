---
title: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: توضح هذه الموضوع كيفية تجنب تقديم الرقم التمثيلي للأرقام الكبيرة أثناء استيرادها من HTML باستخدام Aspose.Cells for Python via NET.
keywords: تجنب تقديم الرقم التمثيلي للأرقام الكبيرة أثناء استيرادها من HTML، حفظ الدقة عند استيراد HTML.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتوي العنصر الخاص بك Html على أرقام مثل 1234567890123456 التي تتجاوز 15 رقمًا وعندما تقوم بإستيراد HTML الخاص بك إلى ملف إكسل، تتحول هذه الأرقام إلى علامة علمية مثل 1.23457E+15. إذا كنت ترغب في استيراد الرقم كما هو وعدم تحويله إلى علامة علمية، يُرجى استخدام ال [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) وضبطه إلى **true** أثناء تحميل HTML الخاص بك.

{{% /alert %}}

الشفرة العينية التالية توضح استخدام ال [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). ستقوم الواجهة بإستيراد الرقم كما هو دون تحويله إلى علامة علمية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
