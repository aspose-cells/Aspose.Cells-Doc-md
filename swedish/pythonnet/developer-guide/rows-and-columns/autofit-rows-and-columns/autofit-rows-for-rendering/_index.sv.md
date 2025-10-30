---
title: Autoanpassa rader för rendering
type: docs
weight: 130
url: /sv/python-net/autofit-rows-for-rendering/
description: Lär dig hur man Autofitar rader för rendering genom Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Autofitar rader för rendering, Python justera automatiskt radhöjden vid öppnande av excelfilen. 
---

I allmänhet, när du vill visa all text i en cell kan du använda autofit för rad i Normalt läge med 100% zoom i Microsoft Excel. Detta gör att texten blir helt synlig i Normalt läge, och även när du skriver ut eller sparar filen som en PDF kommer texten att visas korrekt.

I vissa fall fungerar dock autofit-raden bra i Normalt läge, men när du växlar till utskriftsvy eller sparar filen som en PDF klipps texten. Var god kontrollera källfilen [Book1.xlsx](Book1.xlsx) och skärmklippen.

![text klipps i utskriftsvyn](text_klipps_i_utskriftsvyn.png)

Om du vill förhindra att texten klipps i den sparade PDF-filen kan du autofita raden med alternativet [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Nu är texten inte klippt i den här PDF-filen.

![text klipps inte i sparad pdf](text_klipps_inte_i_sparad_pdf.png)
{{< app/cells/assistant language="python-net" >}}
