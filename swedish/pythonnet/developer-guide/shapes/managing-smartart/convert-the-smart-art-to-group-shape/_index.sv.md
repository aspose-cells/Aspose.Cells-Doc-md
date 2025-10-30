---
title: Konvertera Smart Art till gruppform
type: docs
weight: 200
url: /sv/python-net/convert-the-smart-art-to-group-shape/
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art Shape till gruppform med hjälp av [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art/#)-metoden. Det gör att du kan hantera Smart Art Shape som en gruppform. Som följd kommer du att ha tillgång till de enskilda delarna eller formarna i gruppformen.

## **Konvertera SmartArt till gruppform**

Följande kodexempel laddar [exempel Excel-filen](55541793.xlsx) som innehåller en smart konstform som visas på den här bilden. Den konverterar sedan den smarta konstformen till gruppkonstform och skriver ut Shape.IsGroup-egenskapen. Se konsoloutputen från det angivna kodexemplet nedan.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ConvertSmartArtToGroupShape.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
