---
title: 将图表转换为本地化图像
description: 学习如何使用Aspose.Cells for .NET为图表设置全球化配置。我们的指南演示了如何配置图表以支持多种语言和区域格式，以正确显示不同语言中的文本，日期和数字。
keywords: Aspose.Cells for .NET，图表，全球化设置，多种语言，区域格式，显示，文本，日期，数字。
linktitle: 设置本地化区域
type: docs
weight: 50
url: /zh/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何将图表转换为本地化图像，您将了解如何为图表设置本地化区域。

{{% /alert %}}

## **场景**

何种情况下我们需要为图表设置本地化区域？ 

当您在Excel中使用西班牙地区设置打开带有图表的xlsx文件时，在这种情况下，假设您在Excel中使用西班牙区域设置打开它，您可以看到图表区域中的元素，例如图表标题、图例，它们已经被翻译成西班牙语。但是，当您使用Aspose.Cells将此图表保存为图片时，您可能会遇到以下问题： 

**![全局问题](GlobalIssue.png)**

在这种情况下，输出图片中的图例与Excel中的内容不同，它们仍然以默认的英文显示。现在，您可以通过为图表设置本地化区域来解决此问题。通过正确的设置，以下元素将根据您的本地化设置进行渲染。

## **支持的元素**

图表中的以下元素可以根据您的本地化设置进行渲染。

|**支持的元素**|**英文环境中的默认值**|
| :- | :- |
|轴标题名称|轴标题|
|轴单位名称|百，千...|
|图表标题名称|图表标题|
|图例增加名称|增加|
|图例减少名称|减少|
|图例总和名称|总和|
|其他名称|其他|
|系列名称|系列|

## **操作步骤**

下面的示例将详细展示如何设置本地化区域以实现您想要的效果。

- [如何为图表设置中文区域](/cells/zh/net/convert-chart-to-image-for-chinese-region/)
- [如何为图表设置日语区域](/cells/zh/net/convert-chart-to-image-for-japanese-region/)

