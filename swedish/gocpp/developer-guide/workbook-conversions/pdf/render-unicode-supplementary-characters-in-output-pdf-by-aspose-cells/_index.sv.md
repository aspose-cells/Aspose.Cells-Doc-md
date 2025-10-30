---
title: Rendera Unicode kompletterande tecken i utgångs PDF med Golang via C++ av Aspose.Cells
linktitle: Render Unicode tilläggstecken
type: docs
weight: 350
url: /sv/go-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Lär dig hur man renderar Unicode tilläggstecken i utdata PDF med Aspose.Cells for C++.
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderUnicodeSupplementaryCharactersInOutputPdfByAsposeCells.go" >}}
