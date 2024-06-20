---
title: Autoanpassa rader för rendering
type: docs
weight: 130
url: /sv/java/autofit-rows-for-rendering/
---

I allmänhet, när du vill visa all text i en cell kan du använda autofit för rad i Normalt läge med 100% zoom i Microsoft Excel. Detta gör att texten blir helt synlig i Normalt läge, och även när du skriver ut eller sparar filen som en PDF kommer texten att visas korrekt.

I vissa fall fungerar dock autofit-raden bra i Normalt läge, men när du växlar till utskriftsvy eller sparar filen som en PDF klipps texten. Var god kontrollera källfilen [Book1.xlsx](Book1.xlsx) och skärmklippen.

![text klipps i utskriftsvyn](text_klipps_i_utskriftsvyn.png)

Om du vill förhindra att texten klipps i den sparade PDF-filen kan du autofits rad med hjälp av alternativet [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) .

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Nu är texten inte klippt i den här PDF-filen.

![text klipps inte i sparad pdf](text_klipps_inte_i_sparad_pdf.png)
