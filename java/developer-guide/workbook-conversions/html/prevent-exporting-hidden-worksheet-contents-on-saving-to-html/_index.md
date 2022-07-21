---
title: Prevent Exporting Hidden Worksheet Contents on Saving to HTML
type: docs
weight: 90
url: /java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

You can save Excel workbooks to HTML. However, if the workbook contains hidden worksheets, Aspose.Cells by default exports the hidden worksheet contents to the HTML output (_files) directory which contains files such as worksheets, images, tabstrip.htm, stylesheet.css, etc. Sometimes, exporting the content of the hidden worksheets this way isn't appropriate. For example, if the hidden worksheet contains images that should not be exported to the _files directory.

{{% /alert %}}

Aspose.Cells provides the [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) property. By default, the [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) property is set to **true**. If you set it to **false**, then Aspose.Cells will not export hidden worksheet contents.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Other than controlling whether to export hidden worksheets or not, you may also configure additional settings for exporting workbook to HTML. The following articles demonstrate other features supported by Aspose.Cells for exporting workbooks to HTML.

- [Convert Excel to HTML with headings](/cells/java/convert-excel-to-html-with-headings/)
- [Exclude Unused Styles during Excel to HTML conversion](/cells/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Export Comments while Saving Excel file to HTML](/cells/java/export-comments-while-saving-excel-file-to-html/)
- [Hiding Overlaid Content with CrossHideRight while saving to HTML](/cells/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Export similar Border Style when Border Style is not supported by Web Browsers](/cells/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
