---
title: Konvertera Smart Art till gruppform
type: docs
weight: 80
url: /sv/java/convert-the-smart-art-to-group-shape/
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art Shape till gruppform med hjälp av [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--)-metoden. Det gör att du kan hantera Smart Art Shape som en gruppform. Som följd kommer du att ha tillgång till de enskilda delarna eller formarna i gruppformen.

## **Konvertera SmartArt till gruppform**

Följande exempelkod laddar in den [exempelfilen Excel](55541806.xlsx) som innehåller en Smart Art Shape som visas i denna skärmbild. Sedan konverterar den Smart Art Shape till gruppform och skriver ut egenskapen [Shape.IsGroup](https://reference.aspose.com/cells/java/com.aspose.cells/shape#IsGroup). Se utförseln till konsolen i den nedan givna exemplet.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-ConvertSmartArtToGroupShape.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: true

Is Group Shape: false

Is Group Shape: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
