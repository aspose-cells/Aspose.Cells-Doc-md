---
title: Arbeitsblattansichten
type: docs
weight: 10
url: /de/java/worksheet-views/
---

## **Seitenwechselvorschau**
Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Die normale Ansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenwechselvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenwechselvorschau zeigt an, welche Daten auf jeder Seite erscheinen, sodass Sie den Druckbereich und die Seitenwechsel anpassen können. Mit Aspose.Cells können Entwickler die normale Ansicht oder die Seitenwechselvorschau aktivieren.
### **Steuerung der Ansichtsmodi**
Aspose.Cells bietet eine [Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse, die eine Microsoft Excel-Datei repräsentiert. Die [Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse repräsentiert. Die [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Ansichtsmodi 'normal' oder 'Seitenwechselvorschau' zu aktivieren, verwenden Sie die [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-Methode der [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse.
#### **Normale Ansicht aktivieren**
Setzen Sie jedes Arbeitsblatt auf die normale Ansicht, indem Sie die Methode [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) der [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse verwenden und **false** als Parameter übergeben.
#### **Aktivieren der Seitenwechselvorschau**
Setzen Sie ein Arbeitsblatt mit der [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) Methode der [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse und übergeben Sie **true** als Parameter.

Ein vollständiges Beispiel finden Sie unten, das die Verwendung der Methode [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) der [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse zeigt, um den Seitenwechselvorschau-Modus für das erste Arbeitsblatt der Excel-Datei zu aktivieren.

Im folgenden Screenshot sehen Sie, dass die Datei Book1.xls im Normalmodus geöffnet ist.

**Book1.xls: Arbeitsblatt vor der Änderung** 

![todo:image_alt_text](worksheet-views_1.png)

Book1.xls wird mit der [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse geöffnet und der Modus für das erste Arbeitsblatt wird auf Seitenwechselvorschau umgeschaltet. Die geänderte Datei wird als output.xls gespeichert.

**Ouput.xls: Arbeitsblatt nach der Änderung** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Zoom-Faktor**
Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

**Festlegen des Zoomfaktors mit Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells ermöglicht es Entwicklern auch, den Zoomfaktor des Arbeitsblatts festzulegen.
### **Steuerung des Zoomfaktors**
Aspose.Cells bietet eine [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts einzustellen, verwenden Sie die Methode [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Ein vollständiges Beispiel ist unten angegeben, das zeigt, wie die Methode [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts in einer Excel-Datei festzulegen.

Im folgenden Screenshot sehen Sie die Datei Book1.xls im Standardmodus.

**Book1.xls: Arbeitsblatt vor der Änderung** 

![todo:image_alt_text](worksheet-views_4.png)

Die Datei Book1.xls wird mit der [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse geöffnet und der Zoomfaktor des ersten Arbeitsblatts wird auf 75 gesetzt. Die modifizierte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Fenster fixieren**
Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

**Verwenden von Freeze Panes in Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Auch Aspose.Cells ermöglicht Entwicklern, Freeze Panes zur Laufzeit auf Arbeitsblättern anzuwenden.

Aspose.Cells stellt eine [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse zur Verfügung, die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Freeze-Panes zu konfigurieren, rufen Sie die Methode [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) auf. Die Methode [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) nimmt die folgenden Parameter:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Eingefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich

Ein vollständiges Beispiel zeigt, wie die Methode [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) mit [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) genutzt wird, um Zeilen und Spalten (beginnend bei C4, dargestellt durch die 4. Zeile und die 3. Spalte, wobei die Zeilen und Spalten bei 0 beginnen) des ersten Arbeitsblatts in der Excel-Datei zu sperren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Im Screenshot unten sehen Sie die Datei Book1.xls ohne Freeze Panes.

**Book1.xls: Arbeitsblattansicht vor jeglicher Änderung** 

![todo:image_alt_text](worksheet-views_7.png)

Die Datei Book1.xls wird mit der [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse geöffnet und dann werden einige Zeilen und Spalten auf dem ersten Arbeitsblatt eingefroren. Die modifizierte Datei wird als output.xls gespeichert.

**Outlook.xls: Arbeitsblattansicht nach der Änderung** 

![todo:image_alt_text](worksheet-views_8.png)
## **Geteilte Fenster**
Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.
### **Anwenden und Entfernen von geteilten Fenstern**
#### **Teilen von Fenstern**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Excel-Dateien. Um geteilte Ansichten zu implementieren, verwenden Sie die Methode [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split--) der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Um gespaltene Bereiche zu entfernen, verwenden Sie die Methode [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--).

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Nachdem der obige Code ausgeführt wurde, hat die generierte Datei eine geteilte Ansicht.

**Geteilte Ansichten in der Ausgabedatei** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Panes entfernen**
Entwickler können gespaltene Bereiche mit der Methode [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) der Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) entfernen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Erweiterte Themen**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Arbeitsblattregisterfarbe festlegen](/cells/de/java/set-worksheet-tab-color/)
- [Elemente anzeigen und ausblenden](/cells/de/java/show-and-hide-elements/)
- [Formeln anstelle von Werten in einem Arbeitsblatt anzeigen](/cells/de/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Fehlerüberprüfungsoptionen verwenden](/cells/de/java/use-error-checking-options/)
{{< app/cells/assistant language="java" >}}
