---
title: Rendering av tidslinje med C++
type: docs
weight: 40
url: /sv/cpp/rendering-timeline/
description: Hantera tidslinjer för Excel filer med Aspose.Cells och C++.
keywords: Rendering tidslinje utan office 2013, office 2016, office 2019 och office 365
---

## **Möjliga användningsscenario**
Aspose.Cells stöder rendering av tidslinjeform utan att använda office 2013, office 2016, office 2019 och office 365. Om du konverterar ditt kalkylblad till en bild eller sparar din arbetsbok i PDF- eller HTML-format kommer du att se att tidslinjer renderas korrekt.

## **Rendering Tidslinje**
Följande exempelkod laddar [in den exempel-Excel-filen](input.xlsx) som innehåller en befintlig tidslinje. Få formobjekt enligt tidslinjens namn, och rendera sedan det till en bild med hjälp av Shape.ToImage() metoden. Den resulterande bilden är [utmatningsbilden](out.png) som visar den renderade tidslinjen. Som du kan se har tidslinjen renderats korrekt och ser ut precis som i exempel-Excel-filen.

![todo:image_alt_text](out.png)
### **Exempelkod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
