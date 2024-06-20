---
title: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 600
url: /ar/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

أحيانًا، الـ HTML الخاص بك يحتوي على أرقام مثل 1234567890123456 التي تزيد عن 15 رقمًا وعندما تقوم بإستيراد الـ HTML إلى ملف إكسل، تتحول هذه الأرقام إلى تدوين علمي مثل 1.23457E+15. إذا كنت ترغب في استيراد الرقم كما هو دون تحويله إلى تدوين علمي، يرجى استخدام خاصية [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) وتعيينها على **true** أثناء استيراد HTML الخاص بك.

{{% /alert %}} 
## **تجنب التدوين العلمي للأرقام الكبيرة أثناء الاستيراد من الـ HTML**
توضح الشيفرة العينية التالية الاستخدام لخاصية [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). ستقوم باستيراد الرقم كما هو دون تحويله إلى تدوين علمي.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
