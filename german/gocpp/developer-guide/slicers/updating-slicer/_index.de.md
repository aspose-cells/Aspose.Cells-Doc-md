---
title: Slicer mit Golang via C++ aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Dieser Artikel zeigt, wie Sie einen Slicer aktualisieren, um die Daten der verknüpften Pivot-Tabelle oder Tabelle mit der Aspose.Cells for Go via C++ API zu filtern.
keywords: Aspose.Cells Go via C++ Slicer aktualisieren, Go wie man den Slicer ändert, wie man eine Pivot-Tabelle über einen Slicer in Go filtert, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Mögliche Verwendungsszenarien**
Das Aktualisieren eines Slicers bedeutet, die Daten der Pivot-Tabelle oder Tabelle zu filtern, mit der der Slicer verbunden ist. Wenn Sie Slicer-Elemente in Microsoft Excel auswählen oder abwählen, wird die verknüpfte Pivot-Tabelle oder Tabelle entsprechend neu berechnet. Mit Aspose.Cells for Go via C++ müssen Sie die Slicer-Cache-Elemente nicht durchlaufen und den Slicer nicht manuell aktualisieren — die Methode [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) aktualisiert den Slicer und berechnet die verknüpfte Pivot-Tabelle oder Tabelle direkt anhand der Filterelemente neu:
- `Slicer.SelectItems(labels, append)` — wählt die angegebenen Bezeichnungen aus und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu. Wenn `append` `true` ist, werden die ursprünglich ausgewählten Bezeichnungen beibehalten und die angegebenen Bezeichnungen zur Auswahl hinzugefügt; wenn `append` `false` ist, werden alle ursprünglichen Auswahlen gelöscht und nur die angegebenen Bezeichnungen bleiben ausgewählt.
- `Slicer.UnselectItems(labels)` — wählt einen Teil der aktuell ausgewählten Elemente ab.
- `Slicer.ClearFilter()` — entfernt den Filter und wählt alle Elemente aus.

{{% alert color="primary" %}}
Ab Aspose.Cells for Go via C++ 26.10 wird die Eigenschaft `SlicerCacheItem.Selected` schreibgeschützt, und ihr Setter wird nicht mehr unterstützt. Verwenden Sie die Methoden `Slicer.SelectItems`, `Slicer.UnselectItems` und `Slicer.ClearFilter` anstelle des elementweisen Setzens von `SlicerCacheItem.Selected`.
{{% /alert %}}

## **Wie man den Slicer aktualisiert**
Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen, mit einer Pivot-Tabelle verbundenen Slicer enthält. Er wählt mit `Slicer.SelectItems(labels, false)` nur die Elemente „Blue“ und „Pink“ des Slicers aus — die Pivot-Tabelle wird direkt anhand der Filterelemente neu berechnet, ohne einen manuellen `Slicer.Refresh()`-Aufruf. Anschließend speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, zeigt die Pivot-Tabelle nur die gefilterten Elemente.
![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**
Ersetzt die aktuelle Auswahl (nur die angegebenen Bezeichnungen bleiben ausgewählt) und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu:

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

Behält die aktuell ausgewählten Bezeichnungen bei und wählt zusätzlich weitere Elemente aus:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Wählt einen Teil der ausgewählten Elemente ab:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Entfernt den Filter (wählt alle Elemente aus):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}