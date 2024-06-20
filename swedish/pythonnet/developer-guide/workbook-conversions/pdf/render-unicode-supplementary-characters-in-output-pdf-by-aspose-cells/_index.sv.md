---
title: Rendera Unicode Supplementary tecken i utdata PDF med Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /sv/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lär dig hur man Renderar Unicode Supplementary tecken när du konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Rendera Unicode Supplementary tecken när du sparar filen till PDF, Skriv ut Unicode Supplementary tecken när du sparar Excel till PDF med Python, Python Visa Unicode Supplementary tecken när du konverterar Excel till PDF, Utdata Unicode Supplementary tecken för excel till pdf
---

{{% alert color="primary" %}}

Normala Unicode-tecken är 2 byte långa medan Unicode Supplementary-tecken är 4 byte långa. Aspose.Cells for Python via .NET stöder nu rendering av dessa 4 byte Unicode-tecken.

I den Unicode-tekniska standarden är Supplementary-tecken de tecken som tilldelats kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

## Rendera Unicode Supplementary-tecken i utdata PDF med Aspose.Cells for Python via .NET

Följande skärmdump visar hur Aspose.Cells for Python via .NET renderade [källa excel-filen](5115563.xlsx) till [utdata PDF](5115564.pdf). Som du kan se har alla tre Unicode Supplementary-tecken renderats precis som gjort av Microsoft Excel.

![todo:image_alt_text](output.png)

## Exempelkod

Du kan använda följande exempelkod för att konvertera [källa excel-filen](5115563.xlsx) till [utdata PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
