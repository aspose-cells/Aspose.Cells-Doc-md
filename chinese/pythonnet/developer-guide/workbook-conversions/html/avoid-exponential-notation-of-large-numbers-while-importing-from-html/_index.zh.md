---
title: 在从 HTML 导入时避免大数以指数形式显示
type: docs
weight: 10
url: /zh/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: 本主题向您展示在从HTML导入时如何避免大数字使用指数表示法，使用Aspose.Cells for Python via NET。
keywords: 在从 HTML 导入时避免对大数字使用指数表示法，导入 HTML 时保持精度。
---

{{% alert color="primary" %}}

有时您的 Html 包含如 1234567890123456 这样超过 15 位数的数字，当您将 HTML 导入到 Excel 文件时，这些数字将转换为指数形式，如 1.23457E+15。如果您希望数字被导入为原样而不转换为指数形式，请在加载 HTML 时使用 [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) 属性并将其设置为 **true**。

{{% /alert %}}

以下示例代码说明了 [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) 属性的用法。API 将按原样导入数字，而不将其转换为指数形式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
