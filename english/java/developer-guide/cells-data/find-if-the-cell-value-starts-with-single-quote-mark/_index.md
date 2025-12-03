---
title: Find if the cell value starts with single quote mark
type: docs
weight: 610
url: /java/find-if-the-cell-value-starts-with-single-quote-mark/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells now provides the [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#getQuotePrefix--) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}} 
## **Find if the cell value starts with single quote mark**
The following sample code explains that the strings like sample and 'sample cannot be differentiated with [Cell.StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue--) property. Therefore we must use [Style.QuotePrefix](https://reference.aspose.com/cells/java/com.aspose.cells/style#getQuotePrefix--) property to distinguish them.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-DetectCellValueStartsWithSingleQuote.java" >}}
{{< app/cells/assistant language="java" >}}
