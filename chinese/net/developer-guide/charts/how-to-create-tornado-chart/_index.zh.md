---
title: 如何创建龙卷风图表
type: docs
weight: 73
url: /zh/net/create-tornado-chart/
description: 了解如何使用 Aspose.Cells for .NET API 创建龙卷风图表。
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **介绍**
龙卷风图，也称为龙卷风图或龙卷风图，是一种数据可视化类型，常用于 Excel 中的敏感性分析。它可以帮助您了解变量变化对特定结果或结果的影响。

##  **如何在 Excel 中创建龙卷风图表**
您可以按照以下步骤在 Excel 中创建龙卷风图表：
1. 选择数据并转到插入 --> 图表 --> 插入柱形图或条形图 --> 堆叠条形图。点击它。
<br>
<img src="1.png" width=70% />
2. 更改 Y 轴：右键单击 y 轴。单击格式轴。在标签中，单击标签位置下拉列表并选择低项目。
<br>
<img src="2.png" width=70% />
3. 选择任意栏并转到格式设置。设置合适的间隙宽度。
<br>
<img src="3.png" width=70% />
4. 让我们从龙卷风图中删除减号 (-)。选择 x 轴。转到格式化。在轴选项中，单击数字。在类别中，选择自定义。在格式代码中写入###0、###0。单击添加。
<br>
<img src="4.png" width=70% />
5. 单击 y 轴并转到轴选项。在“轴”选项中，按相反顺序选中“类别”。
<br>
<img src="5.png" width=70% />

##  **如何在 Aspose.Cells 中添加龙卷风图表**
请参阅以下示例代码。它加载了[Excel 文件示例](sample.xlsx)其中包含一些示例数据。然后，它根据初始数据创建堆积条形图并设置相关属性。最后，它将工作簿保存到[输出XLSX格式](out.xlsx)。以下屏幕截图显示了输出 Excel 文件中 Aspose.Cells 创建的龙卷风图表。
<br>
<img src="6.png" width=70% />

###  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}