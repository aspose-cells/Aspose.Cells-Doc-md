---
title: Uppdatera en slicer med C++
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/cpp/updating-slicer/
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med hjälp av Aspose.Cells for C++ API.
keywords: Aspose.Cells C++ Uppdatera slicer, C++ hur man ändrar slicern, hur man filtrerar en pivottabell med slicer i C++, C++ Slicer SelectItems, C++ Slicer ClearFilter, C++ Slicer UnselectItems.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for C++ behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.SelectItems(Vector&lt;U16String&gt;, bool)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/selectitems/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.SelectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.UnselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.ClearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for C++ 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.SelectItems`, `Slicer.UnselectItems` och `Slicer.ClearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.SelectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.Refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

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
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    Vector<U16String> labels{ u"Blue", u"Pink" };
    slicer.SelectItems(labels, false);
    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);
    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```cpp
// Keep the current selection and add "Red" to it.
Vector<U16String> moreLabels{ u"Red" };
slicer.SelectItems(moreLabels, true);
```

Avmarkera en del av de markerade objekten:

```cpp
// Remove "Pink" from the current selection.
Vector<U16String> toRemove{ u"Pink" };
slicer.UnselectItems(toRemove);
```

Ta bort filtret (markera alla objekt):

```cpp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="cpp" >}}