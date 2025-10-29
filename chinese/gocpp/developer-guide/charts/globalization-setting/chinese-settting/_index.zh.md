---
title: 使用C++通过Golang将图表转换为中国区域的图片
linktitle: 设置中国区域
description: 学习如何使用Aspose.Cells for C++设置支持中文字符和格式的图表。我们的指南将演示如何配置图表以支持中文字符，包括字体、大小、文本方向等。
keywords: Aspose.Cells for C++，图表，中文配置，字体，字体大小，文本方向，支持。
type: docs
weight: 9
url: /zh/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置中国区域。

{{% /alert %}}

## **定义继承类**

第一步，你需要定义一个继承自[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)的类"ChartChineseSetttings"。 
然后，通过重写相关函数，你可以用自己的语言设置图表元素的文本。

代码示例:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

## **结论**

在这个示例中，如果不为图表设置中国区域，则以下图表元素可能以默认语言（例如英语）渲染。
在上述操作之后，我们可以获得一个带有中国区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|轴标题名称|坐标轴标题|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题|图表标题|
|增加|增加|
|减少|减少|
|汇总|汇总|
|其他|其他|
|系列|系列|
