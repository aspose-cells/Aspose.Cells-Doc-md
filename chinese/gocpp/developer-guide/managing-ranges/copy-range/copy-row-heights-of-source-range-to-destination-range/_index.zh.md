---
title: 使用C++通过Golang将源范围的行高复制到目标范围
linktitle: 将源范围行高度复制到目标范围
type: docs
weight: 590
url: /zh/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: 学习如何使用 Aspose.Cells for C++ 将行高从源范围复制到目标范围。
---

{{% alert color="primary" %}}

有时用户需要将行高从源范围复制到目标范围。Aspose.Cells 提供了 [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) 枚举来实现这一点。当你用 [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) 枚举设置 [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) 属性时，源范围内所有行的高度将被复制到目标范围。

{{% /alert %}}

以下示例代码演示了如何使用 [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) 枚举将行高从源范围复制到目标范围。将此代码生成的 Excel 文件在 Microsoft Excel 中打开后，你会看到目标范围的行高与源范围完全一致。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
