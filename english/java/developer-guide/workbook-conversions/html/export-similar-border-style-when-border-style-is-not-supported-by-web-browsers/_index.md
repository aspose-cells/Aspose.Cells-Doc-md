---
title: Export similar Border Style when Border Style is not supported by Web Browsers
type: docs
weight: 70
url: /java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel supports some type of dashed borders which are not supported by Web Browsers. When you convert such an Excel file into HTML using Aspose.Cells, such borders are removed. However, Aspose.Cells can also support to display similar borders with [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) property. Please set its value as **true** and the unsupported borders will also be exported to HTML file.

## **Export similar Border Style when Border Style is not supported by Web Browsers**

The following sample code loads the [sample Excel file](64716832.xlsx) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) property inside the [output HTML](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
{{< app/cells/assistant language="java" >}}
