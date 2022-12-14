---
title: Hämta DrawObject and Bound medan du renderar till PDF med DrawObjectEventHandler-klassen
type: docs
weight: 70
url: /sv/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Möjliga användningsscenarier**

 Aspose.Cells tillhandahåller en abstrakt klass[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) som har en[**Dra()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)metod. Användaren kan implementera[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) och utnyttja[**Dra()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) metod för att få[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)och Bound samtidigt som Excel renderas till PDF eller bild. Här är en kort beskrivning av parametrarna för[**Dra()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)metod.

-  drawObject:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) kommer att initieras och returneras vid rendering

- x: Till vänster om[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Toppen av[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- bredd: Bredd av[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- höjd: Höjd på[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Om du renderar Excel-fil till PDF, kan du använda[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)klass med[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . På samma sätt, om du renderar Excel-fil till bild, kan du använda[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)klass med[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Hämta DrawObject and Bound medan du renderar till PDF med DrawObjectEventHandler-klassen**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](64716821.xlsx) och sparar den som[mata ut PDF](64716822.pdf). Vid rendering till PDF använder den[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)egendom och fångar[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) och Bound of existerande celler och objekt, t.ex. bilder etc. Om[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) typen är Cell, den skriver ut sitt Bound och StringValue. Och om[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)typen är Bild, den skriver ut dess bundna och formnamn. Se konsolutgången för exempelkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
