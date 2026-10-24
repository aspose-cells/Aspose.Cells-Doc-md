---
title: Slicer aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/net/updating-slicer/
description: Dieser Artikel zeigt, wie Sie einen Slicer aktualisieren, um die Daten der verknüpften Pivot-Tabelle oder Tabelle mit der Aspose.Cells for .NET API zu filtern.
keywords: Aspose.Cells C# Slicer aktualisieren, C# wie man den Slicer ändert, wie man eine Pivot-Tabelle über einen Slicer in C# filtert, C# Slicer SelectItems, C# Slicer ClearFilter, C# Slicer UnselectItems.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
Das Aktualisieren eines Slicers bedeutet, die Daten der Pivot-Tabelle oder Tabelle zu filtern, mit der der Slicer verbunden ist. Wenn Sie Slicer-Elemente in Microsoft Excel auswählen oder abwählen, wird die verknüpfte Pivot-Tabelle oder Tabelle entsprechend neu berechnet. Mit Aspose.Cells for .NET müssen Sie die Slicer-Cache-Elemente nicht durchlaufen und den Slicer nicht manuell aktualisieren — die Methode [**Slicer.SelectItems(string[], bool)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/selectitems/) aktualisiert den Slicer und berechnet die verknüpfte Pivot-Tabelle oder Tabelle direkt anhand der Filterelemente neu:
- `Slicer.SelectItems(labels, append)` — wählt die angegebenen Bezeichnungen aus und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu. Wenn `append` `true` ist, werden die ursprünglich ausgewählten Bezeichnungen beibehalten und die angegebenen Bezeichnungen zur Auswahl hinzugefügt; wenn `append` `false` ist, werden alle ursprünglichen Auswahlen gelöscht und nur die angegebenen Bezeichnungen bleiben ausgewählt.
- `Slicer.UnselectItems(labels)` — wählt einen Teil der aktuell ausgewählten Elemente ab.
- `Slicer.ClearFilter()` — entfernt den Filter und wählt alle Elemente aus.

{{% alert color="primary" %}}
Ab Aspose.Cells for .NET 26.10 wird die Eigenschaft `SlicerCacheItem.Selected` schreibgeschützt, und ihr Setter wird nicht mehr unterstützt. Verwenden Sie die Methoden `Slicer.SelectItems`, `Slicer.UnselectItems` und `Slicer.ClearFilter` anstelle des elementweisen Setzens von `SlicerCacheItem.Selected`.
{{% /alert %}}

## **Wie man den Slicer aktualisiert**
Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen, mit einer Pivot-Tabelle verbundenen Slicer enthält. Er wählt mit `Slicer.SelectItems(labels, false)` nur die Elemente „Blue“ und „Pink“ des Slicers aus — die Pivot-Tabelle wird direkt anhand der Filterelemente neu berechnet, ohne einen manuellen `Slicer.Refresh()`-Aufruf. Anschließend speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, zeigt die Pivot-Tabelle nur die gefilterten Elemente.
![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**
Ersetzt die aktuelle Auswahl (nur die angegebenen Bezeichnungen bleiben ausgewählt) und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu:

```csharp
using Aspose.Cells;
using Aspose.Cells.Slicers;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.Worksheets[0];
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.Slicers[0];
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.SelectItems(new string[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.Save("out.xlsx");
```

Behält die aktuell ausgewählten Bezeichnungen bei und wählt zusätzlich weitere Elemente aus:

```csharp
// Keep the current selection and add "Red" to it.
slicer.SelectItems(new string[] { "Red" }, true);
```

Wählt einen Teil der ausgewählten Elemente ab:

```csharp
// Remove "Pink" from the current selection.
slicer.UnselectItems(new string[] { "Pink" });
```

Entfernt den Filter (wählt alle Elemente aus):

```csharp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="csharp" >}}