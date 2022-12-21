---
title: HTML への保存時に非表示のワークシート コンテンツをエクスポートしないようにする
type: docs
weight: 210
url: /ja/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Excel ワークブックを HTML に保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、デフォルトで Aspose.Cells は非表示のワークシートの内容を HTML 出力 (_ files) ディレクトリには、ワークシート、画像、tabstrip.htm、stylesheet.css などのファイルが含まれています。非表示のワークシートの内容をこの方法でエクスポートすることが適切でない場合があります。たとえば、非表示のワークシートにエクスポートしてはならない画像が含まれている場合、_ファイル ディレクトリ。

{{% /alert %}}

Aspose.Cells は[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet)財産。デフォルトでは、**真実**非表示のワークシートは HTML にエクスポートされます。設定すれば**間違い**、Aspose.Cells は、非表示のワークシートの内容をエクスポートしません。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

