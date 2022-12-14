---
title: 使用迷你图和设置 3D 格式
type: docs
weight: 40
url: /zh/java/using-sparklines-and-settings-3d-format/
---
## **使用迷你图**
Microsoft Excel 2010 可以以比以往更多的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。迷你图是可以放置在单元格内的迷你图表，以便您可以在同一个表格中查看数据和图表。当正确使用迷你图时，数据分析会更快、更切题。它们还提供了一个简单的信息视图，避免了带有大量繁忙图表的过度拥挤的工作表。

Aspose.Cells 提供了一个 API 用于在电子表格中操作迷你图。
### **Microsoft Excel 中的迷你图**
要在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了便于查看，请选择数据旁边的单元格。
1. 点击**插入**在功能区上，然后选择**柱子**在里面**迷你图**团体。
1. 选择或输入工作表中包含源数据的单元格区域。图表将出现。

迷你图可帮助您查看趋势，例如垒球联赛的输赢记录。迷你图甚至可以总结联盟中每支球队的整个赛季。
### **使用 Aspose.Cells 的迷你图**
开发者可以使用Aspose.Cells提供的API创建、删除或读取sparklines（在模板文件中）。管理sparklines的类包含在[Aspose.Cells.Charts](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)命名空间，因此您需要在使用这些功能之前导入此命名空间。

通过为给定的数据范围添加自定义图形，开发人员可以自由地将不同类型的微型图表添加到选定的单元格区域。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 阅读工作表的迷你图信息。
1. 将给定数据范围的新迷你图添加到单元格区域。
1. 将 Excel 文件保存到磁盘。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparkLine.java" >}}
## **设置 3D 格式**
您可能需要 3D 图表样式，以便您可以只获得场景的结果。 Aspose.Cells确实提供了相关的API应用Microsoft Excel 2007 3D格式。

下面给出了一个完整的示例来演示如何创建图表和应用 Microsoft Excel 2007 3D 格式。执行示例代码后，工作表中将添加一个柱形图（具有 3D 效果）。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat.java" >}}
