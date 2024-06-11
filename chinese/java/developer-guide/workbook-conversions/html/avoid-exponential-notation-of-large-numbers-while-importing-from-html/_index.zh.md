---
title: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 600
url: /zh/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

有时，您的 HTML 中包含如 1234567890123456 这样超过 15 位数的数字，当您将 HTML 导入到 Excel 文件时，这些数字将转换为指数表示法，如 1.23457E+15。如果您希望您的数字被导入为原样，而不是转换为指数表示法，则请在加载 HTML 时使用 [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) 属性，并将其设置为 **true**。

{{% /alert %}} 
## **在从 HTML 导入时避免大数字的指数表示法**
以下示例代码解释了 [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) 属性的用法。它将以原样导入该数字，而不转换为指数表示法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
