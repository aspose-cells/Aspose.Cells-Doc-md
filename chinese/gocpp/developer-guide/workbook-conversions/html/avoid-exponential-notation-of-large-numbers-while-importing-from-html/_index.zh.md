---
title: 在通过 Golang 通过 C++ 导入 HTML 时，避免使用指数符号表示大数字
linktitle: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 10
url: /zh/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: 学习如何在用编号Aspose.Cells for C++导入HTML时避免大数字的指数表示法。
---

{{% alert color="primary" %}}

有时候你的HTML包含像1234567890123456这样长于15位的数字，当你将HTML导入Excel时，这些数字会变成指数表示法如1.23457E+15。如果你希望数字按原样导入而不转换为指数形式，请在加载HTML时使用[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)属性并将其设置为**true**。

{{% /alert %}}

以下示例代码说明了[**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)属性的用法。API将按原样导入数字，而不将其转换为指数表示法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
