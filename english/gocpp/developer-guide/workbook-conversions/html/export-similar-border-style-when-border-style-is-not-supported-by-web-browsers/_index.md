---
title: Export similar Border Style when Border Style is not supported by Web Browsers with Golang via C++
linktitle: Export similar Border Style when Border Style is not supported by Web Browsers
type: docs
weight: 70
url: /go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Learn how to export similar border styles when unsupported by web browsers using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

Microsoft Excel supports some types of dashed borders, which are not supported by web browsers. When you convert such an Excel file into HTML using Aspose.Cells, those borders are removed. However, Aspose.Cells can also display such borders with the [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) property. Please set its value to **true**, and the unsupported borders will also be exported to the HTML file.

## **Export similar Border Style when Border Style is not supported by Web Browsers**

The following sample code loads the [sample Excel file](64716806.xlsx) that contains some unsupported borders, as shown in the following screenshot. The screenshot further illustrates the effect of the [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/) property inside the [output HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}