---
title: Find if the cell value starts with single quote mark
type: docs
weight: 610
url: /java/find-if-the-cell-value-starts-with-single-quote-mark/
---

{{% alert color="primary" %}} 

Aspose.Cells now provides the [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}} 
#### **Find if the cell value starts with single quote mark**
The following sample code explains that the strings like sample and 'sample cannot be differentiated with [Cell.StringValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#StringValue) property. Therefore we must use [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) property to distinguish them.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Articles-DetectCellValueStartsWithSingleQuote.java" >}}
