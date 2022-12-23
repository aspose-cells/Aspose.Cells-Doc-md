---
title: Återge Unicode-tilläggstecken i utdata PDF av Aspose.Cells
type: docs
weight: 690
url: /sv/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

Normala Unicode-tecken är 2-byte långa medan Unicode-tilläggstecken är 4-byte långa. Aspose.Cells stöder nu rendering av dessa 4-byte Unicode-tecken.

I Unicode Character Standard är tilläggstecken de tecken som tilldelas kodpunkter från U+10000 till U+10FFFF. Med andra ord är dessa Unicode-tecken större än U+FFFF.

- I UTF-8 är dessa tecken var och en 4 byte långa.
- I UTF-16 kräver dessa tecken 2 surrogat (16-bitars enheter).

{{% /alert %}} 
## **Återge Unicode-tilläggstecken i utdata PDF av Aspose.Cells**
 Följande skärmdump visar hur Aspose.Cells renderade[source excel-fil](5473390.xlsx) in i[utgång PDF](5473391.pdf). Som du kan se har alla tre tilläggstecken i Unicode renderats på exakt samma sätt som Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Du kan använda den här exempelkoden för att konvertera[source excel-fil](5473390.xlsx) in i[utgång PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
