---
title: Uppdatera en slicer
linktitle: Uppdatera en slicer
type: docs
weight: 60
url: /sv/python-java/updating-slicer/
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med hjälp av Aspose.Cells for Python via Java API.
keywords: Aspose.Cells for Python via Java Uppdatera slicer, Python Java uppdatera slicer, hur man filtrerar en pivottabell med slicer i Python, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Uppdatera en slicer**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. Aspose.Cells for Python via Java uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.selectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `True` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `False` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.unselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.clearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for Python via Java 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.selectItems`, `Slicer.unselectItems` och `Slicer.clearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
Följande kodfragment laddar [exempel-Excel-filen](106365050.xlsx) som innehåller en slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.selectItems(labels, False)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](106365051.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Avmarkera en del av de markerade objekten:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Ta bort filtret (markera alla objekt):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}