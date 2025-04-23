---
title: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 10
url: /zh/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

有时您的HTML中包含长达15位数的数字1234567890123456，当您将HTML导入到Excel文件时，这些数字会转换为1.23457E+15这样的指数表示。如果您希望数字被原样导入而不是转换为指数表示，则请在加载HTML时使用[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)属性并将其设置为**true**。

{{% /alert %}}

以下示例代码说明了[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)属性的用法。API将原样导入数字，而不将其转换为指数表示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
