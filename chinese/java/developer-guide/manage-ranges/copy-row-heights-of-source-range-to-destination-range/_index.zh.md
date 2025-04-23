---
title: 将源范围行高度复制到目标范围
type: docs
weight: 250
url: /zh/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

有时用户需要将源范围的行高复制到目标范围。Aspose.Cells 提供 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) 枚举。设置 [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) 属性为 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) 时，源范围内所有行的行高将被复制到目标范围。

{{% /alert %}} 
## **将源范围的行高复制到目标范围**
以下示例代码演示如何使用 [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) 枚举，将源范围的行高复制到目标范围。一旦你在 Microsoft Excel 中打开由此代码生成的输出文件，你会发现目标范围的行高与源范围完全一致。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
