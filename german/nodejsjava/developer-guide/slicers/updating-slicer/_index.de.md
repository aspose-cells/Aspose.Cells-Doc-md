---
title: Slicer mit Node.js via Java aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/nodejs-java/updating-slicer/
description: Dieser Artikel zeigt, wie Sie einen Slicer aktualisieren, um die Daten der verknüpften Pivot-Tabelle oder Tabelle mit Aspose.Cells for Node.js via Java zu filtern.
keywords: Aspose.Cells Node.js via Java, Slicer in Node.js aktualisieren, wie man den Slicer in Node.js ändert, wie man eine Pivot-Tabelle über einen Slicer in Node.js filtert, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Verwendungsszenarien**
Das Aktualisieren eines Slicers bedeutet, die Daten der Pivot-Tabelle oder Tabelle zu filtern, mit der der Slicer verbunden ist. Wenn Sie Slicer-Elemente in Microsoft Excel auswählen oder abwählen, wird die verknüpfte Pivot-Tabelle oder Tabelle entsprechend neu berechnet. Mit Aspose.Cells for Node.js via Java müssen Sie die Slicer-Cache-Elemente nicht durchlaufen und den Slicer nicht manuell aktualisieren — die Methode [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs/slicer/) aktualisiert den Slicer und berechnet die verknüpfte Pivot-Tabelle oder Tabelle direkt anhand der Filterelemente neu:
- `Slicer.selectItems(labels, append)` — wählt die angegebenen Bezeichnungen aus und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu. Wenn `append` `true` ist, werden die ursprünglich ausgewählten Bezeichnungen beibehalten und die angegebenen Bezeichnungen zur Auswahl hinzugefügt; wenn `append` `false` ist, werden alle ursprünglichen Auswahlen gelöscht und nur die angegebenen Bezeichnungen bleiben ausgewählt.
- `Slicer.unselectItems(labels)` — wählt einen Teil der aktuell ausgewählten Elemente ab.
- `Slicer.clearFilter()` — entfernt den Filter und wählt alle Elemente aus.

{{% alert color="primary" %}}
Ab Aspose.Cells for Node.js via Java 26.10 wird die Eigenschaft `SlicerCacheItem.Selected` schreibgeschützt, und ihr Setter wird nicht mehr unterstützt. Verwenden Sie die Methoden `Slicer.selectItems`, `Slicer.unselectItems` und `Slicer.clearFilter` anstelle des elementweisen Setzens von `SlicerCacheItem.Selected`.
{{% /alert %}}

## **Wie man den Slicer aktualisiert**
Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen, mit einer Pivot-Tabelle verbundenen Slicer enthält. Er wählt mit `Slicer.selectItems(labels, false)` nur die Elemente „Blue“ und „Pink“ des Slicers aus — die Pivot-Tabelle wird direkt anhand der Filterelemente neu berechnet, ohne einen manuellen `Slicer.refresh()`-Aufruf. Anschließend speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, zeigt die Pivot-Tabelle nur die gefilterten Elemente.
![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**
Ersetzt die aktuelle Auswahl (nur die angegebenen Bezeichnungen bleiben ausgewählt) und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Behält die aktuell ausgewählten Bezeichnungen bei und wählt zusätzlich weitere Elemente aus:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Wählt einen Teil der ausgewählten Elemente ab:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Entfernt den Filter (wählt alle Elemente aus):

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-java" >}}