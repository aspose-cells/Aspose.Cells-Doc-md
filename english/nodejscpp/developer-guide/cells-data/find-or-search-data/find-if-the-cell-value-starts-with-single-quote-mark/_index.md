---
title: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for Node.js via C++ API.
keywords: Find cell value starts with a single quote mark Node.js via C++, Search cell value starts with a single quote mark Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells now provides the [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) method to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}}

The following sample code explains that the strings like sample and 'sample cannot be differentiated with [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) method. Therefore we must use [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) method to distinguish them.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

