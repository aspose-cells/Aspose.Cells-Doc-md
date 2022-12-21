---
title: スプレッドシートを HTML にレンダリングする際のデフォルト フォントの設定
type: docs
weight: 370
url: /ja/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、スプレッドシートを HTML にレンダリングする際にデフォルトのフォントを設定できます。をご利用ください[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)この目的のために。このプロパティは、無効なフォントまたは存在しないフォントを含むセルがスプレッドシートにある場合に役立ちます。次に、これらのセルは、で指定されたフォントでレンダリングされます[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)財産。

{{% /alert %}}

## スプレッドシートを HTML にレンダリングする際のデフォルト フォントの設定

次のサンプル コードでは、ワークブックを作成し、最初のワークシートのセル B4 にテキストを追加し、そのフォントを不明または存在しないフォントに設定します。次に、Courier New、Arial、Times New Roman などのさまざまな既定のフォント名を設定して、ワークブックを HTML で保存します。

スクリーンショットは、さまざまなデフォルトのフォント名を設定した効果を示しています[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)財産。

![todo:画像_代替_文章](set-default-font-while-rendering-spreadsheet-to-html_1.png)

コードは、[Courier New で HTML ファイルを出力する](5115516) 、[HTML を Arial で出力する](5115518)、 そしてその[Times New RomanでHTMLファイルを出力する](5115517).

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
