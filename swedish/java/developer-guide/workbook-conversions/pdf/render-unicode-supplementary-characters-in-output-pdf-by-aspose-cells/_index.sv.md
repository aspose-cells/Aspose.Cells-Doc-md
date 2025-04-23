---
title: Rendera Unicode Supplementary tecken i utmatning PDF med Aspose.Cells
type: docs
weight: 690
url: /sv/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

Normala Unicode-tecken är 2 byte långa medan Unicode Supplementary-tecken är 4 byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I den Unicode-tekniska standarden är Supplementary-tecken de tecken som tilldelats kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}} 
## **Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells**
Följande skärmbild visar hur Aspose.Cells renderade [käll-excel-filen](5473390.xlsx) till [utmatnings-PDF-filen](5473391.pdf). Som du kan se har alla tre Unicode Supplementary-tecken renderats exakt på samma sätt som av Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Du kan använda denna exempelkod för att konvertera [käll-excel-filen](5473390.xlsx) till [utmatnings-PDF-filen](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
