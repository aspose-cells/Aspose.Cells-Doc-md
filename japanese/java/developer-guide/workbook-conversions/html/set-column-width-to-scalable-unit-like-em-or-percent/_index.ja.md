---
title: 列幅を em やパーセントなどのスケーラブルな単位に設定する
type: docs
weight: 130
url: /ja/java/set-column-width-to-scalable-unit-like-em-or-percent/
---
スプレッドシートから HTML ファイルを生成することは非常に一般的です。列のサイズは、多くの場合に機能する「pt」で定義されます。ただし、この固定サイズが必要ない場合もあります。たとえば、この HTML ページが表示されているコンテナー パネルの幅が 600px の場合。この場合、生成されたテーブル幅が大きいと、水平スクロールバーが表示されることがあります。この固定サイズは、表示を改善するために em やパーセントなどのスケーラブルな単位に変更する必要がありました。次のサンプル コードは、次の場所で使用できます。[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable)に設定されています**真実**スケーラブルな幅を作成するため。

サンプル ソース ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
