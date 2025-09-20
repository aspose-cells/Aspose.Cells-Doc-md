---
title: Copy Range Data with Style in C++
linktitle: Copy Range Data with Style
type: docs
weight: 610
url: /go-cpp/copy-range-data-with-style/
description: Copy range data including cell styles in Excel files using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/cpp/copy-range-data-only/) explained how to copy cell data between ranges. This article demonstrates how to copy cell ranges while preserving their formatting styles using Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells provides classes and methods for working with ranges including [**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), and [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

This example demonstrates how to:

1. Create a workbook
1. Populate cells with data
1. Create a [**Range**](https://reference.aspose.com/cells/go-cpp/range/)
1. Create and configure a [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object
1. Apply styles to the range
1. Create a second range
1. Copy formatted data between ranges

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}