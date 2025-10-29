---
title: 使用C++导出带有viewBox属性的SVG图表
linktitle: 导出带有viewBox属性的SVG图表
type: docs
weight: 280
url: /zh/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: 使用 Golang 通过 C++ 将图表导出为带有 viewBox 属性的 SVG 格式。
---

{{% alert color="primary" %}}

默认情况下，将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells提供了[**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/)属性，将其设置为**true**时会导出具有viewBox属性的SVG图表。

{{% /alert %}}

## 导出带有viewBox属性的SVG图表

以下示例代码将图表导出为带有viewBox属性的SVG格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
