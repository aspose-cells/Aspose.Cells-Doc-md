---
title: SVG形式でチャートを画像に変換
type: docs
weight: 140
url: /ja/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

スケーラブル・ベクター・グラフィックス（SVG）は、二次元グラフィックス用のXMLベースのベクター画像形式であり、対話性やアニメーションもサポートしています。SVG仕様は、1999年以来世界広範囲のウェブ consortium（W3C） によって開発されたオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これにより、検索、索引付け、スクリプト作成、圧縮が可能です。SVG画像はXMLファイルとして任意のテキストエディタで作成および編集できますが、一般的には図形作成ソフトウェアで作成されます。

Aspose.Cellsは、チャートをBMP、JPEG、PNG、GIF、SVGなどさまざまな形式の画像として保存できます。この記事では、チャートをSVG画像として保存する方法について説明します。

{{% /alert %}} 

次のサンプルコードは、Aspose.Cellsを使用してチャートをSVG形式の画像に変換する方法を説明しています。コードでは、ソースのExcelファイルをロードし、その後、最初のワークシートで見つかった最初のチャートをSVG形式で保存します。

次のスクリーンショットは、サンプルコードで作成されたSVG形式の変換されたチャート画像を示しています。

**出力画像** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

SVGはXMLベースの形式であるため、このスクリーンショットに示すように、出力チャート画像をNotepadなどのテキストエディタで開くこともできます。

**テキストエディタでSCGを出力** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
