---
title: 如何设置系列不可见
description: 在Excel图表中，可能需要设置系列为隐藏状态。本文描述了如何使用Aspose.Cells实现。 
keywords: Excel图表，系列，隐藏，已过滤。
type: docs
weight: 74
url: /zh/net/how-to-set-series-invisible/
---

## 如何在Excel图表中设置系列不可见

在Excel图表中，您可以右键点击图表，选择“选择数据”，然后在弹出窗口中，通过勾选或取消勾选可以设置该系列是否可见。
你可以下载以下[示例文件](SeriesFiltered.xlsx)，并按照图中的操作在Excel中实现此功能。接下来，我们将告诉你如何使用Aspose.Cells库实现此功能。

![todo:image_alt_text](series-invisible.png)

## 如何使用Aspose.Cells设置系列不可见 

我们使用以下代码来将系列设置为不可见：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Set-series-invisible.cs" >}}

你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变成了隐藏。
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="csharp" >}}
