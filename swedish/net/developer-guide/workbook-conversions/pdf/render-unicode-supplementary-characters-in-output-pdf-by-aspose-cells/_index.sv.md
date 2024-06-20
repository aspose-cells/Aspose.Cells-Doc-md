---
title: Rendera Unicode Supplementary tecken i utmatning PDF med Aspose.Cells
type: docs
weight: 350
url: /sv/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

Normala Unicode-tecken är 2 byte långa medan Unicode Supplementary-tecken är 4 byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I den Unicode-tekniska standarden är Supplementary-tecken de tecken som tilldelats kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

## Rendera Unicode Supplementära tecken i utdata-PDF med Aspose.Cells

Följande skärmbild visar hur Aspose.Cells renderade [käll-Excel-filen](5115563.xlsx) till [utdata-PDF](5115564.pdf). Som du kan se har alla tre Unicode Supplementära-tecken renderats exakt som gjorts av Microsoft Excel.

![todo:image_alt_text](output.png)

## Exempelkod

Du kan använda följande exempelkod för att konvertera [källa excel-filen](5115563.xlsx) till [utdata PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
