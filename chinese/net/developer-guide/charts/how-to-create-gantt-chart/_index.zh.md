---
title: 如何创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/net/how-to-create-gantt-chart/
description: 如何在Aspose.Cells中创建甘特图
keywords: 在Aspose中创建/插入甘特图Excel
---
## 什么是甘特图

甘特图可帮助您安排项目任务，并跟踪您的进度。

## 在Excel中添加甘特图

需要在简单项目进度表中显示甘特图状态吗？虽然Excel没有预定义的甘特图类型，但您可以通过自定义堆叠条形图来模拟一个，以显示任务的开始和结束日期，就像这样：

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## 如何创建

- 选择要制作图表的数据。在我们的示例中，这是B1:B7，然后插入**堆叠条形**图。

![todo:image_alt_text](1.png)

- 选择图表，**选择数据**->**添加**，设置**系列名称**和**系列值**如下

![todo:image_alt_text](2.png)

- 选择图表，编辑**水平（类别）轴标签**

![todo:image_alt_text](3.png)

- 对Y轴**格式轴**，选择**反向类别**
- 选择**蓝色系列**并设置**填充->无填充**
- 对X轴**格式轴**，设置**最小和最大值**（2019/1/5:43470，2019/1/30:43494）

![todo:image_alt_text](4.png)

- 为图表**添加数据标签**
现在您拥有了甘特图。

## 在Aspose.Cells中添加甘特图

以下示例代码通过打开[示例文件](sample.xlsx)创建甘特图

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

您将获得一个类似于[result file](result.xlsx)的文件。在该文件中，您将看到以下内容：

![todo:image_alt_text](5.png)

