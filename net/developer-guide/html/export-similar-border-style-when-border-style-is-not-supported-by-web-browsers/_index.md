---
title: Export similar Border Style when Border Style is not supported by Web Browsers
type: docs
weight: 70
url: /net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Possible Usage Scenarios**

Microsoft Excel supports some type of dashed borders which are not supported by Web Browsers. When you convert such an Excel file into HTML using Aspose.Cells, such borders are removed. However, Aspose.Cells can also support to display such borders with [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) property. Please set its value as **true** and the unsupported borders will also be exported to HTML file.

## **Export similar Border Style when Border Style is not supported by Web Browsers**

The following sample code loads the [sample Excel file](64716806.xlsx) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) property inside the [output HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "HTML-ExportSimilarBorderStyle.cs" >}}
