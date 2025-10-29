---
title: 使用Sparklines和设置3D格式
type: docs
weight: 40
url: /zh/python-net/using-sparklines-and-settings-3d-format/
---

## **使用迷你图**
Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。 Sparklines是迷你图，可以放置在单元格内，以便您可以在同一张表格中查看数据和图表。当Sparklines被正确使用时，数据分析更快捷、更简洁。它们还提供信息的简单视图，避免了拥挤的工作表和繁忙的图表。

Aspose.Cells for Python via .NET提供了操作电子表格中迷你图的API。
### **Microsoft Excel 中的迷你图**
如何在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了方便查看，选择数据旁边的单元格。
1. 在功能区上单击**插入**，然后在**迷你图**组中选择**柱**。
1. 选择或输入包含源数据的工作表中的单元格范围。图表将出现。

迷你图可帮助您查看趋势，例如垒球联赛的胜负记录。迷你图甚至可以总结联赛中每支队伍整个赛季的情况。
### **使用Aspose.Cells for Python via .NET制作迷你图**
开发者可以使用Aspose.Cells for Python via .NET的API创建、删除或读取模板文件中的迷你图（在模板文件中）。管理迷你图的类包含在[aspose.cells.charts](https://reference.aspose.com/cells/python-net/aspose.cells.charts)命名空间中，因此在使用这些功能之前需要导入该命名空间。

通过为给定的数据范围添加自定义图形，开发人员可以自由地向选定的单元区域添加不同类型的迷你图。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围向单元区域添加新的迷你图。
1. 将 Excel 文件保存到磁盘。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-UsingSparklines-1.py" >}}
## **设置 3D 格式**
您可能需要3D图表样式，以便专门获取适合您的场景的结果。Aspose.Cells for Python via .NET提供了相关API，用于应用Microsoft Excel 2007 3D格式。

下面给出了一个完整的示例，演示如何创建图表并应用 Microsoft Excel 2007 的 3D 格式。执行示例代码后，工作表中将添加一个带有 3D 效果的柱状图。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-Applying3DFormat-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
