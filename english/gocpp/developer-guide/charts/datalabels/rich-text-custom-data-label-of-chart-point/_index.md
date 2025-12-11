---
title: Rich Text Custom Data Label of Chart Point with Golang via C++
description: Learn how to add rich text custom data labels to chart points in Aspose.Cells for C++. Our guide will show you how to format the labels with different fonts, colors, and alignment options to enhance the appearance and readability of your charts.
keywords: Aspose.Cells for C++, charting, rich text, custom data labels, fonts, colors, alignment, appearance, readability.
type: docs
weight: 10
url: /go-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

You can use Aspose.Cells to create a rich text custom data label for a chart point. Aspose.Cells provides the [DataLabels.Characters()](https://reference.aspose.com/cells/go-cpp/charttextframe/characters/) method to return the [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) object, which can be used to set the font properties of the text, such as its color, boldness, etc.

{{% /alert %}}

## Rich Text Custom Data Label of Chart Point

The following code accesses the first chart point of the first series, sets its text, and then sets the font of the first 10 characters by changing their color to red and making them bold.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichTextCustomDataLabelOfChartPoint.go" >}}