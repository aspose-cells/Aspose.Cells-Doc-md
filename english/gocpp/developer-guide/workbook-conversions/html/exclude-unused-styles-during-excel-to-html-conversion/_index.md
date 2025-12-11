---
title: Exclude Unused Styles during Excel to HTML conversion with Golang via C++
linktitle: Exclude Unused Styles
type: docs
weight: 30
url: /go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Learn how to exclude unused styles during Excel to HTML conversion using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Microsoft Excel files may contain many unused styles. When you export the Excel file to HTML format, these unused styles are also exported, which can increase the size of the HTML. You can exclude the unused styles during the conversion of an Excel file to HTML using the [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) property. When you set it to **true**, all unused styles are excluded from the output HTML. The following screenshot displays a sample unused style inside the output HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclude Unused Styles during Excel to HTML conversion**

The following sample code creates a workbook and also creates an unused named style. Since the [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) is set to **true**, this unused named style will not be exported to the [output HTML](61767778.zip). However, if you set it to **false**, this unused style will be present inside the output HTML, which you can then see in the HTML markup as shown in the above screenshot.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}