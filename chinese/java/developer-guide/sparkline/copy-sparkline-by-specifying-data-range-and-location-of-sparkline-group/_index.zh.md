---
title: 通过指定迷你图组的数据范围和位置来复制迷你图
type: docs
weight: 120
url: /zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
通过在 MS Excel 中指定数据范围和迷你图组的位置来复制迷你图

Microsoft Excel 允许您通过指定迷你图组的数据范围和位置来复制迷你图。按照以下步骤将您的迷你图复制到其他单元格。

- 选择包含迷你图的单元格。
- 选择**编辑数据**来自**迷你图**里面的部分**设计**标签
- 选择**编辑组位置和数据...**
- 指定数据范围和位置并单击确定。

## 例子

Aspose.Cells 提供了[**SparklineCollection.add（数据范围、行、列）**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection)指定迷你图组的数据范围和位置的方法。

### 源文件和输出文件的屏幕截图

以下屏幕截图显示了代码中使用的源 Excel 文件。红色高亮区域显示“**编辑组位置和数据...**" 选项指定迷你图组的数据范围和位置。单元格 P4 显示迷你图，它将使用 Aspose.Cells 复制到其他四个填充黄色的单元格。

![待办事项：图片_替代_文本](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

以下屏幕截图显示了示例代码生成的输出 Excel 文件。如您所见，单元格 P4 中的迷你图已复制到列 P 中接下来的四个单元格，每个单元格具有不同的数据范围。

![待办事项：图片_替代_文本](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java 通过指定迷你图组的数据范围和位置来复制迷你图的代码

以下示例代码加载源 Excel 文件，如上面的屏幕截图所示，然后访问第一个迷你图组并在迷你图组内添加数据范围和位置。最后，它将输出的 Excel 文件写入磁盘，如上图所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
