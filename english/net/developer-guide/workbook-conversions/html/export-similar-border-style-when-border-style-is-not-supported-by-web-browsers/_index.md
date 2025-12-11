---
title: Export Similar Border Style When Border Style Is Not Supported by Web Browsers
type: docs
weight: 70
url: /net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel supports some types of dashed borders that are not supported by web browsers. When you convert such an Excel file into HTML using Aspose.Cells, those borders are removed. However, Aspose.Cells can also display such borders with the **[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)** property. Please set its value to **true**, and the previously unsupported borders will be exported to the HTML file.

## **Export Similar Border Style When Border Style Is Not Supported by Web Browsers**

The following sample code loads the **[sample Excel file](64716806.xlsx)** that contains some unsupported borders, as shown in the screenshot below. The screenshot further illustrates the effect of **[HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)** in the **[output HTML](64716804.zip)**.

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
