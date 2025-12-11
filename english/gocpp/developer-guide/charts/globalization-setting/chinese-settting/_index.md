---
title: Convert Chart to Image for Chinese Region with Golang via C++
linktitle: Set Chinese Region
description: Learn how to use Aspose.Cells for C++ to set Chinese configuration for charts. Our guide will demonstrate how to configure charts to support Chinese characters and formats, including fonts, sizes, text directions, and more.
keywords: Aspose.Cells for C++, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
type: docs
weight: 9
url: /go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In this topic, we will show you how to set the Chinese region for a chart.

{{% /alert %}}

## **Define a derived class**

The first step is to define a class **ChartChineseSettings** that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/).  
Then, by overriding the related functions, you can set the text of the chart elements in your own language.

Code example:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}

You can see the effect in the output image: the elements in the chart will be rendered according to your settings.

## **Conclusion**

In this example, if you do not set the Chinese region for a chart, the following chart elements may be rendered in the default language, such as English.  
After the above operation, we can obtain an output chart image with the Chinese region.

| **Supported elements** | **Value in this example** | **Default value in the English environment** |
| :- | :- | :- |
| Axis Title Name | 坐标轴标题 | Axis Title |
| Axis Unit Name | 百,千... | Hundreds, Thousands... |
| Chart Title Name | 图表标题 | Chart Title |
| Legend Increase Name | 增加 | Increase |
| Legend Decrease Name | 减少 | Decrease |
| Legend Total Name | 汇总 | Total |
| Other Name | 其他 | Other |
| Series Name | 系列 | Series |