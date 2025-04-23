---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/go-cpp/worksheet-views/
---

## **Seitenwechselvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenwechselvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenwechselvorschau zeigt an, welche Daten auf jeder Seite gedruckt werden, damit Sie den Druckbereich und Seitenumbrüche anpassen können. Mithilfe von Aspose.Cells können Entwickler die Normalansicht oder die Seitenwechselvorschau aktivieren.

### **Steuerung der Ansichtsmodi**

Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern. Um den normalen oder den Seitenumbruch-Vorschaumodus zu aktivieren, verwenden Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse. [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) gibt einen booleschen Wert zurück, was bedeutet, dass es nur **true** oder **false** speichern kann.

#### **Normale Ansicht aktivieren**

Setzen Sie ein Arbeitsblatt auf Normalansicht, indem Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse auf **false** setzen.

#### **Aktivieren der Seitenwechselvorschau**

Setzen Sie ein beliebiges Arbeitsblatt in den Seitenumbruch-Vorschaumodus, indem Sie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse auf **true** setzen. Dadurch wird das Arbeitsblatt vom Normalmodus in den Seitenumbruch-Vorschaumodus umgeschaltet.

Unten ist ein vollständiges Beispiel, das zeigt, wie die Methode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) verwendet wird, um den Seitenumbruch-Vorschaumodus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Zoom-Faktor**

### **Verwendung von Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht es auch, den Zoomfaktor von Arbeitsblättern festzulegen. Aspose.Cells bietet die Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei erlaubt.

Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Methode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse. Der Zoomfaktor wird gesetzt, indem ein numerischer (Ganzzahl-)Wert an die Methode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) übergeben wird.

Unten ist ein vollständiges Beispiel, das zeigt, wie die Methode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts in der Excel-Datei festzulegen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Fenster fixieren**

### **Verwendung von Microsoft Excel**

Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

### **Aspose.Cells & Einfrieren von Fenstern**

Aspose.Cells ermöglicht es Entwicklern auch, das Einfrieren von Fensterbereichen während der Laufzeit zu aktivieren. Aspose.Cells bietet die Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung von Arbeitsblättern. Um Freeze-Panes zu konfigurieren, rufen Sie die [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) Methode der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse auf. Die [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) Methode akzeptiert folgende Parameter:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

Ein vollständiges Beispiel zeigt, wie man die [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) Methode verwendet, um Zeilen und Spalten (beginnend bei C4, dargestellt durch die 4. Zeile und die 3. Spalte, wobei Zeilen und Spalten bei 0 beginnen) des ersten Arbeitsblatts der Excel-Datei einzufrieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Geteilte Fenster**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.

### **Anwenden und Entfernen von geteilten Fenstern**

#### **Teilen von Fenstern**

Aspose.Cells stellt die Klasse [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse bietet eine Vielzahl von Methoden zur Verwaltung einer Excel-Datei. Um Split-Ansichten umzusetzen, verwenden Sie die [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) Methode der [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse. Um die Split-Panes zu entfernen, verwenden Sie die [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Panes entfernen**

Schneiden Sie Split-Panes mit der [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/) Methode entfernt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
