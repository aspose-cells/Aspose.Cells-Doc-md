---
title: 通过指定数据范围和 Sparkline 组的位置来复制 Sparkline
type: docs
weight: 120
url: /zh/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

通过在 MS Excel 中指定数据范围和 Sparkline 组的位置来复制 Sparkline

Microsoft Excel 允许您通过指定数据范围和 Sparkline 组的位置来复制 Sparkline。按照以下步骤将您的 Sparkline 复制到其他单元格。

- 选择包含您的 Sparkline 的单元格。
- 从 **设计** 选项卡内的 **Sparkline** 部分选择 **编辑数据**。
- 选择**编辑组位置和数据...**
- 指定数据范围和位置，然后单击确定。

## 示例

Aspose.Cells提供[**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection)方法来指定Sparkline组的数据范围和位置。

### 源和输出文件的屏幕截图

以下屏幕截图显示了在代码中使用的源Excel文件。红色高亮显示的区域显示了"**编辑组位置和数据...**"选项，用于指定Sparkline组的数据范围和位置。单元格P4显示了Sparkline，它将使用Aspose.Cells复制到其他四个填充有黄色的单元格中。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

以下屏幕截图显示了示例代码生成的输出Excel文件。正如您所看到的，单元格P4中的Sparkline已复制到列P中的接下来四个单元格，每个单元格使用不同的数据范围。

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### 通过指定Sparkline组的数据范围和位置来复制Sparkline的Java代码

以下示例代码加载了如上面屏幕截图所示的源Excel文件，然后访问第一个Sparkline组，并在Sparkline组内添加数据范围和位置。最后，将输出Excel文件写入磁盘，也如上面的屏幕截图所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
