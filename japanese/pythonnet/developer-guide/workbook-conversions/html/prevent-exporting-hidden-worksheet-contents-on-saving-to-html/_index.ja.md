---
title: HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしないようにする
type: docs
weight: 210
url: /ja/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cellsはプロパティ[**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet)を提供します。デフォルトでは、**true**に設定されており、非表示のワークシートがHTMLにエクスポートされます。**false**に設定すると、Aspose.Cellsは非表示のワークシート内容をエクスポートしません。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

{{< app/cells/assistant language="python-net" >}}
