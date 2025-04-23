---
title: グラフィックコンテキストにワークシートをレンダリングする
type: docs
weight: 300
url: /ja/java/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、ワークシートをグラフィックコンテキストにレンダリングできるようになりました。グラフィックコンテキストは画像ファイル、画面、プリンターなどのものであることができます。次のメソッドを使用してワークシートをグラフィックコンテキストにレンダリングします。

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

{{% /alert %}} 
## **ワークシートをグラフィックコンテキストにレンダリング**
以下のコードは、Aspose.Cellsを使用してワークシートをグラフィックコンテキストにレンダリングする方法を示しています。コードを実行すると、ワークシート全体がプリントされ、グラフィックコンテキストの残りの空きスペースを青色で塗りつぶして**test.png**ファイルとして画像を保存します。このコードを試すためには、任意のソースExcelファイルを使用できます。理解を深めるために、コード内のコメントも読んでください。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RenderWorksheetToGraphicContext-ReleaseUnmanagedResources.java" >}}






{{< app/cells/assistant language="java" >}}
