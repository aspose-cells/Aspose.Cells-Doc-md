---
title: Slicer aktualisieren
linktitle: Slicer aktualisieren
type: docs
weight: 60
url: /de/python-java/updating-slicer/
description: Dieser Artikel zeigt, wie Sie einen Slicer aktualisieren, um die Daten der verknüpften Pivot-Tabelle oder Tabelle mit der Aspose.Cells for Python via Java API zu filtern.
keywords: Aspose.Cells for Python via Java Slicer aktualisieren, Python Java Slicer aktualisieren, wie man eine Pivot-Tabelle über einen Slicer in Python filtert, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Slicer aktualisieren**
Das Aktualisieren eines Slicers bedeutet, die Daten der Pivot-Tabelle oder Tabelle zu filtern, mit der der Slicer verbunden ist. Aspose.Cells for Python via Java aktualisiert den Slicer und berechnet die verknüpfte Pivot-Tabelle oder Tabelle direkt anhand der Filterelemente neu:
- `Slicer.selectItems(labels, append)` — wählt die angegebenen Bezeichnungen aus und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu. Wenn `append` `True` ist, werden die ursprünglich ausgewählten Bezeichnungen beibehalten und die angegebenen Bezeichnungen zur Auswahl hinzugefügt; wenn `append` `False` ist, werden alle ursprünglichen Auswahlen gelöscht und nur die angegebenen Bezeichnungen bleiben ausgewählt.
- `Slicer.unselectItems(labels)` — wählt einen Teil der aktuell ausgewählten Elemente ab.
- `Slicer.clearFilter()` — entfernt den Filter und wählt alle Elemente aus.

{{% alert color="primary" %}}
Ab Aspose.Cells for Python via Java 26.10 wird die Eigenschaft `SlicerCacheItem.Selected` schreibgeschützt, und ihr Setter wird nicht mehr unterstützt. Verwenden Sie die Methoden `Slicer.selectItems`, `Slicer.unselectItems` und `Slicer.clearFilter` anstelle des elementweisen Setzens von `SlicerCacheItem.Selected`.
Der folgende Codeausschnitt lädt die [Beispiel-Excel-Datei](106365050.xlsx), die einen mit einer Pivot-Tabelle verbundenen Slicer enthält. Er wählt mit `Slicer.selectItems(labels, False)` nur die Elemente „Blue“ und „Pink“ des Slicers aus — die Pivot-Tabelle wird direkt anhand der Filterelemente neu berechnet, ohne einen manuellen `Slicer.refresh()`-Aufruf. Anschließend speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](106365051.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispiel-Excel-Datei. Wie Sie im Screenshot sehen können, zeigt die Pivot-Tabelle nur die gefilterten Elemente.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Beispielcode**
Ersetzt die aktuelle Auswahl (nur die angegebenen Bezeichnungen bleiben ausgewählt) und berechnet die verknüpfte Pivot-Tabelle oder Tabelle neu:

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

Behält die aktuell ausgewählten Bezeichnungen bei und wählt zusätzlich weitere Elemente aus:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Wählt einen Teil der ausgewählten Elemente ab:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Entfernt den Filter (wählt alle Elemente aus):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}