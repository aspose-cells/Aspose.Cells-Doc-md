---
title : "Find if the cell value starts with single quote mark" 
description : "" 
weight : 12528 
toc : false
type: docs
url: /java/developerguide/technicalarticles/find+if+the+cell+value+starts+with+single+quote+mark/
---

# Aspose.Cells for Java : Find if the cell value starts with single quote mark



Aspose.Cells now provides the [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like `sample` and `'sample` etc.

#### Find if the cell value starts with single quote mark

The following sample code explains that the strings like `sample` and `'sample` cannot be differentiated with [Cell.StringValue](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#StringValue) property. Therefore we must use [Style.QuotePrefix](https://apireference.aspose.com/java/cells/com.aspose.cells/style#QuotePrefix) property to distinguish them.

