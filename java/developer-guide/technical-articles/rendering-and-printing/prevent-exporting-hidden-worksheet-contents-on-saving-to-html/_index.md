---
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML
type: docs
weight: 90
url: /java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}} 

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (_files) directory which contains files such as worksheets, images, tabstrip.htm, stylesheet.css, etc. Sometimes, exporting the content of the hidden worksheets this way isn't appropriate. For example, if the hidden worksheet contains images that should not be exported to the _files directory.

{{% /alert %}} 

Aspose.Cells provides the [HtmlSaveOptions.ExportHiddenWorksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) property. By default, the [ExportHiddenWorksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) method is set to **true**. If you set it to **false**, then Aspose.Cells will not export hidden worksheet contents.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}
