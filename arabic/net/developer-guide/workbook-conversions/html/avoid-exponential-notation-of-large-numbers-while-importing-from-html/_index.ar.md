---
title: تجنب التدوين الأسي للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، يحتوي Html على أرقام مثل 1234567890123456 أطول من 15 رقمًا وعندما تقوم باستيراد HTML إلى ملف Excel ، تتحول هذه الأرقام إلى تدوين أسي مثل 1.23457E + 15. إذا أردت ، يجب استيراد رقمك كما هو وليس تحويله إلى تدوين أسي ، ثم الرجاء استخدام[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) الملكية وتعيينها**حقيقي** أثناء تحميل HTML الخاص بك.

{{% /alert %}}

 يشرح نموذج التعليمات البرمجية التالي استخدام[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)خاصية. سيقوم API باستيراد الرقم كما هو بدون تحويله إلى تدوين أسي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
