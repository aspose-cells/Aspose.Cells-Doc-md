---
title: GolangをC++経由でHTMLに保存する際に非表示のワークシートコンテンツをエクスポートしないようにする
linktitle: 非表示のワークシート内容をエクスポートしない
type: docs
weight: 210
url: /ja/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for C++を使用して、ExcelワークブックをHTMLに保存するときに非表示のシート内容のエクスポートを防ぐ方法を学びます。
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cellsはプロパティ[**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/)を提供します。デフォルトでは、**true**に設定されており、非表示のワークシートがHTMLにエクスポートされます。**false**に設定すると、Aspose.Cellsは非表示のワークシート内容をエクスポートしません。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
