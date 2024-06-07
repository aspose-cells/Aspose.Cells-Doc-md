---
title: 使用迷你图和设置3D格式
type: docs
weight: 40
url: /zh/net/using-sparklines-and-settings-3d-format/
---

## **使用迷你图**
Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户通过新的数据分析和可视化工具追踪和突出重要的数据趋势。迷你图是一种迷你图表，您可以将其放在单元格内，以便同时查看数据和图表。正确使用迷你图，可以加快数据分析的速度并更直观。它们还提供信息的简单视图，避免了使用许多繁杂图表的拥挤工作表。

Aspose.Cells提供了一个API来操作电子表格中的迷你图。
### **Microsoft Excel中的迷你图**
在Microsoft Excel 2010中插入迷你图：

1. 选择要显示迷你图的单元格。为了便于查看，选择数据旁边的单元格。
1. 在功能区上单击 **插入**，然后在 **迷你图** 组中选择 **列**。
1. 选择或输入工作表中包含源数据的单元格范围。图表将显示。

迷你图帮助您查看趋势，例如软式联赛的胜负记录。迷你图甚至可以总结每支球队整个赛季的情况。
### **使用Aspose.Cells进行迷你图**
开发人员可以使用Aspose.Cells提供的API创建、删除或读取（在模板文件中的）迷你图。管理迷你图的类包含在[Aspose.Cells.Charts](https://reference.aspose.com/cells/net/aspose.cells.charts)命名空间中，因此在使用这些特性之前，您需要导入此命名空间。

通过为给定的数据范围添加自定义图形，开发人员可以自由添加不同类型的迷你图表到选定的单元格区域。

以下示例演示了迷你图功能。示例显示如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围添加新的迷你图到单元格区域。
1. 将Excel文件保存到磁盘。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-UsingSparklines-1.cs" >}}
## **设置3D格式**
您可能需要3D图表样式，以便获取适合您场景的结果。Aspose.Cells确实提供了相关的API来应用Microsoft Excel 2007的3D格式。

下面给出一个完整的示例，演示如何创建一个图表并应用Microsoft Excel 2007的3D格式。执行示例代码后，将向工作表中添加一个带有3D效果的柱形图。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-Applying3DFormat-1.cs" >}}
