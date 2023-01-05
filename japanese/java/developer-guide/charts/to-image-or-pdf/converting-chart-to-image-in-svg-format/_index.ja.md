---
title: チャートを SVG 形式の画像に変換する
type: docs
weight: 140
url: /ja/java/converting-chart-to-image-in-svg-format/
---
{{% alert color="primary" %}} 

Scalable Vector Graphics (SVG) は、対話機能とアニメーションもサポートする 2 次元グラフィックス用の XML ベースのベクター画像形式です。 SVG 仕様は、1999 年に World Wide Web Consortium (W3C) によって開発されたオープン スタンダードです。

SVG 画像とその動作は XML テキスト ファイルで定義されます。これは、それらを検索、索引付け、スクリプト化、および圧縮できることを意味します。 XML ファイルとして、SVG 画像は任意のテキスト エディターで作成および編集できますが、描画ソフトウェアで作成されることが多いです。

Aspose.Cells は、チャートを BMP、JPEG、PNG、GIF、SVG などのさまざまな形式の画像として保存できます。この記事では、チャートを SVG 画像として保存する方法について説明します。

{{% /alert %}} 

次のサンプル コードは、Aspose.Cells を使用してグラフを SVG 形式の画像に変換する方法を説明しています。このコードはソース Excel ファイルを読み込み、最初のワークシートで見つかった最初のグラフを SVG に保存します。

次のスクリーンショットは、サンプル コードで作成された SVG 形式の変換されたグラフ イメージを示しています。

**出力画像** 

![todo:画像_代替_文章](converting-chart-to-image-in-svg-format_1.png)

SVG は XML ベースの形式であるため、このスクリーンショットに示すように、メモ帳などのテキスト エディターで出力グラフ イメージを開くこともできます。

**テキストエディタでSCGを出力する** 

![todo:画像_代替_文章](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
