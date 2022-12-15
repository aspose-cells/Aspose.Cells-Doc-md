---
title: Återge Unicode-tilläggstecken i utdata-PDF med Aspose.Cells
type: docs
weight: 350
url: /sv/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}}

Normala Unicode-tecken är 2-byte långa medan Unicode-tilläggstecken är 4-byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I Unicode Character Standard är tilläggstecken de tecken som tilldelas kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}}

## Återge Unicode-tilläggstecken i utdata-PDF med Aspose.Cells

 Följande skärmdump visar hur Aspose.Cells renderade[källkod excel-fil](5115563.xlsx) in i[mata ut PDF](5115564.pdf). Som du kan se har alla tre tilläggstecken i Unicode renderats på exakt samma sätt som Microsoft Excel.

![todo:image_alt_text](output.png)

## Exempelkod

 Du kan använda den här exempelkoden för att konvertera[källkod excel-fil](5115563.xlsx) in i[mata ut PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
