---
title: 如何创建龙卷风图表
type: docs
weight: 73
url: /zh/net/create-tornado-chart/
description: 学习如何使用Aspose.Cells for .NET创建风暴图表。
keywords: C#创建龙卷风图表，添加龙卷风图表，插入龙卷风图表
---

## **介绍**
龙卷风图表，也称为龙卷风图或龙卷风图，是一种常用于Excel中的敏感性分析的数据可视化类型。它帮助您理解变量变化对特定结果或结果的影响。

## **如何在Excel中创建龙卷风图表**
您可以通过以下步骤在Excel中创建龙卷风图表：
1. 选择数据并转到插入 --> 图表 --> 插入柱状图或条形图 --> 堆积柱状图。点击。
<br>
<img src="1.png" width=70% />
2. 更改Y轴：右键单击Y轴。点击格式轴。在标签中，点击标签位置下拉菜单并选择低项。
<br>
<img src="2.png" width=70% />
3. 选择任何柱并进行格式设置。设置适当的间距宽度。
<br>
<img src="3.png" width=70% />
4. 让我们从龙卷风图表中删除减号（-）。选择X轴。转到格式设置。在轴选项中，点击数字。在类别中，选择自定义。在格式代码中写入###0,###0。点击添加。
<br>
<img src="4.png" width=70% />
5. 点击Y轴并转到轴选项。在轴选项中，勾选倒序显示的类别。
<br>
<img src="5.png" width=70% />

## **如何在Aspose.Cells中添加龙卷风图表**
请参阅以下示例代码。它加载包含一些示例数据的[示例Excel文件](sample.xlsx)。然后根据初始数据创建堆叠条形图表，并设置相关属性。最后，将工作簿保存到[输出XLSX格式](out.xlsx)。以下截图显示了Aspose.Cells在输出Excel文件中创建的龙卷风图表。
<br>
<img src="6.png" width=70% />

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
