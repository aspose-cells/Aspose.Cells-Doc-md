---
title: Hämta papperets bredd och höjd för sidbildningsinställningen för arket
type: docs
weight: 50
url: /sv/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Du kommer att upptäcka i denna artikel hur man får Excel Arbetsblad Siduppställning Pappersbredd och Pappershöjd med Python kod programmatiskt med Aspose.Cells för Python via .NET API eller bibliotek.
keywords: Python Excel bibliotek, Python excels siduppställning pappersbredd, excels siduppställning pappershöjd i Python.
---

## **Möjliga användningsscenario**

Ibland behöver du veta bredd och höjd för pappersstorleken som har ställts in i sidlayouten för arket. Använd [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) och [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)-egenskaperna för detta ändamål.

## **Hämta pappersbredd och höjd i sidinställningen för kalkylblad**

Följande exempelkod förklarar användningen av [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) och [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) egenskaper. Den ändrar först pappersstorleken till *A2* och hittar sedan bredden och höjden på papperet, sedan ändrar den det till *A3*, *A4*, *Brev* och hittar bredden och höjden på papperet respektive.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Konsoloutput**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
