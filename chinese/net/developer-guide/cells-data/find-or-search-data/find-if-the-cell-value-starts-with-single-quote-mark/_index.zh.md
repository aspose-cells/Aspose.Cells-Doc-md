---
title: 通过 Aspose.Cells for .NET API 学习如何查找单元格值是否以单引号标记开头。
type: docs
weight: 270
url: /zh/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: 通过 Aspose.Cells for .NET API 学习如何查找单元格值是否以单引号标记开头。
keywords: 查找单元格值是否以单引号标记开头，搜索单元格值是否以单引号标记开头
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 属性来查找单元格值是否以单引号标记开头。在引入此属性之前，无法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

以下示例代码解释了类似 sample 和 'sample 无法通过 [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) 属性区分的情况。因此，我们必须使用 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 属性来区分它们。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
