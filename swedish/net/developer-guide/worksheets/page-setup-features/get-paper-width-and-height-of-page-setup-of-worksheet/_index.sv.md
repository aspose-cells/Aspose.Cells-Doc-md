---
title: Hämta papperets bredd och höjd för sidbildningsinställningen för arket
type: docs
weight: 50
url: /sv/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Du kommer att upptäcka i den här artikeln hur man får Excel arket Sidlayout Pappersbredd och Papperens höjd med C# kod programmatiskt med .NET API eller Bibliotek.
keywords: excel sidlayout pappersbredd c#, excel sidlayout papperens höjd c#
---

## **Möjliga användningsscenario**

Ibland behöver du veta bredd och höjd för pappersstorleken som har ställts in i sidlayouten för arket. Använd [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) och [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)-egenskaperna för detta ändamål.

## **Hämta pappersbredd och höjd i sidinställningen för kalkylblad**

Följande exempelkod förklarar användningen av [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) och [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)-egenskaperna. Det ändrar först pappersstorleken till *A2* och sedan hittar bredden och höjden för pappret, ändrar det sedan till *A3*, *A4*, *Brev* och hittar bredden och höjden för papperet respektive.

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Konsoloutput**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
