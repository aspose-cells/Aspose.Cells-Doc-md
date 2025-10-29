---
title: 使用C++通过Golang更改刻度标签方向
linktitle: 更改刻度标签方向
description: 了解如何在Aspose.Cells for C++中更改刻度标签的方向。我们的指南将帮助您理解如何调整轴上的刻度标签的方向，包括水平、垂直和倾斜方向。
keywords: Aspose.Cells for C++，刻度标签，方向，方向性，轴，水平，垂直，倾斜。
type: docs
weight: 170
url: /zh/go-cpp/change-tick-label-direction/
---

## **更改刻度标签方向**

Aspose.Cells 通过使用 [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/) 属性提供更改图表刻度标签方向的能力。 [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/) 属性接受 [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) 枚举值。 [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) 枚举包含以下成员：

- 水平
- 垂直
- 旋转90度
- 旋转270度
- 堆叠

以下图片对比了源文件和输出文件：

### **源文件图像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **输出文件图像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

以下代码片段将刻度标签方向从Rotate90更改为水平方向

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTickLabelDirection.go" >}}
可以从以下链接下载源文件和输出文件。

[源文件](105480221.xlsx)

[输出文件](105480223.xlsx)
