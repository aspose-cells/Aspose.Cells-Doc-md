---
title: Finding Absolute Position of Shape in the Worksheet with Golang via C++
linktitle: Finding Absolute Position of Shape in the Worksheet
type: docs
weight: 8000
url: /go-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Determine the absolute position of a shape in a worksheet using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes, you need to know the absolute position of a shape in a worksheet. Aspose.Cells provides the [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/go-cpp/shape/getlefttocorner/) and [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) properties for this purpose. These properties return the absolute position of the shape in the worksheet in pixels.

{{% /alert %}}

The following sample code displays the absolute position of the first shape in the worksheet in pixels. The sample code displays the following console output:

{{< highlight java >}}

Absolute position of this shape is (320, 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindingAbsolutePositionOfShapeInsideTheWorksheet.go" >}}