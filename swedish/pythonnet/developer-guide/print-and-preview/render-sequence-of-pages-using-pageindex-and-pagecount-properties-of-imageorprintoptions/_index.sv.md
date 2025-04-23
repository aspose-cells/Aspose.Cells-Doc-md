---
title: Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions
type: docs
weight: 110
url: /sv/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Möjliga användningsscenario**

Du kan rendera en sekvens av sidor i din Excel-fil till bilder med Aspose.Cells för Python via .NET med hjälp av [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) och [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count) egenskaperna. Dessa egenskaper är användbara när det finns så många sidor, t.ex. tusentals sidor i ditt arbetsblad, men du vill bara rendera ett urval. Detta sparar inte bara bearbetningstid utan också minnesförbrukningen vid rendering.

## **Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions**

Följande kodexempel laddar den [prov-Excel-filen](55541781.xlsx) och renderar endast sidorna 4, 5, 6 och 7 med hjälp av [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index)- och [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count)-egenskaperna. Här är de renderade sidorna som genererats av koden.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
