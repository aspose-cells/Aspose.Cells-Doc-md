---
title: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for .NET API.
keywords: Find cell value starts with a single quote mark, Search cell value starts with a single quote mark
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells now provides the [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like `sample` and `'sample` etc.

{{% /alert %}}

The following sample code explains that strings like `sample` and `'sample` cannot be differentiated with the [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue) property. Therefore, we must use the [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) property to distinguish them.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
{{< app/cells/assistant language="csharp" >}}
