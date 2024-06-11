---
title: 将源范围行高度复制到目标范围
type: docs
weight: 250
url: /zh/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

有时用户需要将源范围的行高度复制到目标范围。Aspose.Cells 提供了 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) 枚举来实现这一目的。当您将 [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) 属性设置为 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) 枚举时，源范围内所有行的高度将被复制到目标范围。

{{% /alert %}} 
## **将源范围的行高复制到目标范围**
以下示例代码解释了如何使用 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) 枚举将源范围的行高度复制到目标范围。一旦您在 Microsoft Excel 中打开此代码生成的输出 Excel 文件，您会发现目标范围的行高度与源范围的行高度完全相同。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
