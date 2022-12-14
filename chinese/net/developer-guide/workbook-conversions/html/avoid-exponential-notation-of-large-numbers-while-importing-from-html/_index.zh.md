---
title: 从 HTML 导入时避免大数的指数表示法
type: docs
weight: 10
url: /zh/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

有时，您的 Html 包含 1234567890123456 等长度超过 15 位的数字，当您将 HTML 导入 excel 文件时，这些数字会转换为指数表示法，例如 1.23457E+15。如果你愿意，你的数字应该原样导入而不是转换为指数表示法，那么请使用[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)属性并设置它**真的**在加载您的 HTML 时。

{{% /alert %}}

下面的示例代码解释了[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)财产。 API 将按原样导入数字，而不将其转换为指数表示法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
