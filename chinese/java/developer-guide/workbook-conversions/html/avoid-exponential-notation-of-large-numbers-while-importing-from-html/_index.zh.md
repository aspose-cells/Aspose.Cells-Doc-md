---
title: 从 HTML 导入时避免大数的指数表示法
type: docs
weight: 600
url: /zh/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

有时您的 HTML 包含 1234567890123456 等长度超过 15 位的数字，当您将 HTML 导入 excel 文件时，这些数字会转换为指数表示法，例如 1.23457E+15。如果你愿意，你的数字应该原样导入而不是转换为指数表示法，那么请使用[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)属性并设置它**真的**在加载您的 HTML 时。

{{% /alert %}} 
## **从 HTML 导入时避免大数的指数表示法**
下面的示例代码解释了[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)财产。它会按原样导入数字，而不会将其转换为指数表示法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
