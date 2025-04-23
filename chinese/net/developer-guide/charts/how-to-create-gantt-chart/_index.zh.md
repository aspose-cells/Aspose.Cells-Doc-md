---
title: 如何创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/net/how-to-create-gantt-chart/
description: 学习如何使用Aspose.Cells for .NET API创建甘特图。
keywords: 用C#创建甘特图、添加甘特图、插入甘特图。
---

## **什么是甘特图**

甘特图是一种条形图，显示项目时间表。它显示项目各个元素的开始和结束日期。每个任务或活动由一条条形表示，其长度对应持续时间。甘特图还显示任务之间的依赖关系，使项目管理者可以直观地看到任务的执行顺序。它在项目管理中广泛用于规划、排程和跟踪项目。

## **如何在Excel中创建甘特图**

你可以按照以下步骤在Excel中创建甘特图：
1. 添加一些用于甘特图的数据。 
<br>
<img src="00.png" width=50% />
1. 选择数据，点击插入 → 图表 → 插入簇状条形或柱形图 → 堆积条形图。在我们的示例中，是 B1:B7，然后插入 **堆积条形图**。
<br>
<img src="1.png" width=50% />

1. 选择图表，**选择数据** -> **添加**，设置 **系列名称** 和 **系列值** 如下。
<br>
<img src="2.png" width=50% />

1. 选择图表，编辑**横（类别）轴标签**。
<br>
<img src="3.png" width=50% />

1. **格式轴**，选择**类别逆序**以格式化Y轴。
1. 选择 **蓝色系列**，设置 **填充->无填充**。
1. **格式化轴**（X 轴），设置 **最小值和最大值**（2019年1月5日：43470，2019年1月30日：43494）。
<br>
<img src="4.png" width=50% />

1. 为图表**添加数据标签**，现在你将得到一个甘特图。
<br>
<img src="0.png" width=50% />


## **在Aspose.Cells中添加甘特图的方法。**
请查看以下示例代码。它加载包含一些示例数据的[示例Excel文件](sample.xlsx)，然后基于初始数据创建堆积柱状图，并设置相关属性。最后将工作簿保存为[输出XLSX](result.xlsx)。下方截图显示了由Aspose.Cells在输出Excel文件中创建的甘特图。
<br>
<img src="5.png" width=60% />

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
