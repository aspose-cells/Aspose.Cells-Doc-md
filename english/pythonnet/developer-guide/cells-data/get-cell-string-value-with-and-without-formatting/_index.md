---
title: Get Cell String Value with Format Strategy
type: docs
weight: 240
url: /python-net/get-cell-string-value-with-format-strategy/
description: Learn how to get cell string value with and without formatting through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get Cell String Value with and without Formatting, Python Retrieve Cell String Value with and without Formatting, Python Obtain Cell String Value with and without Formatting
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides a method [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) which can be used to get the string value of the cell with or without any formatting. Suppose you have a cell with value 0.012345 and you have formatted it to display two decimal places only. It will then display as 0.01 in Excel. You can retrieve string values both as 0.01 and as 0.012345 using the [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) method. It takes [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) enum as a parameter, which has the following values:

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

The following sample code explains the use of [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
