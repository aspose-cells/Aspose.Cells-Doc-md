---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/cpp/worksheet-views/
---
##  **Seitenumbruchvorschau**
Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenumbruchvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt beim Drucken anzeigt. In der Seitenumbruchvorschau wird angezeigt, welche Daten auf jeder Seite angezeigt werden, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells können Entwickler den Normalansicht- oder Seitenumbruch-Vorschaumodus aktivieren.
###  **Ansichtsmodi steuern**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Die Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um den normalen oder Seitenumbruch-Vorschaumodus zu aktivieren, verwenden Sie die[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) gibt einen Bool-Wert zurück, was bedeutet, dass nur a gespeichert werden kann**WAHR** oder**FALSCH** Wert.
####  **Normalansicht aktivieren**
Stellen Sie ein Arbeitsblatt auf Normalansicht ein, indem Sie das festlegen[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse auf *false**.
####  **Aktivieren der Seitenumbruchvorschau**
Stellen Sie ein beliebiges Arbeitsblatt auf Seitenumbruchvorschau ein, indem Sie Folgendes festlegen[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Klasse auf *true**. Dadurch wird das Arbeitsblatt von der Normalansicht zur Seitenumbruchvorschau umgeschaltet.

Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)-Methode, um den Seitenumbruch-Vorschaumodus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Zoomfaktor**
###  **Mit Microsoft Excel**
Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Mit dieser Funktion können Benutzer den Inhalt des Arbeitsblatts in kleineren oder größeren Ansichten anzeigen. Benutzer können den Zoomfaktor auf einen beliebigen Wert einstellen.
###  **Aspose.Cells & Zoomfaktor**
 Mit Aspose.Cells können Entwickler auch den Zoomfaktor des Arbeitsblatts festlegen. Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Die Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der Zoomfaktor wird durch Zuweisen eines numerischen (ganzzahligen) Werts festgelegt[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)Methode.

Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)Methode zum Festlegen des Zoomfaktors des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Fenster einfrieren**
###  **Mit Microsoft Excel**
Das Einfrieren von Fenstern ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie Daten auswählen, die beim Scrollen in einem Arbeitsblatt sichtbar bleiben.
###  **Aspose.Cells & Fenster einfrieren**
 Aspose.Cells ermöglicht es Entwicklern außerdem, zur Laufzeit eingefrorene Bereiche auf Arbeitsblätter anzuwenden. Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Die Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um eingefrorene Fenster zu konfigurieren, rufen Sie die auf[FreezePanees](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[FreezePanees](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Die Methode benötigt die folgenden Parameter:

- *Zeile**, der Zeilenindex der Zelle, ab der das Einfrieren beginnt.
- *Spalte**, der Spaltenindex der Zelle, ab der das Einfrieren beginnt.
- *Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- *Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung zeigt[FreezePanees](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)Methode zum Einfrieren von Zeilen und Spalten (beginnend mit C4, dargestellt durch die 4. Zeile und die 3. Spalte, wobei die Zeilen und Spalten beim Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Geteilte Fenster**
Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, teilen Sie die Bereiche. Microsoft Excel bietet eine sehr praktische Funktion, mit der Sie mehr als eine Kopie Ihres Arbeitsblatts anzeigen und unabhängig durch jeden Bereich Ihres Arbeitsblatts scrollen können: geteilte Bereiche.

Die Scheiben arbeiten gleichzeitig. Wenn Sie in einem eine Änderung vornehmen, wird die Änderung gleichzeitig auch im anderen angezeigt. Aspose.Cells stellt den Benutzern die Funktion „Split Panes“ zur Verfügung.
###  **Anbringen und Entfernen geteilter Fenster**
####  **Fenster teilen**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Die Klasse bietet eine breite Palette von Methoden zum Verwalten einer Excel-Datei. Um geteilte Ansichten zu implementieren, verwenden Sie die[Teilt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) Methode der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Um die geteilten Scheiben zu entfernen, verwenden Sie die[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)Methode.

Im Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird. Anschließend wird die Funktion „Teilte Bereiche festlegen“ auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Scheiben entfernen**
 Spaltscheiben mit dem entfernen[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)Methode.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
