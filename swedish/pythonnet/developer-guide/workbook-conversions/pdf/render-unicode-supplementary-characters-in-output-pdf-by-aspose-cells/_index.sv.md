---
title: Återge Unicode-tilläggstecken i utdata PDF med Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /sv/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lär dig hur du renderar Unicode-tilläggstecken samtidigt som du konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Normala Unicode-tecken är 2-byte långa medan Unicode-tilläggstecken är 4-byte långa. Aspose.Cells for Python via .NET stöder nu rendering av dessa 4-byte Unicode-tecken.

I Unicode Character Standard är tilläggstecken de tecken som tilldelas kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

##  Återge Unicode-tilläggstecken i utdata PDF med Aspose.Cells for Python via .NET

 Följande skärmdump visar hur Aspose.Cells for Python via .NET återgav[source excel-fil](5115563.xlsx) in i[utgång PDF](5115564.pdf). Som du kan se har alla tre tilläggstecken i Unicode renderats på exakt samma sätt som Microsoft Excel.

![todo:image_alt_text](output.png)

##  Exempelkod

Du kan använda den här exempelkoden för att konvertera[source excel-fil](5115563.xlsx) in i[utgång PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
