---
title: 图表类型
type: docs
weight: 10
url: /zh/java/chart-types/
---

{{% alert color="primary" %}} 

图表是信息的可视化显示。Aspose.Cells允许开发人员像Microsoft Excel一样在图表中可视化信息。以图表方式呈现信息对于决策者快速做出及时决策总是有帮助的。通过图表比较、模式和数据趋势比原始数字更容易快速看到。根据电子表格中的数据在运行时创建图表是Aspose.Cells最强大的功能之一。

{{% /alert %}} 
## **图表类型**
Aspose.Cells支持几乎所有Microsoft Excel支持的图表类型。图表分为两大类别：

- [标准类型](/cells/zh/java/chart-types/)
- [自定义类型](/cells/zh/java/chart-types/)
### **标准类型**
标准图表通常使用标准格式：

|<p>- [列](/cells/zh/java/chart-types/)</p><p>- [柱形](/cells/zh/java/chart-types/)</p><p>- [折线](/cells/zh/java/chart-types/)</p><p>- [饼图](/cells/zh/java/chart-types/)</p><p>- [散点](/cells/zh/java/chart-types/)</p><p>- [面积](/cells/zh/java/chart-types/)</p><p>- [圆环图](/cells/zh/java/chart-types/)</p>|<p>- [雷达图](/cells/zh/java/chart-types/)</p><p>- [3D 曲面图](/cells/zh/java/chart-types/)</p><p>- [气泡图](/cells/zh/java/chart-types/)</p><p>- [股票图](/cells/zh/java/chart-types/)</p><p>- [圆柱](/cells/zh/java/chart-types/)</p><p>- [圆锥](/cells/zh/java/chart-types/)</p><p>- [金字塔](/cells/zh/java/chart-types/)</p><p>- [树状图](/cells/zh/java/chart-types/)</p><p>- [日晷图](/cells/zh/java/chart-types/)</p><p>- [直方图](/cells/zh/java/chart-types/)</p><p>- [箱形图](/cells/zh/java/chart-types/)</p><p>- [瀑布图](/cells/zh/java/chart-types/)</p>|
| :- | :- |
下面将更详细地描述每种标准图表类型。
#### **柱形图**
柱形图使用垂直条（称为柱）来显示一个或多个数据项的不同值。柱形图通常用于比较不同类别之间的值。它们非常适合显示一个项目的值随时间的变化，例如，在进行预算分析时。

**Microsoft Excel支持的柱状图** 

![todo:image_alt_text](chart-types_1.png)

Aspose.Cells支持以下柱形图类型：

- Clustered column chart
- Stacked column chart
- 100% stacked column chart
- 3D clustered column chart
- 3D stacked column chart
- 3D 100% stacked column chart
- 3D column chart
#### **条形图**
条形图与柱状图几乎是相同类型，区别在于它们使用水平条而不是垂直条。

**Microsoft Excel支持的条形图** 

![todo:image_alt_text](chart-types_2.png)

Aspose.Cells支持以下条形图:

- Clustered bar chart
- Stacked bar chart
- 100% stacked bar chart
- 3D clustered bar chart
- 3D stacked bar chart
- 3D 100% stacked bar chart
#### **折线图**
折线图利用线条显示信息。这些图表非常有用，能够展示随时间的暂时变化，并经常用于显示多个项目的价值随时间变化的波动。

**Microsoft Excel支持的折线图** 

![todo:image_alt_text](chart-types_3.png)

Aspose.Cells支持以下折线图:

- Simple line chart
- Stacked line chart
- 100% stacked line chart
- Line chart with data markers
- Stacked line chart with data markers
- 100% stacked line chart with data markers
- 3D line chart

{{% alert color="primary" %}} 

数据标记用于表示数据点，即图表中绘制的单个值。相同颜色的数据标记构成一个数据系列。

{{% /alert %}} 
#### **饼图**
饼图主要用于在想要表示整体不同部分或总数百分比时显示信息。

**Microsoft Excel支持的饼图** 

![todo:image_alt_text](chart-types_4.png)

Aspose.Cells支持以下饼图:

- Simple pie chart
- 3D pie chart
- Pie of pie chart
- Exploded pie chart
- 3D exploded pie chart
- Bar of pie chart
#### **散点图**
散点图主要用于统计学中，通过在水平（"X"）和垂直（"Y"）轴上各有一个坐标的有限点进行可视化显示和比较两组相关的定量或数值数据。

**Microsoft Excel支持的散点图** 

![todo:image_alt_text](chart-types_5.png)

Aspose.Cells支持以下散点图：

- Simple scatter chart
- Scatter chart connected by curves, with data markers
- Scatter chart connected by curves, without data markers
- Scatter chart connected by lines, with data markers
- Scatter chart connected by lines, without data markers
#### **面积图**
面积图是一种线图，其中每个区域都被赋予固体颜色或图案，以突出图表信息之间的关系。

**Microsoft Excel支持的面积图** 

![todo:image_alt_text](chart-types_6.png)

Aspose.Cells支持以下面积图：

- Simple area chart
- Stacked area chart
- 100% stacked area chart
- 3D area chart
- 3D stacked area chart
- 3D 100% stacked area chart
#### **圆环图**
圆环图类似于饼图，主要用于显示数据的比例如何对整体产生影响。

**Microsoft Excel支持的环形饼图** 

![todo:image_alt_text](chart-types_7.png)

Aspose.Cells支持以下圆环图：

- Simple doughnut chart
- Exploded doughnut chart
#### **雷达图**
雷达图在您想要查看与一项相关的几个不同因素时非常有用。这些图表有多个轴，可以沿着这些轴绘制数据。

**Microsoft Excel支持的雷达图** 

![todo:image_alt_text](chart-types_8.png)

下面的雷达图在Aspose.Cells中受支持:

- Simple radar chart
- Radar chart with data markers
- Filled radar chart
#### **表面3D图表**
与其他3D图表一样，表面3D图表基于X、Y和Z轴。这些图表有助于显示根据另外两个变量“X”和“Y”中的"Z"变量的变化。

**Microsoft Excel支持的表面3D图表** 

![todo:image_alt_text](chart-types_9.png)

Aspose.Cells支持以下表面3D图表:

- 3D surface chart
- Wireframe 3D surface chart
- Surface contour chart
- Wireframe contour chart
#### **气泡图**
气泡图是散点图的一种变体，其中数据点被气泡代替。如果您的数据包含三个包含一组值的数据系列，可以使用气泡图代替散点图。气泡图主要用于显示财务数据。

**Microsoft Excel支持的气泡图** 

![todo:image_alt_text](chart-types_10.png)

Aspose.Cells支持以下气泡图:

- Simple bubble chart
- 3D bubble chart
#### **股票图**
股票图主要用于股票价格数据，但也可用于科学数据.

**Microsoft Excel支持的股票图** 

![todo:image_alt_text](chart-types_11.png)

Aspose.Cells支持以下股票图:

- High-low-close stock chart
- Open-high-low-close stock chart
- Volume-high-low-close stock chart
- Volume-open-high-low-close stock chart
#### **圆柱图**
这些图表类型使用圆柱形数据标记，可为柱状图、条形图和3D柱状图增添戏剧效果。

**Microsoft Excel支持的圆柱图** 

![todo:image_alt_text](chart-types_12.png)

Aspose.Cells支持以下圆柱图:

- Simple cylinder chart
- Stacked cylinder chart
- 100% stacked cylinder chart
- Cylindrical bar chart
- Stacked cylindrical bar chart
- 100% stacked cylindrical bar chart
- 3D cylindrical column chart
#### **锥形图**
这些图表类型使用锥形数据标记，给柱状图、条形图和3D柱状图带来戏剧效果。 

![todo:image_alt_text](chart-types_13.png)


**Microsoft Excel支持的圆锥图**

Aspose.Cells支持以下锥形图表:

- Simple cone chart
- Stacked cone chart
- 100% stacked cone chart
- Conical bar chart
- Stacked conical bar chart
- 100% stacked conical bar chart
- 3D conical column chart
#### **金字塔图表**
这些图表类型使用金字塔数据标记，给柱状图、条形图和3D柱状图带来戏剧效果。

**Microsoft Excel支持的金字塔图** 

![todo:image_alt_text](chart-types_14.png)

Aspose.Cells支持以下金字塔图表:

- Simple pyramid chart
- Stacked pyramid chart
- 100% stacked pyramid chart
- Pyramid bar chart
- Stacked pyramid bar chart
- 100% stacked pyramid bar chart
- 3D pyramid column chart
#### **树状图**
树状图提供了数据的分层视图，帮助用户发现模式，比如哪些商品是店铺的畅销商品。树形分支由矩形表示，每个子分支显示为较小的矩形。树状图通过颜色和相似性显示类别，并可以轻松显示大量数据，其他图表类型难以做到这一点。

Aspose.Cells支持树状图。

#### **日光辐射图**
旭日图适用于显示分层数据。每个层次的数据由一个环或圆表示，最内圈为层次结构的顶部。一个没有任何分层数据的旭日图（一级类别）看起来类似于一个甜甜圈图表。然而，具有多个类别级别的旭日图表显示了外部环与内部环的关系。旭日图最有效地显示了一个环是如何被分解成其组成部分的，而另一种层次图表，树状图表，则适合用来比较相对大小。

Aspose.Cells支持旭日图。

#### **直方图图表**
直方图是显示频率数据的柱状图。

下面的雷达图在Aspose.Cells中受支持:

- Histogram chart
- Pareto chart

#### **箱式图**
箱式图显示数据分布到四分位数，突出均值和离群值。箱子可能有垂直延伸的线，称为``天顶”。这些线表示超出上下四分位数的变化，超出这些线或天顶的任何点都被认为是离群值。

箱式图在Aspose.Cells中受支持。

#### **瀑布图**
瀑布图显示随着值的增加或减少而形成的累积总数。它有助于了解一个初始值（例如，净收入）如何受一系列正负值的影响。

瀑布图在Aspose.Cells中受支持。

### **自定义图表类型**
自定义图表允许您创建具有自定义格式的图表，这些格式也可应用于其他图表。在这里，我们只讨论了标准图表。如果您想了解更多关于自定义图表的详细信息，请阅读【创建自定义图表】(/cells/zh/java/creating-and-customizing-charts/#creatingandcustomizingcharts-usingchartingobjects) 文章，该文章描述了如何创建自定义图表。
