---
title: Render Unicode Supplementary characters in output PDF by Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Learn how to render Unicode Supplementary characters while converting Excel to PDF with Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Normal Unicode characters are 2‑byte long while Unicode Supplementary characters are 4‑byte long. Aspose.Cells for Python via .NET now supports rendering of these 4‑byte Unicode characters.

In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.

- In UTF-8 these characters are each 4 bytes long.  
- In UTF-16 these characters require 2 surrogates (16‑bit units).

{{% /alert %}}

## Render Unicode Supplementary characters in output PDF by Aspose.Cells for Python via .NET

The following screenshot shows how Aspose.Cells for Python via .NET rendered the [source Excel file](5115563.xlsx) into the [output PDF](5115564.pdf). As you can see, all three Unicode Supplementary characters have been rendered exactly the same as those rendered by Microsoft Excel.

![todo:image_alt_text](output.png)

## Sample Code

You can use this sample code to convert the [source Excel file](5115563.xlsx) into the [output PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
