---
title: viewBox属性を使用してグラフをSVGにエクスポートします
type: docs
weight: 190
url: /ja/java/export-chart-to-svg-with-viewbox-attribute/
---
デフォルトでは、グラフを SVG 形式でエクスポートすると、**ビューボックス**属性はその XML に含まれていません。ただし、Aspose.Cells は提供します[**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort)に設定されたときのプロパティ**真実**viewBox 属性を使用してチャートを SVG にエクスポートします。

チャートの SVG をメモ帳で開くと、**ビューボックス**これに似た属性。

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

## コードスニペット

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCharttoSVG-ExportCharttoSVG.java" >}}

## 関連記事

- [チャートのレンダリング](/cells/ja/java/chart-rendering/)
- [ワークシートまたはチャートを目的の幅と高さの画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
