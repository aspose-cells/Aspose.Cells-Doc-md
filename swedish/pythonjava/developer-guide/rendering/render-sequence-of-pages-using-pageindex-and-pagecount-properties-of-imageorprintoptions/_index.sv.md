---
title: Rendera sekvens av sidor med hjälp av PageIndex och PageCount Properties för ImageOrPrintOptions
type: docs
weight: 10
url: /sv/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---
## **Rendera sekvens av sidor med hjälp av PageIndex och PageCount Properties för ImageOrPrintOptions**
Du kan rendera en sekvens av sidor i din Excel-fil till bilder med Aspose.Cells med[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) och[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) egenskaper. Dessa egenskaper är användbara när det finns så många t.ex. tusentals sidor i ditt kalkylblad men du bara vill rendera några av dem. Detta kommer inte bara att spara bearbetningstiden utan kommer också att spara minnesförbrukningen för renderingsprocessen.

Följande exempelkod laddar exemplet i Excel-filen och återger endast sidorna 4, 5, 6 och 7 med[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex)och[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) egenskaper. Följande är bilderna av de renderade sidorna som genereras av exempelkoden.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
|:- |:- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
