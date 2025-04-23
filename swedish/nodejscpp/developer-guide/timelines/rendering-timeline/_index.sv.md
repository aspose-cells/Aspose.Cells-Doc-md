---
title: Rendering tidslinje
type: docs
weight: 40
url: /sv/nodejs-cpp/rendering-timeline/
description: Hantera tidslinjer för Excel filer med Aspose.Cells for Node.js via C++.
keywords: Rendering tidslinje utan office 2013, office 2016, office 2019 och office 365
---

## **Möjliga användningsscenario**
Aspose.Cells for Node.js via C++ stöder rendering av tidlinjens form utan att använda Office 2013, Office 2016, Office 2019 och Office 365. Om du konverterar ditt kalkylblad till en bild eller sparar arbetsboken i PDF- eller HTML-format, kommer du att se att tidslinjer renderas korrekt.

## **Rendering Tidslinje**
Följande exempelkod laddar [in den exempel-Excel-filen](input.xlsx) som innehåller en befintlig tidslinje. Få formobjekt enligt tidslinjens namn, och rendera sedan det till en bild med hjälp av Shape.ToImage() metoden. Den resulterande bilden är [utmatningsbilden](out.png) som visar den renderade tidslinjen. Som du kan se har tidslinjen renderats korrekt och ser ut precis som i exempel-Excel-filen.

![todo:image_alt_text](out.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
