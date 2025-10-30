---
title: Hur man använder bildmarkörer i Smart Markers
type: docs
weight: 30
url: /sv/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Möjliga användningsscenario**
Bildmarkörer är specialiserade platshållare i mallningssystem (som FoxPro, Handlebars eller moderna UI-ramverk) som dynamiskt infogar bilder eller visuella tillgångar i mallar. Ibland behöver du infoga bilder med hjälp av smarta markörer. Aspose.Cells gör det möjligt att lägga till bilder i smarta markörer.

## **Bildparametrar i Smart Markers**
Smarta markörsparametrar för hantering av bilder.

- **Bild:FitToCell** - Justera automatiskt bilden till cellens radhöjd och kolumnbredd.
- **Bild:SkalaN** - Skala höjd och bredd till N procent.
- **Picture:Width:Nin&Height:Nin** - Rendera bilden N tum hög och N tum bred. Du kan också specificera vänster och övre positioner (i punkter).

## **Hur man använder bildmarkörer i Smart Markers**
Vänligen se följande exempel som visar hur man infogar bilder med hjälp av smarta markörer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Hur man använder bildmarkörer vid gruppering av data i Smart Markers**
Följande exempel skapar en arbetsbok och lägger sedan till följande smarta markör-taggar i cellerna D2, E2 och F2 respektive.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Sedan fylls datakällan med data och [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)-metoden anropas för att bearbeta smarta markör-taggar. Koden använder dessa bilder dvs [moon.png](5115492.png) och [moon2.png](5115491.png) men du kan använda vilken bild som helst.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
