---
title: 如何创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/net/how-to-create-gantt-chart/
description: 如何在Aspose.Cells中创建甘特图
keywords: 创建/插入Aspose中的甘特图Excel
---
## 什么是甘特图

甘特图可帮助您安排项目任务，然后帮助您跟踪进度。

## 在Excel中添加甘特图

需要为简单项目进度表显示状态的甘特图？尽管Excel没有预定义的甘特图类型，但您可以通过自定义堆积条形图来模拟一个，以显示任务的开始和完成日期，就像这样：

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## 如何创建

- 选择要绘制图表的数据。在我们的示例中，是B1:B7，然后插入**堆积柱形**图。

![todo:image_alt_text](1.png)

- 选择图表，**选择数据**-> **添加**，将**系列名称**和**系列值**设置如下

![todo:image_alt_text](2.png)

- 选择图表，编辑**水平（类别）轴标签**

![todo:image_alt_text](3.png)

- **格式化轴** Y 轴，选择**逆序排列的类别**
- 选择**蓝色系列**，设置**填充->无填充**
- **格式化轴** X 轴，设置**最小和最大值** （1/5/2019: 43470, 1/30/2019: 43494）

![todo:image_alt_text](4.png)

- 为图表**添加数据标签**
现在您已经有了一个甘特图。

## 在Aspose.Cells中添加甘特图

以下示例代码通过打开 [示例文件](sample.xlsx)创建甘特图

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

您将得到一个类似于[result file](result.xlsx)的文件。在文件中，您将看到以下内容：

![todo:image_alt_text](5.png)

