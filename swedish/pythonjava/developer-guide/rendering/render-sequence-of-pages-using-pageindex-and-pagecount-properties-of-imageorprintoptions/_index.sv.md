---
title: Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions
type: docs
weight: 10
url: /sv/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions**
Du kan rendera en sekvens av sidor av din Excel-fil till bilder med Aspose.Cells med [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) och [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) egenskaper. Dessa egenskaper är användbara när det finns så många t.ex. tusentals sidor i ditt arbetsblad men du vill rendera bara vissa av dem. Detta kommer inte bara att spara bearbetningstid utan även spara minnesförbrukningen av renderingsprocessen.

Följande exempelkod laddar den provisoriska Excel-filen och renderar endast sidorna 4, 5, 6 och 7 med hjälp av [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) och [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) egenskaper. Följande är bilderna på de renderade sidorna som genererats av exemplarkoden.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
