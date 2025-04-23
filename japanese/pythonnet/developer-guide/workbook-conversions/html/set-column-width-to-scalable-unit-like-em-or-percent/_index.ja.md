---
title: emやパーセントなどのスケーラブルユニットに列の幅を設定する
type: docs
weight: 130
url: /ja/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

スプレッドシートからHTMLファイルを生成することは非常に一般的です。列のサイズは多くの場合「pt」で定義されています。ただし、生成されたテーブルの幅が大きい場合、600pxのコンテナパネルの幅に適合させる必要がある場合があります。この場合、生成されたテーブルの幅が大きい場合に水平スクロールバーが表示される可能性があります。[**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable)を**true**に設定すると、この固定サイズをemやパーセントなどのスケーラブルな単位に変更して、より良い表示を行うことができます。

サンプルのソースファイルと出力ファイルは以下のリンクからダウンロードできます：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
