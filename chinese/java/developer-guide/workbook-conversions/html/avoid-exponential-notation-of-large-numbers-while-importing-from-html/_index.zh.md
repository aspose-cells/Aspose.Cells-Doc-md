---
title: 在从 HTML 导入时避免大数以指数形式显示
type: docs
weight: 600
url: /zh/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

有时您的 HTML 包含长达 15 位的数字（例如 1234567890123456），当您将 HTML 导入到 Excel 文件时，这些数字会转换为指数表示法，如 1.23457E+15。如果您希望，您的数字应按原样导入而不转换为指数表示法，则在加载 HTML 时请使用 [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) 属性并将其设置为 **true**。

{{% /alert %}} 
## **在从 HTML 导入时避免大数的指数表示法**
以下示例代码解释了 [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) 属性的用法。它将按原样导入数字而不将其转换为指数表示法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
