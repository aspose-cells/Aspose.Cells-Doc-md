---
title: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: 使用Aspose.Cells for .NET API学习如何查找单元格值是否以单引号标记开头。
keywords: 查找单元格值是否以单引号标记开始，搜索单元格值是否以单引号标记开始
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了属性 [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 来查找单元格值是否以单引号标记开始。在此属性之前，无法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

下面的示例代码解释了像“sample”和“'sample”这样的字符串不能通过[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)属性进行区分。因此，我们必须使用[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)属性对它们进行区分。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
