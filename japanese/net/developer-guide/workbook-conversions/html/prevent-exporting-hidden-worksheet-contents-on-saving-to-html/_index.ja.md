---
title: HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしないようにする
type: docs
weight: 210
url: /ja/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cellsはプロパティ[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet)を提供します。デフォルトでは、**true**に設定されており、非表示のワークシートがHTMLにエクスポートされます。**false**に設定すると、Aspose.Cellsは非表示のワークシート内容をエクスポートしません。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

