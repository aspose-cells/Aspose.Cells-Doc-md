---
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML with Golang via C++
linktitle: Prevent Exporting Hidden Worksheet Contents
type: docs
weight: 210
url: /go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Learn how to prevent exporting hidden worksheet contents when saving Excel workbooks to HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (_files) directory which contains files such as worksheets, images, tabstrip.htm, stylesheet.css, etc. Sometimes, exporting the content of the hidden worksheets this way isn't appropriate. For example, if the hidden worksheet contains images that should not be exported to the _files directory.

{{% /alert %}}

Aspose.Cells provides the [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/) property. By default, it is set to **true** and hidden worksheets are exported to HTML. If you set it **false**, Aspose.Cells will not export hidden worksheet contents.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}