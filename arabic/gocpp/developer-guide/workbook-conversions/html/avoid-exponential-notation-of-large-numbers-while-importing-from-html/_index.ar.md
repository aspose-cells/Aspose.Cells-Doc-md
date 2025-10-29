---
title: تجنب التمثيل بالأرقام الأسية للأرقام الكبيرة عند الاستيراد من HTML باستخدام Golang عبر C++
linktitle: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: تعلم كيفية تجنب تدوين الأرقام الكبيرة في الصيغة الأسية أثناء الاستيراد من HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 أحيانًا يتضمن HTML الخاص بك أرقامًا طويلة مثل 1234567890123456 والتي تتجاوز 15 رقمًا، وعند استيراد HTML إلى ملف إكسل، تتغير هذه الأرقام إلى صيغة أُسية مثل 1.23457E+15. إذا كنت تريد استيراد الرقم كما هو وعدم تحويله إلى صيغة أُسية، يرجى استخدام خاصية [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) وتعيينها إلى **true** أثناء تحميل HTML الخاص بك.

{{% /alert %}}

 يوضح الكود النموذجي التالي كيفية استخدام خاصية [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/). ستقوم الـ API باستيراد الرقم كما هو دون تحويله إلى صيغة أُسية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
