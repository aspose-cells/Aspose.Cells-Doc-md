---
title: 将源范围的行高复制到目标范围
type: docs
weight: 590
url: /zh/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

有时用户需要将源范围的行高复制到目标范围。Aspose.Cells 提供了 [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) 枚举来实现这个目的。当您将 [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) 属性与 [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) 枚举一起设置时，源范围内所有行的高度都将复制到目标范围。

{{% /alert %}}

以下示例代码解释了如何使用 [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) 枚举将源范围的行高复制到目标范围。一旦您在Microsoft Excel中打开此代码生成的输出Excel文件，您会看到目标范围的行高与源范围的行高完全相同。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
