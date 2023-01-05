---
title: تجنب التدوين الأسي للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 600
url: /ar/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

في بعض الأحيان يحتوي HTML على أرقام مثل 1234567890123456 والتي تزيد عن 15 رقمًا وعندما تقوم باستيراد HTML إلى ملف Excel ، يتم تحويل هذه الأرقام إلى تدوين أسي مثل 1.23457E + 15. إذا أردت ، يجب استيراد رقمك كما هو وليس تحويله إلى تدوين أسي ، ثم الرجاء استخدام[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) الملكية وتعيينها**حقيقي** أثناء تحميل HTML الخاص بك.

{{% /alert %}} 
## **تجنب التدوين الأسي للأرقام الكبيرة أثناء الاستيراد من HTML**
 يشرح نموذج التعليمات البرمجية التالي استخدام[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)خاصية. سيقوم باستيراد الرقم كما هو دون تحويله إلى تدوين أسي.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
