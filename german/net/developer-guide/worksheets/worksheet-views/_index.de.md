---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/net/worksheet-views/
description: Dieser Artikel beschreibt, wie man C# und die .NET API verwendet, um mit der Seitenumbruchsvorschau eines Excel Arbeitsmappen und Arbeitsblatts zu interagieren. Arbeiten mit geteilten Bereichen, fixierten Bereichen und Zoomfaktor. 
---

## **Seitenwechselvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruchvorschau zeigt an, welche Daten auf jeder Seite stehen, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells können Entwickler die Normalansicht oder die Seitenumbruchvorschau aktivieren.

### **Steuerung der Ansichtsmodi**

Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Normal- oder Seitenumbruchvorschau zu aktivieren, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) und die Eigenschaft [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview). [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) ist eine boolesche Eigenschaft, die nur einen Wert von **true** oder **false** speichern kann.

#### **Normale Ansicht aktivieren**

Legen Sie ein Arbeitsblatt auf Normalansicht, indem Sie die Eigenschaft [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **false** setzen.

#### **Aktivieren der Seitenwechselvorschau**

Legen Sie ein Arbeitsblatt auf die Seitenumbruchvorschau, indem Sie die Eigenschaft [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **true** setzen. Dadurch wird das Arbeitsblatt von der Normalansicht zur Seitenumbruchvorschau gewechselt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) verwendet wird, um den Seitenumbruchvorschau-Modus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) geöffnet. Die Ansicht wird für das erste Arbeitsblatt auf die Seitenumbruchvorschau umgeschaltet, indem die Eigenschaft [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) auf **true** gesetzt wird. Die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Zoom-Faktor**

### **Verwendung von Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht Entwicklern, den Zoomfaktor des Arbeitsblatts festzulegen.
Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Eigenschaft [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Der Zoomfaktor wird durch Zuweisen eines numerischen (ganzzahligen) Werts zur Eigenschaft [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) festgelegt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts der Excel-Datei festzulegen.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) geöffnet. Der Zoomfaktor für das erste Arbeitsblatt wird auf 75 eingestellt und die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Fenster fixieren**

### **Verwendung von Microsoft Excel**

Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

### **Aspose.Cells & Einfrieren von Fenstern**

Aspose.Cells ermöglicht Entwicklern, das Einfrieren von Zeilen und Spalten in Arbeitsblättern zur Laufzeit anzuwenden.

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um Einfrierunterschiede festzulegen, rufen Sie die [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)-Methode der Klasse Arbeitsblatt auf. Die Methode [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) nimmt die folgenden Parameter an:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

Die Datei book1.xls wird geöffnet, indem der Konstruktor der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) aufgerufen wird, während sie instanziiert wird, und einige Zeilen und Spalten werden im ersten Arbeitsblatt eingefroren. Die modifizierte Datei wird als output.xls gespeichert.

Im folgenden wird ein vollständiges Beispiel gezeigt, das zeigt, wie die Methode [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) zum Einfrieren von Zeilen und Spalten (beginnend ab C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei Zeilen und Spalten ab dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei verwendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Geteilte Fenster**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.

### **Anwenden und Entfernen von geteilten Fenstern**

#### **Teilen von Fenstern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um Split-Ansichten zu implementieren, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Methode der Klasse. Verwenden Sie zum Entfernen der Split-Panes die [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split)-Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Nach Ausführung des obigen Codes hat die generierte Datei eine Split-Ansicht.

#### **Panes entfernen**

Entfernen Sie geteilte Fenster mit der Methode [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Erweiterte Themen**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Arbeitsblattregisterfarbe festlegen](/cells/de/net/set-worksheet-tab-color/)
- [Gitternetzlinien und Zeilen- und Spaltenüberschriften anzeigen oder ausblenden](/cells/de/net/show-and-hide-gridlines-and-row-column-headers/)
- [Zeilen, Spalten und Bildlaufleisten anzeigen oder ausblenden](/cells/de/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Arbeitsblätter und Registerkarten anzeigen oder ausblenden](/cells/de/net/show-and-hide-worksheets-and-tabs/)
- [Formeln anstelle von Werten im Arbeitsblatt anzeigen](/cells/de/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Fehlerüberprüfungsoptionen verwenden](/cells/de/net/use-error-checking-options/)

{{< app/cells/assistant language="csharp" >}}
