---
title: Arbeitsblattansichten
type: docs
weight: 40
url: /de/python-net/worksheet-views/
description: Dieser Artikel beschreibt, wie man mit der Aspose.Cells für Python via .NET API den Seitenumbruch Vorschau eines Excel Arbeitsbuchs und Arbeitsblättern steuert. Arbeiten Sie mit geteilten Fenstern, eingefrorenen Fenstern und Zoom Faktor. 
keywords: Python Excel Bibliothek, Python Wie man die Seitenumbruch Vorschau einstellt, Python Wie man den Normalansicht aktiviert, Python Wie man den Zoom Faktor einstellt, Python Wie man Fenster einfriert, Python Wie man Fenster teilt, Python Wie man Fenster entfernt.
---

## **Seitenwechselvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Die Normalansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruch-Vorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruch-Vorschau zeigt, welche Daten auf jede Seite passen, damit Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells für Python via .NET können Entwickler die Normalansicht oder die Seitenumbruch-Vorschau aktivieren.

### **Steuerung der Ansichtsmodi**

Aspose.Cells für Python via .NET bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Normal- oder Seitenumbruchvorschau zu aktivieren, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) und die Eigenschaft [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview). [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) ist eine boolesche Eigenschaft, die nur einen Wert von **true** oder **false** speichern kann.

#### **Normale Ansicht aktivieren**

Legen Sie ein Arbeitsblatt auf Normalansicht, indem Sie die Eigenschaft [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **false** setzen.

#### **Aktivieren der Seitenwechselvorschau**

Legen Sie ein Arbeitsblatt auf die Seitenumbruchvorschau, indem Sie die Eigenschaft [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **true** setzen. Dadurch wird das Arbeitsblatt von der Normalansicht zur Seitenumbruchvorschau gewechselt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) verwendet wird, um den Seitenumbruchvorschau-Modus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) geöffnet. Die Ansicht wird für das erste Arbeitsblatt auf die Seitenumbruchvorschau umgeschaltet, indem die Eigenschaft [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) auf **true** gesetzt wird. Die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Zoom-Faktor**

### **Verwendung von Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht Entwicklern, den Zoomfaktor des Arbeitsblatts festzulegen.
Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Eigenschaft [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Der Zoomfaktor wird durch Zuweisen eines numerischen (ganzzahligen) Werts zur Eigenschaft [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) festgelegt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts der Excel-Datei festzulegen.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) geöffnet. Der Zoomfaktor für das erste Arbeitsblatt wird auf 75 eingestellt und die geänderte Datei wird als output.xls gespeichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Fenster fixieren**

### **Verwendung von Microsoft Excel**

Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

### **Aspose.Cells & Einfrieren von Fenstern**

Aspose.Cells ermöglicht Entwicklern, das Einfrieren von Zeilen und Spalten in Arbeitsblättern zur Laufzeit anzuwenden.

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um Einfrierunterschiede festzulegen, rufen Sie die [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int)-Methode der Klasse Arbeitsblatt auf. Die Methode [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) nimmt die folgenden Parameter an:

- **row**, der Zeilenindex, ab dem der Freeze beginnt.
- **column**, der Spaltenindex, ab dem der Freeze beginnt.
- **frozen_rows**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **frozen_columns**, die Anzahl der sichtbaren Spalten im linken Bereich.

Die Datei book1.xls wird geöffnet, indem der Konstruktor der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) aufgerufen wird, während sie instanziiert wird, und einige Zeilen und Spalten werden im ersten Arbeitsblatt eingefroren. Die modifizierte Datei wird als output.xls gespeichert.

Im folgenden wird ein vollständiges Beispiel gezeigt, das zeigt, wie die Methode [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) zum Einfrieren von Zeilen und Spalten (beginnend ab C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei Zeilen und Spalten ab dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei verwendet wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Geteilte Fenster**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.

### **Anwenden und Entfernen von geteilten Fenstern**

#### **Teilen von Fenstern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um Split-Ansichten zu implementieren, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Methode der Klasse. Verwenden Sie zum Entfernen der Split-Panes die [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split)-Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Nach Ausführung des obigen Codes hat die generierte Datei eine Split-Ansicht.

#### **Panes entfernen**

Entfernen Sie geteilte Fenster mit der Methode [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Erweiterte Themen**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Arbeitsblattregisterfarbe festlegen](/cells/de/python-net/set-worksheet-tab-color/)
- [Gitternetzlinien und Zeilen- und Spaltenüberschriften anzeigen oder ausblenden](/cells/de/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Zeilen, Spalten und Bildlaufleisten anzeigen oder ausblenden](/cells/de/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Arbeitsblätter und Registerkarten anzeigen oder ausblenden](/cells/de/python-net/show-and-hide-worksheets-and-tabs/)
- [Formeln anstelle von Werten im Arbeitsblatt anzeigen](/cells/de/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Fehlerüberprüfungsoptionen verwenden](/cells/de/python-net/use-error-checking-options/)

