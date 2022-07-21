---
title: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 600
url: /java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

Sometimes your HTML contains numbers like 1234567890123456 which are longer than 15 digits and when you import your HTML to excel file, these numbers convert to exponential notation like 1.23457E+15. If you want, your number should be imported as it is and not converted to exponential notation, then please use [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) property and set it **true** while loading your HTML.

{{% /alert %}} 
## **Avoid exponential notation of large numbers while importing from HTML**
The following sample code explains the usage of [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) property. It will import the number as it is without converting it to exponential notation.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
