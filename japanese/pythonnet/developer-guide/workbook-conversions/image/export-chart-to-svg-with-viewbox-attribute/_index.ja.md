---
title: viewBox 属性を使用してチャートを SVG にエクスポート
type: docs
weight: 280
url: /ja/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells for Python via .NET API を使用して、viewBox 属性を持つチャートを SVG にエクスポートします。
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

デフォルトでは、グラフが SVG 形式にエクスポートされると、**ビューボックス**属性は XML に含まれていません。ただし、Aspose.Cells for Python via .NET は、[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/)に設定するとプロパティ**真実**viewBox 属性を使用してグラフを SVG にエクスポートします。

{{% /alert %}}

##  viewBox 属性を使用してチャートを SVG にエクスポート

次のサンプル コードでは、viewBox 属性を使用してグラフを SVG 形式にエクスポートします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

メモ帳でチャートの SVG を開くと、**ビューボックス**これに似た属性。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
