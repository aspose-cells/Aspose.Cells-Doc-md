---
title: 将图表转换为本地化图像，使用Python via .NET
linktitle: 设置本地化地区
type: docs
weight: 50
url: /zh/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: 学习如何使用Aspose.Cells for Python via .NET设置图表的全球化配置。配置图表以支持多种语言和区域格式，以正确显示文本、日期和数字。
keywords: Aspose.Cells for Python via .NET、图表、全球化设置、多语言、区域格式、显示、文本、日期、数字。
---

{{% alert color="primary" %}}

在本主题中，我们将向你展示如何将图表转化为本地化图像，以及如何为图表设置本地化区域。

{{% /alert %}}

## **场景**

何时需要为图表设置本地化区域？

如果你在Excel中以西班牙地区设置打开包含图表的XLSX文件，图表的元素如标题和图例会以西班牙语显示。但是，使用Aspose.Cells将此图表保存为图像时，这些元素可能会默认保持英文：

**![全局问题](GlobalIssue.png)**

这是因为输出图像中的图表图例与Excel的本地化不匹配。你可以通过配置图表的本地化区域设置来解决这个问题。

## **支持的元素**

以下图表元素将根据你的本地化设置显示：

| **支持的元素** | **默认值（英文）** |
|-----------------------------|-----------------------------------|
| 轴标题名称 | 轴标题 |
| 轴单位名称 | 百位、千位... |
| 图表标题名称 | 图表标题 |
| 图例增加名称 | 增加 |
| 图例减少名称 | 减少 |
| 图例总计名称 | 总计 |
| 其他名称 | 其他 |
| 系列名称 | 系列 |

