---
title: Rendering tidslinje
type: docs
weight: 40
url: /sv/python-net/rendering-timeline/
description: Hantera tidslinjer för Excel filer med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Python Rendering tidslinje utan Excel, Rendera tidslinjen till bild med hjälp av Aspose.Cells för Python bibliotek.
---

## **Möjliga användningsscenario**
Aspose.Cells för Python via .NET stödjer renderingen av tidslinjeformen utan att använda Office 2013, Office 2016, Office 2019 och Office 365. Om du konverterar ditt kalkylblad till en bild eller sparar arbetsboken till PDF- eller HTML-format, kommer du att se att tidslinjerna renderas korrekt.

## **Hur man renderar tidslinje med Aspose.Cells för Python Excel-bibliotek**
Följande exempelkod laddar den [exempelfil för Excel](input.xlsx) som innehåller en befintlig tidslinje. Hämta formobjektet enligt namnet på tidslinjen och rendera det sedan i en bild genom metoden Shape.to_image(). Det resulterande bild är [utdata-bilden](out.png) som visar den renderade tidslinjen. Som du kan se har tidslinjen renderats korrekt och ser ut på samma sätt som i exemplet Excel-filen.

![todo:image_alt_text](out.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

