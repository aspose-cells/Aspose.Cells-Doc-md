---
title: ワークシートをグラフィック コンテキストにレンダリング
type: docs
weight: 300
url: /ja/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells はワークシートをグラフィック コンテキストにレンダリングできるようになりました。グラフィック コンテキストは、画像ファイル、画面、プリンターなどのようなものです。次の 2 つの方法のいずれかを使用して、ワークシートをグラフィック コンテキストにレンダリングしてください。

- [**SheetRender.ToImage(int pageIndex、Graphics g、float x、float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

次のコードは、Aspose.Cells を使用してワークシートをグラフィック コンテキストにレンダリングする方法を示しています。コードを実行すると、ワークシート全体が印刷され、残りの空きスペースがグラフィック コンテキストの青色で塗りつぶされ、画像が次のように保存されます。**OutputImage_out_.png**ファイル。任意のソース Excel ファイルを使用して、このコードを試すことができます。理解を深めるために、コード内のコメントもお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
