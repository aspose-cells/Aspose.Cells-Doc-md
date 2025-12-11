---
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML
type: docs
weight: 210
url: /net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (_files) directory, which contains files such as worksheets, images, tabstrip.htm, stylesheet.css, etc. Sometimes, exporting the content of the hidden worksheets this way isn't appropriate. For example, if the hidden worksheet contains images that should not be exported to the _files directory.

{{% /alert %}}

Aspose.Cells provides the [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) property. By default, it is set to **true**, and hidden worksheets are exported to HTML. If you set it to **false**, Aspose.Cells will not export hidden worksheet contents.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

{{< app/cells/assistant language="csharp" >}}
