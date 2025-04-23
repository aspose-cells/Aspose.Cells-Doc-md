---
title: 设置点为总数的方法。
description: 在某些Excel图表，例如瀑布图，可能需要将某个点设置为总计。本文介绍了如何使用Aspose.Cells实现。 
keywords: 水平瀑布图，点，设为总和。
type: docs
weight: 72
url: /zh/net/how-to-set-point-as-total/
---

## Excel图表中的"设为总和"是什么意思

在一些Excel图表中，例如瀑布图，某些点的数据是前面所有点的总和，你可能需要"设为总和"。我们会展示示例代码和说明。

## 瀑布图需要将点设为"总和" 

![todo:image_alt_text](set-as-total1.png)

此图显示了Excel中的瀑布图。我们可以看到有四个以"总和"开头的数据点，它们用于计算之前所有数据点的总和。
在此图中，设置并不完全正确，当我们选择"2024年总和"点时，可以看到Excel中"设为总和"选项没有被勾选。
下方附有需要修改的 [示例Excel文件](SampleSheet.xlsx)，我们将使用Aspose.Cells来正确设置它。

## 使用Aspose.Cells将点设为"总和" 

我们使用以下代码来正确设置文件：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Set-point-as-total.cs" >}}

你可以得到以下正确的[输出文件](output.xlsx)

如下图所示，四个"总和"数据点已正确设置，你可以看到与之前图表的区别。

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="csharp" >}}
