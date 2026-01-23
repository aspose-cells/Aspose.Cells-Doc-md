---
title: How to Switch MHTML Tabs in IE
type: docs
weight: 70
url: /net/convert-excel-to-mhtml-with-ie-compatible/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

## **How to Switch MHTML Tabs in Internet Explorer**
When converting Excel files with multiple worksheets to MHTML, users may encounter issues when opening the generated .mhtml file in Internet Explorer, such as: Worksheet tabs are not switchable or only the first sheet is visible.
This article explains how to enable proper worksheet tab switching in Internet Explorer when exporting Excel files to MHTML. Please use [**HtmlSaveOptions.IsIECompatible**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/isiecompatible/)  property and set it to true while saving to MHTML.
This ensures the generated MHTML tabs work correctly in IE.
## **Sample Code**
This is the main code showing how to enable Internet Explorer–compatible MHTML output so that worksheet tab switching works correctly.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportToMHtmlWithIECompatible.cs" >}}
{{< app/cells/assistant language="csharp" >}}