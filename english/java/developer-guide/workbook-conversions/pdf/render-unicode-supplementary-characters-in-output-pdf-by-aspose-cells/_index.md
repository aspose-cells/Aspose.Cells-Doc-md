---
title: Render Unicode Supplementary characters in output PDF by Aspose.Cells
type: docs
weight: 690
url: /java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Normal Unicode characters are 2-bytes long while Unicode Supplementary characters are 4-bytes long. Aspose.Cells now supports rendering of these 4-bytes Unicode characters.

In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.

- In UTF-8 these characters are each 4 bytes long.
- In UTF-16 these characters require 2 surrogates (16-bit units).

{{% /alert %}} 
## **Render Unicode Supplementary characters in output PDF by Aspose.Cells**
The following screenshot shows how Aspose.Cells rendered the [source excel file](5473390.xlsx) into the [output PDF](5473391.pdf). As you can see all three Unicode Supplementary characters have been rendered exactly the same as done by Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

You can use this sample code to convert the [source excel file](5473390.xlsx) into [output PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
