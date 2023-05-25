---
title: Få pappersbredd och höjd på sidinställningar för arbetsblad
type: docs
weight: 50
url: /sv/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Du kommer att upptäcka i den här artikeln hur du får Excel-arbetsbladet Sidinställning Pappersbredd och pappershöjd med C#-koden programmatiskt med .NET API eller bibliotek.
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **Möjliga användningsscenarier**

Ibland behöver du veta bredden och höjden på pappersstorleken som den har ställts in i sidinställningarna i kalkylbladet. Vänligen använd[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)och[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)fastigheter för detta ändamål.

##  **Få pappersbredd och höjd på sidinställningar för arbetsblad**

 Följande exempelkod förklarar användningen av[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) och[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) egenskaper. Den ändrar först pappersstorleken till*A2*och sedan hittar papprets bredd och höjd, sedan ändras det till*A3*, *A4*, *Brev*och hittar bredd respektive höjd på papper.

###  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
