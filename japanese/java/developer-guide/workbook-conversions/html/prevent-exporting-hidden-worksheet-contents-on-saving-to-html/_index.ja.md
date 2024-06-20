---
title: HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしないようにする
type: docs
weight: 90
url: /ja/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cellsは[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)プロパティを提供します。デフォルトでは、[**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet)プロパティが**true**に設定されています。**false**に設定すると、Aspose.Cellsは非表示のワークシートコンテンツをエクスポートしません。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

非表示のワークシートをエクスポートするかどうかを制御する以外にも、ワークブックをHTMLにエクスポートする際の追加設定を行うことができます。以下の記事では、Aspose.CellsがワークブックをHTMLにエクスポートする際にサポートされる他の機能を示しています。

- [見出しを使用したExcelからHTMLへの変換](/cells/ja/java/convert-excel-to-html-with-headings/)
- [ExcelからHTMLへの変換時に未使用のスタイルを除外](/cells/ja/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [ExcelファイルをHTMLに保存する際にコメントをエクスポート](/cells/ja/java/export-comments-while-saving-excel-file-to-html/)
- [HTMLに保存する際のボーダースタイルがWebブラウザでサポートされていない場合に似たボーダースタイルをエクスポートする](/cells/ja/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする](/cells/ja/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
