---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/net/worksheet-views/
description:  In diesem Artikel wird beschrieben, wie Sie C# und .NET API verwenden, um mit der Seitenumbruchvorschau einer Excel-Arbeitsmappe und Arbeitsblättern zu interagieren. Arbeiten Sie auch mit geteilten Fenstern, eingefrorenen Fenstern und Zoomfaktor.
---
## **Seitenumbruchvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenumbruchvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruchvorschau zeigt, welche Daten auf jeder Seite erscheinen, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells können Entwickler die Vorschaumodi Normalansicht oder Seitenumbruch aktivieren.

### **Ansichtsmodi steuern**

Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Vorschaumodi Normal oder Seitenumbruch zu aktivieren, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) Eigentum.[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**wahr** oder ein**FALSCH** Wert.

#### **Normalansicht aktivieren**

 Versetzen Sie ein Arbeitsblatt in die normale Ansicht, indem Sie das festlegen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) Eigentum zu**FALSCH**.

#### **Seitenumbruchvorschau aktivieren**

 Stellen Sie ein beliebiges Arbeitsblatt auf Seitenumbruchvorschau ein, indem Sie das einstellen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) Eigentum zu**wahr**Dadurch wird das Arbeitsblatt von der normalen Ansicht auf die Seitenumbruchvorschau umgeschaltet.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-Eigenschaft, um den Vorschaumodus für den Seitenumbruch für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

Die Datei book1.xls wird geöffnet, indem eine Instanz der erstellt wird[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse. Durch Setzen von wird die Ansicht auf Seitenumbruchvorschau für das erste Arbeitsblatt umgeschaltet[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)Eigentum zu**wahr**. Die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Zoomfaktor**

### **Mit Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, den Arbeitsblattinhalt in kleineren oder größeren Ansichten anzuzeigen. Benutzer können den Zoomfaktor auf einen beliebigen Wert einstellen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht Entwicklern das Festlegen des Arbeitsblatt-Zoomfaktors.
Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Zoomen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)Eigentum. Der Zoomfaktor wird eingestellt, indem dem ein numerischer (ganzzahliger) Wert zugewiesen wird[**Zoomen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) Eigentum.

Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**Zoomen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) -Eigenschaft, um den Zoomfaktor des ersten Arbeitsblatts der Excel-Datei festzulegen.

Die Datei book1.xls wird geöffnet, indem eine Instanz der erstellt wird[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse. Der Zoomfaktor des ersten Arbeitsblatts wird auf 75 gesetzt und die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Fenster einfrieren**

### **Mit Microsoft Excel**

Fenster einfrieren ist eine Funktion, die von Microsoft Excel bereitgestellt wird. Durch das Einfrieren von Fenstern können Sie Daten auswählen, die beim Scrollen in einem Arbeitsblatt sichtbar bleiben sollen.

### **Aspose.Cells & Fenster einfrieren**

Aspose.Cells ermöglicht Entwicklern das Einfrieren von Fenstern zur Laufzeit auf Arbeitsblätter anzuwenden.

Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Rufen Sie zum Konfigurieren von Einfrierfenstern die Worksheet-Klasse auf.[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)Methode. Das[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)Die Methode nimmt die folgenden Parameter an:

- **Reihe**, der Zeilenindex der Zelle, bei der das Einfrieren beginnt.
- **Spalte**, der Spaltenindex der Zelle, ab der das Einfrieren beginnt.
- **Gefrorene Reihen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Säulen**, die Anzahl der sichtbaren Spalten im linken Bereich

 Die Datei book1.xls wird durch Aufrufen der geöffnet[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klassenkonstruktor beim Instanziieren und einige Zeilen und Spalten werden im ersten Arbeitsblatt eingefroren. Die geänderte Datei wird als output.xls gespeichert.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von zeigt[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)Methode zum Einfrieren von Zeilen und Spalten (beginnend bei C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei die Zeilen und Spalten mit dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Geteilte Scheiben**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten in demselben Arbeitsblatt zu erhalten, teilen Sie die Bereiche. Microsoft Excel bietet eine sehr praktische Funktion, mit der Sie mehr als eine Kopie Ihres Arbeitsblatts anzeigen und unabhängig voneinander durch jeden Bereich Ihres Arbeitsblatts scrollen können: geteilte Bereiche.

Die Scheiben arbeiten gleichzeitig. Wenn Sie in einem eine Änderung vornehmen, erscheint die Änderung gleichzeitig im anderen. Aspose.Cells stellt die Split-Pane-Funktion für die Benutzer bereit.

### **Anwenden und Entfernen von geteilten Scheiben**

#### **Teilen von Scheiben**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um geteilte Ansichten zu implementieren, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Teilt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Um die geteilten Scheiben zu entfernen, verwenden Sie die[**Split entfernen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, dann wird die Funktion zum Festlegen von geteilten Fenstern auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Nach dem Ausführen des obigen Codes hat die generierte Datei eine geteilte Ansicht.

#### **Scheiben entfernen**

 Entfernen Sie geteilte Scheiben mit dem[**Split entfernen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Themen vorantreiben**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Legen Sie die Farbe des Arbeitsblatt-Tabs fest](/cells/de/net/set-worksheet-tab-color/)
- [Rasterlinien und Spaltenüberschriften ein- und ausblenden](/cells/de/net/show-and-hide-gridlines-and-row-column-headers/)
- [Anzeigen und Ausblenden von Zeilen, Spalten und Bildlaufleisten](/cells/de/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Arbeitsblätter und Registerkarten ein- und ausblenden](/cells/de/net/show-and-hide-worksheets-and-tabs/)
- [Zeigen Sie Formeln anstelle von Werten in einem Arbeitsblatt an](/cells/de/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Verwenden Sie die Optionen zur Fehlerprüfung](/cells/de/net/use-error-checking-options/)

