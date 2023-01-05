---
title: 列幅を em やパーセントなどのスケーラブルな単位に設定する
type: docs
weight: 130
url: /ja/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
スプレッドシートから HTML ファイルを生成することは非常に一般的です。列のサイズは、多くの場合に機能する「pt」で定義されます。ただし、この固定サイズが必要ない場合もあります。たとえば、コンテナ パネルの幅が 600px で、この HTML ページが表示されているとします。この場合、生成されたテーブル幅が大きいと、水平スクロールバーが表示されることがあります。この固定サイズは、表示を改善するために em やパーセントなどのスケーラブルな単位に変更する必要がありました。次のサンプル コードは、次の場所で使用できます。[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable)に設定されています**真実**スケーラブルな幅を作成するため。

サンプル ソース ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
