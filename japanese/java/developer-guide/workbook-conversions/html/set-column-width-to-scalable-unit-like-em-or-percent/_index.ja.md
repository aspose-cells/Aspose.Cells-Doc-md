---
title: emやパーセントなどのスケーラブルユニットに列の幅を設定する
type: docs
weight: 130
url: /ja/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

スプレッドシートからHTMLファイルを生成するのは一般的です。列のサイズは多くの場合"pt"で定義されていますが、固定サイズが必要ではない場合があります。例えば、HTMLページが表示されるコンテナパネルの幅が600pxである場合。この場合、生成されたテーブルの幅が大きいと水平スクロールバーが表示される可能性があります。より良い表現を得るためには、この固定サイズをemやパーセントなどのスケーラブルユニットに変更する必要があります。次のサンプルコードでは、**true**に設定された[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable)が使用されます。

サンプルのソースファイルと出力ファイルは以下のリンクからダウンロードできます：

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
