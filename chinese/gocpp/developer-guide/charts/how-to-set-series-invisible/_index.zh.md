---
title: 使用 Golang 通过 C++ 设置系列不可见
linktitle: 如何设置系列不可见
description: 在 Excel 图表中，可能需要将系列设置为不可见。本文介绍如何使用 Aspose.Cells 通过 C++ 与 Golang 实现。
keywords: Excel图表，系列，隐藏，已过滤。
type: docs
weight: 74
url: /zh/go-cpp/how-to-set-series-invisible/
---

## 如何在Excel图表中设置系列不可见

在Excel图表中，你可以右键点击图表，选择"选择数据"，在弹出窗口中，通过勾选或取消勾选系列来设置是否显示该系列。你可以下载下面的[示例文件](SeriesFiltered.xlsx)，在Excel中操作实现此功能。接下来，我们将告诉你如何使用Aspose.Cells库实现此功能。

![todo:image_alt_text](series-invisible.png)

## 如何使用Aspose.Cells设置系列不可见 

我们使用以下代码来将系列设置为不可见：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变成了隐藏。  
![todo:image_alt_text](output.png)
