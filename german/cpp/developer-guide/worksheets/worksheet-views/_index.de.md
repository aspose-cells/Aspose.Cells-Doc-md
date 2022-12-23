---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/cpp/worksheet-views/
---
## **Seitenumbruchvorschau**
Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenumbruchvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruchvorschau zeigt, welche Daten auf jeder Seite erscheinen, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells können Entwickler die Vorschaumodi Normalansicht oder Seitenumbruch aktivieren.
### **Ansichtsmodi steuern**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) -Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um die Vorschaumodi Normal oder Seitenumbruch zu aktivieren, verwenden Sie die[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) gibt einen booleschen Wert zurück, was bedeutet, dass nur a gespeichert werden kann**wahr** oder**FALSCH** Wert.
#### **Normalansicht aktivieren**
Versetzen Sie ein Arbeitsblatt in die normale Ansicht, indem Sie das festlegen[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse zu**FALSCH**.
#### **Seitenumbruchvorschau aktivieren**
Stellen Sie ein beliebiges Arbeitsblatt auf Seitenumbruchvorschau ein, indem Sie das einstellen[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse zu**wahr**Dadurch wird das Arbeitsblatt von der normalen Ansicht auf die Seitenumbruchvorschau umgeschaltet.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)-Methode zum Aktivieren des Seitenumbruch-Vorschaumodus für das erste Arbeitsblatt einer Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Zoomfaktor**
### **Mit Microsoft Excel**
Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, den Arbeitsblattinhalt in kleineren oder größeren Ansichten anzuzeigen. Benutzer können den Zoomfaktor auf einen beliebigen Wert einstellen.
### **Aspose.Cells & Zoomfaktor**
 Aspose.Cells ermöglicht es Entwicklern auch, den Zoomfaktor des Arbeitsblatts festzulegen. Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)-Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die[Zoomen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse Der Zoomfaktor wird eingestellt, indem der Klasse ein numerischer (ganzzahliger) Wert zugewiesen wird[Zoomen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)Methode.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[Zoomen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)Methode zum Festlegen des Zoomfaktors des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Fenster einfrieren**
### **Mit Microsoft Excel**
Fenster einfrieren ist eine Funktion, die von Microsoft Excel bereitgestellt wird. Durch das Einfrieren von Fenstern können Sie Daten auswählen, die beim Scrollen in einem Arbeitsblatt sichtbar bleiben sollen.
### **Aspose.Cells & Fenster einfrieren**
 Aspose.Cells ermöglicht es Entwicklern auch, zur Laufzeit eingefrorene Fenster auf Arbeitsblätter anzuwenden. Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)-Klasse bietet eine breite Palette von Methoden zum Verwalten von Arbeitsblättern. Rufen Sie zum Konfigurieren von Einfrierfenstern die[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)Die Methode nimmt die folgenden Parameter an:

- **Reihe**, der Zeilenindex der Zelle, bei der das Einfrieren beginnt.
- **Spalte**, der Spaltenindex der Zelle, ab der das Einfrieren beginnt.
- **Gefrorene Reihen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Säulen**, die Anzahl der sichtbaren Spalten im linken Bereich

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von zeigt[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)Methode zum Einfrieren von Zeilen und Spalten (beginnend bei C4, dargestellt durch die 4. Zeile und die 3. Spalte, wobei die Zeilen und Spalten beim Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Geteilte Scheiben**
Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten in demselben Arbeitsblatt zu erhalten, teilen Sie die Bereiche. Microsoft Excel bietet eine sehr praktische Funktion, mit der Sie mehr als eine Kopie Ihres Arbeitsblatts anzeigen und unabhängig voneinander durch jeden Bereich Ihres Arbeitsblatts scrollen können: geteilte Bereiche.

Die Scheiben arbeiten gleichzeitig. Wenn Sie in einem eine Änderung vornehmen, erscheint die Änderung gleichzeitig im anderen. Aspose.Cells stellt die Split-Pane-Funktion für die Benutzer bereit.
### **Anwenden und Entfernen von geteilten Scheiben**
#### **Teilen von Scheiben**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)-Klasse bietet eine breite Palette von Methoden zum Verwalten einer Excel-Datei. Um geteilte Ansichten zu implementieren, verwenden Sie die[Teilt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) Methode der[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Um die geteilten Scheiben zu entfernen, verwenden Sie die[Split entfernen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, dann wird die Funktion zum Festlegen von geteilten Fenstern auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Scheiben entfernen**
 Entfernen Sie geteilte Scheiben mit dem[Split entfernen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)Methode.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
