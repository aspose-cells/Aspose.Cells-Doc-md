---
title: 通过指定数据范围和Sparkline组的位置复制Sparkline
type: docs
weight: 120
url: /zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

在 MS Excel 中通过指定数据范围和 Sparkline 分组的位置复制 Sparkline

Microsoft Excel 允许您通过指定数据范围和 Sparkline 组的位置来复制 Sparkline。按照以下步骤将您的 Sparkline 复制到其他单元格。

- 选择包含您的 Sparkline 的单元格。
- 从“设计”选项卡内的“Sparkline”部分中选择“编辑数据”。
- 选择“编辑分组位置和数据...”
- 指定数据范围和位置，然后单击确定。

## 示例

Aspose.Cells 提供 [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) 方法来指定 Sparkline 组的数据范围和位置。

### 源文件和输出文件的屏幕截图

下面的屏幕截图显示了代码中使用的源 Excel 文件。 红色高亮显示区域显示了“**编辑分组位置和数据...**”选项，以指定 Sparkline 组的数据范围和位置。 单元格 P4 显示了将使用 Aspose.Cells 复制到填充有黄色的其他四个单元格的 Sparkline。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

下面的屏幕截图显示了样品代码生成的输出 Excel 文件。 如您所见，单元格 P4 中的 Sparkline 已复制到 P 列中的下一个四个单元格，每个单元格都具有不同的数据范围。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### 通过指定 Sparkline 组的数据范围和位置复制 Sparkline 的 Java 代码

下面的示例代码加载了上面屏幕截图中显示的源 Excel 文件，然后访问了第一个 Sparkline 组，并在 Sparkline 组内添加了数据范围和位置。 最后，它将输出 Excel 文件写入磁盘，也显示了上面的屏幕截图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
