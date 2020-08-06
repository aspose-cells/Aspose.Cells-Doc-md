---
title: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /net/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells now provides the [Style.QuotePrefix](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/quoteprefix) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}} 

The following sample code explains that the strings like sample and 'sample cannot be differentiated with [Cell.StringValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/properties/stringvalue) property. Therefore we must use [Style.QuotePrefix](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/quoteprefix) property to distinguish them.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
