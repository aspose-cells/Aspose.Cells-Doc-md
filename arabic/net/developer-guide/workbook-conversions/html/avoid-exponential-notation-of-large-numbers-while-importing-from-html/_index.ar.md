---
title: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتوي العنصر الخاص بك Html على أرقام مثل 1234567890123456 التي تتجاوز 15 رقمًا وعندما تقوم بإستيراد HTML الخاص بك إلى ملف إكسل، تتحول هذه الأرقام إلى علامة علمية مثل 1.23457E+15. إذا كنت ترغب في استيراد الرقم كما هو وعدم تحويله إلى علامة علمية، يُرجى استخدام ال [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) وضبطه إلى **true** أثناء تحميل HTML الخاص بك.

{{% /alert %}}

الشفرة العينية التالية توضح استخدام ال [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). ستقوم الواجهة بإستيراد الرقم كما هو دون تحويله إلى علامة علمية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
