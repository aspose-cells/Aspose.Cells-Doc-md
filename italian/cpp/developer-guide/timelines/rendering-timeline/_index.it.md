---
title: Rendering della timeline con C++
type: docs
weight: 40
url: /it/cpp/rendering-timeline/
description: Gestisci le timeline dei file Excel con Aspose.Cells con C++.
keywords: Rappresentazione della timeline senza office 2013, office 2016, office 2019 e office 365
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells supporta la rappresentazione della forma della timeline senza utilizzare office 2013, office 2016, office 2019 e office 365. Se converti il tuo foglio di lavoro in un'immagine o salvi il tuo workbook in formati PDF o HTML, vedrai che le timeline vengono rappresentate correttamente.

## **Rappresentazione della Timeline**
Il seguente codice di esempio carica il [file di Excel di esempio](input.xlsx) che contiene una timeline esistente. Ottieni l'oggetto forma in base al nome della timeline, e poi rendilo in un'immagine attraverso il metodo Shape.ToImage(). L'immagine seguente è l'[immagine di output](out.png) che mostra la timeline resa. Come puoi vedere, la timeline è stata rappresentata correttamente e sembra la stessa del file di Excel di esempio.

![todo:image_alt_text](out.png)
### **Codice di Esempio**
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
{{< app/cells/assistant language="cpp" >}}
