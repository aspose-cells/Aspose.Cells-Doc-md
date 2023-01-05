---
title: viewBox属性を使用してグラフをSVGにエクスポートします
type: docs
weight: 280
url: /ja/net/export-chart-to-svg-with-viewbox-attribute/
---
{{% alert color="primary" %}}

デフォルトでは、グラフが SVG 形式でエクスポートされると、**ビューボックス**属性はその XML に含まれていません。ただし、Aspose.Cells は提供します[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport)に設定されたときのプロパティ**真実**viewBox 属性を使用してチャートを SVG にエクスポートします。

{{% /alert %}}

## viewBox属性を使用してグラフをSVGにエクスポートします

次のサンプル コードは、viewBox 属性を使用してグラフを SVG 形式にエクスポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

チャートの SVG をメモ帳で開くと、**ビューボックス**これに似た属性。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
