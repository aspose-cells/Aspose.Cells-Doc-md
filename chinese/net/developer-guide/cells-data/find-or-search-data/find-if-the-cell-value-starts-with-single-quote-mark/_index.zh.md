---
title: 查找单元格值是否以单引号开头
type: docs
weight: 270
url: /zh/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: 了解如何通过 Aspose.Cells for .NET API 查找单元格值是否以单引号开头。
keywords: Find cell value starts with a single quote mark, Search cell value starts with a single quote mark
---
{{% alert color="primary" %}}

 Aspose.Cells现在提供[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)属性来查找单元格值是否以单引号开头。在此属性之前，无法区分诸如“sample”和“'sample”等字符串。

{{% /alert %}}

下面的示例代码解释了像sample和'sample这样的字符串不能用[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)财产。因此我们必须使用[**样式.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)属性来区分它们。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
