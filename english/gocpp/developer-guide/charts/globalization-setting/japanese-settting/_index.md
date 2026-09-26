---
title: Convert Chart to Image for Japanese Region with Golang via C++
linktitle: Set Japanese Region
type: docs
weight: 10
url: /go-cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Learn how to use Aspose.Cells for Go via C++ to set the Japanese configuration for the chart. Our guide will demonstrate how to configure charts to support Japanese characters and formatting, including fonts, size, text direction, and more.
keywords: Aspose.Cells for Go, Charts, Japanese configuration, font, font size, text direction, support.
---

{{% alert color="primary" %}}

In this topic, we will show you how to set the Japanese region for a chart.

{{% /alert %}}

## **Define a Derived Class**

First, you need to define a class `ChartJapaneseSettings` that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/).  
Then, by overriding the related functions, you can set the text of the chart elements in your own language.  

Code example:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-JapaneseSettting.go" >}}

## **Configure Japanese Settings for Chart**

In this step, you will use the class `ChartJapaneseSettings` you defined in the previous step.  

Code example:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-JapaneseSettting-1.go" >}}

Then you can see the effect in the output image; the elements in the chart will be rendered according to your settings.

## **Conclusion**

In this example, if you do not set the Japanese region for a chart, the following chart elements may be rendered in the default language, such as English.  
After the above operation, you can obtain an output chart image with the Japanese region.

| **Supported Elements** | **Value in This Example** | **Default Value in the English Environment** |
| :- | :- | :- |
| Axis Title Name | 軸タイトル | Axis Title |
| Axis Unit Name | 百,千... | Hundreds, Thousands... |
| Chart Title Name | グラフ タイトル | Chart Title |
| Legend Increase Name | ぞうか | Increase |
| Legend Decrease Name | 削減 | Decrease |
| Legend Total Name | すべての | Total |
| Other Name | その他 | Other |
| Series Name | シリーズ | Series |
{{< app/cells/assistant language="go" >}}
