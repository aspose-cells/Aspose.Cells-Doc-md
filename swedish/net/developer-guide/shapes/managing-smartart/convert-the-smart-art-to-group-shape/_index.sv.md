---
title: Konvertera Smart Art till gruppform
type: docs
weight: 200
url: /sv/net/convert-the-smart-art-to-group-shape/
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art Shape till gruppform med hjälp av [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart)-metoden. Det gör att du kan hantera Smart Art Shape som en gruppform. Som följd kommer du att ha tillgång till de enskilda delarna eller formarna i gruppformen.

## **Konvertera SmartArt till gruppform**

Följande kodexempel laddar [exempel Excel-filen](55541793.xlsx) som innehåller en smart konstform som visas på den här bilden. Den konverterar sedan den smarta konstformen till gruppkonstform och skriver ut Shape.IsGroup-egenskapen. Se konsoloutputen från det angivna kodexemplet nedan.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-ConvertSmartArtToGroupShape.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
