---
title: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する
type: docs
weight: 370
url: /ja/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、スプレッドシートをHTMLにレンダリングする際にデフォルトフォントを設定することができます。そのためには、[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)を使用してください。このプロパティは、スプレッドシート内に無効または存在しないフォントを持つセルがある場合に役立ちます。その場合、[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)プロパティで指定したフォントでセルがレンダリングされます。

{{% /alert %}}

## スプレッドシートをHTMLにレンダリングする際のデフォルトフォントの設定

次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。

次のスクリーンショットは、[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)　プロパティを使用して異なるデフォルトフォント名を設定した効果を示しています。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

このコードは、異なる{0}を指定して生成された[出力HTMLファイルとCourier New](5115516)、[Arial](5115518)、[Times New Roman](5115517)を生成します。

## サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
