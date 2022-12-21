---
title: HTML への保存時に非表示のワークシート コンテンツをエクスポートしないようにする
type: docs
weight: 90
url: /ja/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Excel ワークブックを HTML に保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、デフォルトで Aspose.Cells は非表示のワークシートの内容を HTML 出力 (_ files) ディレクトリには、ワークシート、画像、tabstrip.htm、stylesheet.css などのファイルが含まれています。非表示のワークシートの内容をこの方法でエクスポートすることが適切でない場合があります。たとえば、非表示のワークシートにエクスポートしてはならない画像が含まれている場合、_ファイル ディレクトリ。

{{% /alert %}}

Aspose.Cells は[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)財産。デフォルトでは、[**非表示ワークシートのエクスポート**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)プロパティはに設定されています**真実**.に設定すると**間違い**の場合、Aspose.Cells は非表示のワークシートの内容をエクスポートしません。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

非表示のワークシートをエクスポートするかどうかを制御する以外に、ワークブックを HTML にエクスポートするための追加設定を構成することもできます。次の記事では、ワークブックを HTML にエクスポートするために Aspose.Cells でサポートされているその他の機能について説明します。

- [Excel を見出し付きの HTML に変換する](/cells/ja/java/convert-excel-to-html-with-headings/)
- [Excel から HTML への変換中に未使用のスタイルを除外する](/cells/ja/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Excel ファイルを HTML に保存しながらコメントをエクスポートする](/cells/ja/java/export-comments-while-saving-excel-file-to-html/)
- [HTML への保存時に CrossHideRight でオーバーレイされたコンテンツを非表示にする](/cells/ja/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [ボーダー スタイルが Web ブラウザーでサポートされていない場合に、同様のボーダー スタイルをエクスポートする](/cells/ja/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
