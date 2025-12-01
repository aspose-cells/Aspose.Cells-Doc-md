---
title: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Find cell value starts with a single quote mark, Python Search cell value starts with a single quote mark
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET now provides the [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}}

The following sample code explains that the strings like sample and 'sample cannot be differentiated with [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/) property. Therefore we must use [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) property to distinguish them.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
{{< app/cells/assistant language="python-net" >}}
