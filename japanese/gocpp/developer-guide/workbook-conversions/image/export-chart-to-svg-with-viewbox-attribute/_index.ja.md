---
title: viewBox属性を持つSVGへのエクスポートチャート（C++使用）
linktitle: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cellsを使用して、viewBox属性付きのSVG形式でチャートをエクスポートします。
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートするとき、そのXMLには**viewBox**属性が含まれません。しかし、Aspose.Cellsは、**true**に設定された場合に**viewBox**属性でチャートをSVG形式でエクスポートする[**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/)プロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
