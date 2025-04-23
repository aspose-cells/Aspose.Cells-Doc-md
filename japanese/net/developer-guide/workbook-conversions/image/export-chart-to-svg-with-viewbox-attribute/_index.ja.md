---
title: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/net/export-chart-to-svg-with-viewbox-attribute/
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートするとき、そのXMLには**viewBox**属性が含まれません。しかし、Aspose.Cellsは、**true**に設定された場合に**viewBox**属性でチャートをSVG形式でエクスポートする[**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport)プロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ExportChartToSvgWithViewBox-ExportChartToSvgWithViewBox.cs" >}}

{{% alert color="primary" %}}

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
