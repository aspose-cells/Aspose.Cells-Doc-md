---
title: C++経由のGolangを使用して、スプレッドシートをHTMLにレンダリングするときにデフォルトフォントを設定します。
linktitle: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する
type: docs
weight: 370
url: /ja/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aspose.Cells for C++を使用して、HTMLにスプレッドシートをレンダリングする際のデフォルトフォント設定方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsでは、スプレッドシートをHTMLにレンダリングする際にデフォルトフォントを設定できます。これには [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) を使用してください。このプロパティは、スプレッドシート内のセルに無効または存在しないフォントがある場合に便利です。そのセルは [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) プロパティで指定されたフォントでレンダリングされます。

{{% /alert %}}

## スプレッドシートをHTMLにレンダリングする際のデフォルトフォントの設定

次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。

スクリーンショットは、[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) プロパティを介して異なるデフォルトフォント名を設定した効果を示しています。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

このコードは、異なる{0}を指定して生成された[出力HTMLファイルとCourier New](5115516)、[Arial](5115518)、[Times New Roman](5115517)を生成します。

## サンプルコード

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
