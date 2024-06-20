---
title: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 190
url: /ja/java/export-chart-to-svg-with-viewbox-attribute/
---

デフォルトでは、チャートをSVG形式でエクスポートするときには、そのXMLに**viewBox**属性は含まれません。しかし、Aspose.Cellsは[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort)プロパティを提供しており、それを**true**に設定すると、**viewBox**属性を含めたSVG形式でチャートをエクスポートできます。

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## コードスニペット

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## 関連記事

- [グラフのレンダリング](/cells/ja/java/chart-rendering/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
