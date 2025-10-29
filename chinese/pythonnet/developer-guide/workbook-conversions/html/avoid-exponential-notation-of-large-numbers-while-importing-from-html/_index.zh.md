---
title: 在从HTML导入时避免大数字的指数表示
type: docs
weight: 10
url: /zh/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: 此主题介绍如何使用Aspose.Cells for Python via NET从HTML中导入时避免大数字的指数表示
keywords: 在从HTML导入时避免大数字的指数表示，保留导入HTML时的精度
---

{{% alert color="primary" %}}

有时您的HTML中包含长达15位数的数字1234567890123456，当您将HTML导入到Excel文件时，这些数字会转换为1.23457E+15这样的指数表示。如果您希望数字被原样导入而不是转换为指数表示，则请在加载HTML时使用[**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)属性并将其设置为**true**。

{{% /alert %}}

以下示例代码说明了[**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)属性的用法。API将原样导入数字，而不将其转换为指数表示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
