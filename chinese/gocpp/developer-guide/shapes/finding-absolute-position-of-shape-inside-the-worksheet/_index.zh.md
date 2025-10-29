---
title: 用 Golang 通过 C++ 查找工作表中形状的绝对位置。
linktitle: 查找工作表内形状的绝对位置
type: docs
weight: 8000
url: /zh/go-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: 使用 Aspose.Cells 通过 C++ 和 Golang 确定形状在工作表中的绝对位置。
---

{{% alert color="primary" %}}

有时，您需要知道工作表中形状的绝对位置。Aspose.Cells提供了 [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/go-cpp/shape/getlefttocorner/) 和 [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) 属性来实现这一目的。这些属性返回形状在工作表中的绝对位置（以像素为单位）。

{{% /alert %}}

以下示例代码显示了工作表中第一个形状的绝对位置（以像素为单位）。示例代码显示了以下控制台输出：

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindingAbsolutePositionOfShapeInsideTheWorksheet.go" >}}
