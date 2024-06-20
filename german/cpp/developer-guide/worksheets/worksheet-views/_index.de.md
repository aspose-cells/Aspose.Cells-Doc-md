---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/cpp/worksheet-views/
---

## **Seitenwechselvorschau**
Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenwechselvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenwechselvorschau zeigt an, welche Daten auf jeder Seite gedruckt werden, damit Sie den Druckbereich und Seitenumbrüche anpassen können. Mithilfe von Aspose.Cells können Entwickler die Normalansicht oder die Seitenwechselvorschau aktivieren.
### **Steuerung der Ansichtsmodi**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) -Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern. Um die Normalansicht oder die Seitenwechselvorschau zu aktivieren, verwenden Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -Klasse. [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) gibt einen boolschen Wert zurück, was bedeutet, dass es nur einen **true** oder **false** Wert speichern kann.
#### **Normale Ansicht aktivieren**
Setzen Sie ein Arbeitsblatt in die Normalansicht, indem Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -Klasse auf **false** setzen.
#### **Aktivieren der Seitenwechselvorschau**
Setzen Sie ein beliebiges Arbeitsblatt in die Seitenwechselvorschau, indem Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) -Klasse auf **true** setzen. Dadurch wird das Arbeitsblatt von der Normalansicht in die Seitenwechselvorschau umgeschaltet.

Ein vollständiges Beispiel finden Sie unten, das zeigt, wie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) verwendet wird, um für das erste Arbeitsblatt einer Excel-Datei den Modus Seitenwechselvorschau zu aktivieren.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Zoom-Faktor**
### **Verwendung von Microsoft Excel**
Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.
### **Aspose.Cells & Zoomfaktor**
Aspose.Cells ermöglicht Entwicklern außerdem die Einstellung des Arbeitsblatt-Zoomfaktors. Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) -Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) -Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse stellt eine breite Palette von Methoden zur Verwaltung von Arbeitsblättern bereit. Verwenden Sie zur Festlegung des Zoomfaktors eines Arbeitsblatts die [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) Methode der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der Zoomfaktor wird festgelegt, indem ein numerischer (ganzzahliger) Wert der [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) Methode zugewiesen wird.

Ein vollständiges Beispiel unten demonstriert, wie die [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) Methode verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts der Excel-Datei festzulegen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Fenster fixieren**
### **Verwendung von Microsoft Excel**
Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.
### **Aspose.Cells & Einfrieren von Fenstern**
Aspose.Cells ermöglicht es Entwicklern auch, beim Ausführen Arbeitsblättern Fixierungsfenster anzuwenden. Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse stellt eine breite Palette von Methoden zur Verwaltung von Arbeitsblättern bereit. Um Fixierungsfenster zu konfigurieren, rufen Sie die [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) Methode der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse auf. Die [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) Methode verwendet die folgenden Parameter:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

Ein vollständiges Beispiel unten zeigt, wie die [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) Methode verwendet wird, um Zeilen und Spalten (beginnend ab C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei die Zeilen und Spalten ab dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei einzufrieren.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Geteilte Fenster**
Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.
### **Anwenden und Entfernen von geteilten Fenstern**
#### **Teilen von Fenstern**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse stellt eine breite Palette von Methoden zur Verwaltung einer Excel-Datei bereit. Um Splitt-Ansichten zu implementieren, verwenden Sie die [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) Methode der [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Um die Splittfenster zu entfernen, verwenden Sie die [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Panes entfernen**
Entfernen Sie Splittfester mit der [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) Methode.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
