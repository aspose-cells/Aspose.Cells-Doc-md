---
title: 通过Node.js和C++将图表转换成本地化图片
description: 学习如何使用Aspose.Cells for Node.js via C++设置图表的全球化配置。我们的指南演示如何配置图表以支持多语言和区域格式，以正确显示不同语言的文本、日期和数字。
keywords: Aspose.Cells for Node.js via C++，图表，全球化设置，多语言，区域格式，显示，文本，日期，数字。
linktitle: 设置本地化地区
type: docs
weight: 50
url: /zh/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何将图表转换为本地化图像，您将了解如何为图表设置本地化地区。

{{% /alert %}}

## **场景**

我们在什么情况下需要为图表设置本地化区域？ 

 当你用Excel打开带有图表的xlsx文件时，例如用Excel的西班牙区域设置打开，你可以看到图表区域的元素，比如图表标题、图例，它们已被翻译成西班牙语。但当你使用Aspose.Cells将此图表保存为图片时，可能会遇到以下问题： 

**![全局问题](GlobalIssue.png)**

在这种情况下，输出图片中的图表图例与Excel中的不同，默认仍显示为英文。现在您可以通过设置图表的本地化区域来解决此问题。设置正确后，以下元素将根据您的本地化设置进行渲染。

## **支持的元素**

图表中的以下元素可以根据您的本地化设置进行渲染。

|**支持的元素**|**在英文环境中的默认值**|
| :- | :- |
|坐标轴标题名称|坐标轴标题|
|坐标单位名称|百、千...|
|图表标题名称|图表标题|
|图例增加名称|增加|
|图例减少名称|减少|
|图例总计名称|总计|
|其他名称|其他|
|系列名称|系列|

## **操作步骤**

以下示例将详细展示如何设置本地化区域以实现您想要的效果。

- [如何为图表设置中文区域](/cells/zh/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [如何为图表设置日文区域](/cells/zh/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


