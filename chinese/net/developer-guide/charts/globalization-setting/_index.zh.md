---
title: 将图表转换为本地化图像
linktitle: 设置本地化区域
type: docs
weight: 50
url: /zh/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---
{{% alert color="primary" %}}

在本主题中，我们将向您展示如何将图表转换为本地化图像，您将了解如何为图表设置本地化区域。

{{% /alert %}}

##  **设想**

在什么情况下我们需要为图表设置本地化区域？

当您在 Excel 中打开带有图表的 xlsx 文件时，在这种情况下，假设您在 Excel 中使用西班牙语区域设置打开它，您可以看到图表区域中的元素，例如图表标题、图例，它们被翻译成西班牙语。但是当你将这张图表保存为Aspose.Cells的图片时，你可能会遇到如下问题：

**![全球问题](GlobalIssue.png)**

在这种情况下，输出图片中的 Chart Lengend 与 Excel 中的不一样，它们默认以英文显示。现在您可以通过为图表设置本地化区域来解决这个问题。使用正确的设置，将根据您的本地化设置呈现以下元素。

##  **支持的元素**

图表中的以下元素可以根据您的本地化设置呈现。

|**支持的元素**|**英文环境默认值**|
| :- | :- |
|轴标题名称|轴标题|
|轴单位名称|数百，数千...|
|图表标题名称|图表标题|
|图例增加名称|增加|
|图例减少名称|减少|
|图例总名|全部的|
|其他名字|其他|
|系列名称|系列|

##  **操作步骤**

下面的示例将详细说明如何设置本地化区域以达到您想要的效果。

- [如何为图表设置中文区域](/cells/zh/net/convert-chart-to-image-for-chinese-region/)
- [如何为图表设置日语区域](/cells/zh/net/convert-chart-to-image-for-japanese-region/)

