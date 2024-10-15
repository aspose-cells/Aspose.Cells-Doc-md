---
title: Copy Range Data with Style
type: docs
weight: 610
url: /net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/net/copy-range-data-only/) explained how to copy the data from a range of cells to another range. Specifically, it process applied a new set of styles to the copied cells. Aspose.Cells can also copy a range complete with formatting. This article explains how.

{{% /alert %}}

Aspose.Cells provides a range of classes and methods for working with ranges, for example, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) and [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

This example:

1. Creates a workbook.
1. Fills a number of cells in the first worksheet with data.
1. Creates a [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Creates a [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object with specified formatting attributes.
1. Applies the style to the data range.
1. Creates a second range of cells.
1. Copies data with the formatting from the first range to the second range.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}