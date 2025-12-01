---
title: Copy Range Data with Style
type: docs
weight: 610
url: /python-net/copy-range-data-with-style/
description: This article describes how to Copy Range Data with Style with Aspose.Cells for Python via .NET library.
keywords: Python Excel Library, Python How to Copy Range Data with Style, Python How to Copy Range Data with Style with python excel library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/python-net/copy-range-data-only/) explained how to copy the data from a range of cells to another range. Specifically, it process applied a new set of styles to the copied cells. Aspose.Cells for Python via .NET can also copy a range complete with formatting. This article explains how.

{{% /alert %}}

Aspose.Cells for Python via .NET provides a range of classes and methods for working with ranges, for example, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) and [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

This example:

1. Creates a workbook.
1. Fills a number of cells in the first worksheet with data.
1. Creates a [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Creates a [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object with specified formatting attributes.
1. Applies the style to the data range.
1. Creates a second range of cells.
1. Copies data with the formatting from the first range to the second range.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
