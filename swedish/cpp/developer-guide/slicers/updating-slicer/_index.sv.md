---
title: Uppdatera slicer med C++
linktitle: Uppdatera slicer
type: docs
weight: 50
url: /sv/cpp/updating-slicer/
description: Den här artikeln visar hur man uppdaterar länkade pivottabeller genom att uppdatera slicer med API et Aspose.Cells for C++.
keywords: Aspose.Cells C++ Uppdatera slicer, C++ hur man ändrar slicer, hur man justerar slicer i C++, hur man väljer eller avmarkerar slicer objekt.
---

## **Möjliga användningsscenario**

Om du vill uppdatera en slicer i Microsoft Excel, välj eller avmarkera dess objekt, uppdateras slicer-tabellen eller pivottabellen därefter. Använd [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) för att välja eller avmarkera slicer objekt med Aspose.Cells och anropa sedan [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)-metoden för att uppdatera slicer tabellen eller pivottabellen.

## **Hur man uppdaterar snittet**

Följande exempelkod laddar [provmappen](67338475.xlsx) som innehåller en befintlig snitt. Den avmarkerar den 2:a och 3:e objekten i snittet och uppdaterar snittet sedan. Den sparar sedan arbetsboken som [utmatningsmapp](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på provmappen. Som du kan se på skärmbilden, har uppdateringen av snittet med markerade objekt också uppdaterat pivottabellen.

![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
