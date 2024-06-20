---
title: グラフィックコンテキストにワークシートをレンダリングする
type: docs
weight: 300
url: /ja/net/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシートをグラフィックコンテキストにレンダリングすることができます。グラフィックコンテキストは、画像ファイル、スクリーン、プリンターなど、何でも指定できます。ワークシートをグラフィックコンテキストにレンダリングするには、以下の2つのメソッドのいずれかを使用してください。

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

以下のコードは、Aspose.Cells を使用してワークシートをグラフィックコンテキストにレンダリングする方法を示しています。コードを実行すると、グラフィックコンテキストにワークシート全体が印刷され、残りの空きスペースが青色で塗りつぶされ、**OutputImage_out_.png** ファイルとして画像が保存されます。このコードを試すためには、任意の元の Excel ファイルを使用できます。理解を深めるためにコード内のコメントもお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
