---
title: Autopassa rader för rendering
type: docs
weight: 130
url: /sv/java/autofit-rows-for-rendering/
---
I allmänhet, när du vill visa all text i en cell, kan du automatiskt anpassa rad i normalvy med 100 % zoom i Microsoft Excel. Detta gör att texten är helt synlig i normalvy, och även när du skriver ut eller sparar filen som en PDF kommer texten att visas korrekt.

 Men i vissa fall fungerar autoanpassning av rad bra i normalvy, men när du byter till utskriftsvy eller sparar filen som en PDF, klipps texten. Kontrollera källfilen[Bok1.xlsx](Book1.xlsx) och skärmdumpar.

![texten klipps i utskriftsvy](text_clipped_in_printview.png)

Om du vill förhindra att text klipps i den sparade PDF-filen kan du autopassa raden med[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) alternativ.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Nu är texten inte klippt i utdatafilen PDF.

![texten är inte klippt i sparad pdf](text_not_clipped_in_saved_pdf.png)