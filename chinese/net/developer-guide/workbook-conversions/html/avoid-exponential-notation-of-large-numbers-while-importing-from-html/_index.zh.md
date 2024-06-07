---
title: 在从 HTML 导入时避免大数以指数形式显示
type: docs
weight: 10
url: /zh/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

有时您的 Html 包含如 1234567890123456 这样超过 15 位数的数字，当您将 HTML 导入到 Excel 文件时，这些数字将转换为指数形式，如 1.23457E+15。如果您希望数字被导入为原样而不转换为指数形式，请在加载 HTML 时使用 [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) 属性并将其设置为 **true**。

{{% /alert %}}

以下示例代码说明了 [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) 属性的用法。API 将按原样导入数字，而不将其转换为指数形式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
