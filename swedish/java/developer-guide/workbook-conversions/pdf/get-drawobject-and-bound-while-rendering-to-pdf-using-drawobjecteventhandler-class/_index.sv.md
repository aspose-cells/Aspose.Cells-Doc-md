---
title: Hämta DrawObject and Bound medan du renderar till PDF med DrawObjectEventHandler-klassen
type: docs
weight: 60
url: /sv/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Möjliga användningsscenarier**

Aspose.Cells tillhandahåller en abstrakt klass[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) som har en[**dra()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metod. Användaren kan implementera[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)och utnyttja[**dra()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metod för att få[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)och**Bunden**medan du renderar Excel till PDF eller Image. Här är en kort beskrivning av parametrarna för[**dra()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metod.

-  drawObject:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)kommer att initieras och returneras vid rendering

- x: Till vänster om[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Toppen av[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- bredd: Bredd av[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- höjd: Höjd på[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Om du renderar Excel-fil till PDF, kan du använda[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)klass med[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). På samma sätt, om du renderar Excel-fil till bild, kan du använda[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)klass med[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Hämta DrawObject and Bound medan du renderar till PDF med DrawObjectEventHandler-klassen**

Se följande exempelkod. Den laddar[exempel på Excel-fil](64716843.xlsx)och sparar den som[utgång PDF](64716842.pdf). Vid rendering till PDF använder den[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)egendom och fångar[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) och**Bunden**av befintliga celler och objekt, t.ex. bilder etc. Om drawObject-typen är Cell, skrivs dess Bound och StringValue ut. Och om drawObject-typen är Image, skrivs dess Bound and Shape Name ut. Se konsolutgången för exempelkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
