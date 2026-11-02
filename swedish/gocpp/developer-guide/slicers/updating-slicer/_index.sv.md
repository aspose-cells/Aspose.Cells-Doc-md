---
title: Uppdatera en slicer med Golang via C++
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med hjälp av Aspose.Cells for Go via C++ API.
keywords: Aspose.Cells Go via C++ Uppdatera slicer, Go hur man ändrar slicern, hur man filtrerar en pivottabell med slicer i Go, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for Go via C++ behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.SelectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.UnselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.ClearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for Go via C++ 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.SelectItems`, `Slicer.UnselectItems` och `Slicer.ClearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.SelectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.Refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Avmarkera en del av de markerade objekten:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Ta bort filtret (markera alla objekt):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}